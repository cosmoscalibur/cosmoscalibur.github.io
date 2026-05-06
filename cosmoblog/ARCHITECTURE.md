# Cosmoblog — Architecture Decisions

This document records the key architecture decisions made during the
Cosmoblog engine implementation. Each entry explains the *why* behind
non-obvious design choices.

---

## 1. Metadata Source: `env.metadata` over Docinfo Nodes

**Decision:** Read post frontmatter from `env.metadata[docname]` instead
of parsing `docinfo` nodes in the doctree.

**Context:** MyST-Parser extracts YAML frontmatter from `.md` files and
stores it in `env.metadata[docname]` during the parsing phase. By the time
the `doctree-read` event fires, the `docinfo` nodes have already been
consumed and removed from the doctree. Attempting to parse docinfo nodes
results in an empty dictionary.

**Fallback:** For non-MyST sources (`.rst`), a fallback path parses
`docinfo` nodes from the doctree if `env.metadata` is empty.

---

## 2. Picklable PostInfo (No Doctree Storage)

**Decision:** Store post excerpts as plain text strings, not as docutils
`Node` objects.

**Context:** Sphinx pickles the `BuildEnvironment` between phases (read →
write). Storing docutils nodes in `PostInfo.excerpt` caused
`PickleError` because nodes contain non-picklable references (parent
pointers, document references). Converting excerpts to text at
registration time ensures the entire `BlogEngine` can be pickled and
restored across build phases.

**Trade-off:** Excerpts lose inline markup (bold, links, code). This is
acceptable because excerpts are used for feed summaries and postlist
previews where plain text is sufficient.

---

## 3. `env-merge-info` for Parallel Read Support

**Decision:** Implement the `env-merge-info` Sphinx event handler to merge
`BlogEngine` state from parallel reader worker processes.

**Context:** When `sphinx-build` runs with parallel readers (`-j auto`),
each worker gets a **copy** of the environment. Posts registered in worker
processes are lost unless explicitly merged back. The `env-merge-info`
handler collects posts from each worker's `env.cosmoblog.posts` dictionary
and merges them into the main process.

---

## 4. Language Discovery via Directory Scanning

**Decision:** Infer supported languages by scanning `{srcdir}/*/blog/`
directories instead of requiring explicit configuration.

**Context:** The blog follows a `{lang}/blog/{year}/{slug}.md` path
convention. Scanning for directories with a `blog/` subdirectory at the
first level automatically discovers all languages (e.g., `es`, `en`).
This eliminates a configuration step and ensures new languages are
picked up without config changes.

**Override:** The `cosmoblog_languages` config option can override
auto-discovery when needed.

---

## 5. CSS Class Naming (`cosmoblog-*`)

**Decision:** Emit `cosmoblog-post`, `cosmoblog-post-title`,
`cosmoblog-post-excerpt`, and `cosmoblog-sidebar-item` CSS class names
in generated HTML.

**History:** During initial migration, `ablog-*` class names were kept
to avoid CSS churn while the engine was unstable. Once the engine
stabilised (Phase 2 complete), all CSS selectors and Python emitters
were renamed to `cosmoblog-*` atomically to eliminate naming confusion.

---

## 6. Single-Pass Post Registration

**Decision:** Register all post metadata in a single pass during
`doctree-read`, instead of multi-pass or lazy resolution.

**Context:** Each blog post's frontmatter (date, tags, category, language)
is extracted once during the read phase and stored in a `PostInfo`
dataclass. This avoids repeated doctree traversals and ensures all
metadata is available for feed generation and tag page creation in the
`html-collect-pages` phase.

---

## 7. Feed Generation via `html-collect-pages`

**Decision:** Generate Atom feeds as virtual pages yielded from the
`html-collect-pages` event, rather than writing files in a custom builder.

**Context:** Sphinx's `html-collect-pages` is the standard hook for
generating pages that don't correspond to source documents. Yielding
`(pagename, context, template)` tuples integrates naturally with Sphinx's
output pipeline and ensures feeds are included in incremental builds.

The feed XML is generated directly (no Jinja template) since Atom XML
has a fixed structure that doesn't benefit from templating.

---

## 8. First Image Extraction for Postlist Cards

**Decision:** Extract the URI and alt text of the first `nodes.image` in
the post's doctree during `doctree-read` and store them as plain strings
in `PostInfo.image` and `PostInfo.image_alt`.

**Context:** ABlog stored the full docutils node tree in the excerpt,
which automatically included images rendered inline. After switching to
plain text excerpts (Decision #2), images were lost from listing pages.
Extracting the first image URI during registration restores visual parity.

**Rendering:** In `directives.py`, the image is rendered after the text
excerpt as a `<a class="image-reference"><img></a>` wrapper, matching
ABlog's production HTML structure so the existing CSS applies unchanged.

---

## 9. Doctree Post-Transforms over HTML Regex

**Decision:** Move lazy-loading and image dimension injection from
post-build HTML regex processing into Sphinx `SphinxPostTransform`
subclasses that operate on the doctree before rendering.

**Context:** The original optimizer used regex patterns on rendered HTML
to add `loading="lazy"` and `width`/`height` attributes.  This is
fragile (regexes can mismatch minified HTML) and doesn't apply to
nodes generated at write-time (e.g., postlist card images).
Post-transforms run at write time (after `doctree-resolved`), so they
see the fully resolved doctree including dynamically generated nodes.

**Transforms:**
- `LazyImageTransform` (priority 800): Sets `loading="lazy"` on all
  images except the first (assumed above-the-fold / LCP candidate).
- `ImageDimensionsTransform` (priority 810): Reads source image files
  (header-only, no Pillow) to inject `width`/`height` attributes,
  preventing Cumulative Layout Shift (CLS).

---

## 10. WebP Conversion in Post-Build (Output Only)

**Decision:** Convert images to WebP and rewrite HTML references as
post-build processing in the theme optimizer, operating exclusively
on the output directory (`_images/`).

**Context:** Two alternative approaches were evaluated and rejected:

1. **Read-phase transform** — Creating `.webp` in the source tree
   before `ImageCollector` runs.  Pollutes the source tree with build
   artifacts and conflicts with legitimately committed WebP source
   files.

2. **Post-transform URI rewrite** — Changing `node['uri']` from
   `.png` to `.webp` at write time, so HTML is generated correctly.
   Not feasible because Sphinx's per-document write flow is:

       apply_post_transforms()  →  post_process_images()  →  write_doc()

   `post_process_images()` populates `builder.images[uri] = basename`
   using the node URI.  `write_doc()` looks up `builder.images[uri]`
   to resolve the output path.  There is no hook between these two
   steps, so rewriting the URI in a post-transform (which runs
   before `post_process_images`) breaks the lookup.

**Approach:** The optimizer converts PNG/JPEG in `_images/` after
Sphinx finishes writing, then rewrites `_images/*.png|jpg` references
in HTML via a targeted regex.  This keeps the source tree clean and
handles images from all sources (blog posts, jupyter outputs, etc.)
uniformly.

