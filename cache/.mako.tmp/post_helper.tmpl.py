# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499824173.079447
_enable_loop = True
_template_filename = 'themes/carpet/templates/post_helper.tmpl'
_template_uri = 'post_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['meta_translations', 'twitter_card_information', 'mathjax_script', 'html_tags', 'html_pager', 'open_graph_metadata']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        translations = context.get('translations', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        len = context.get('len', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            for langname in sorted(translations):
                if langname != lang and ((not post.skip_untranslated) or post.is_translation_available(langname)):
                    __M_writer('      <link rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('" href="')
                    __M_writer(str(post.permalink(langname)))
                    __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_twitter_card_information(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        twitter_card = context.get('twitter_card', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if twitter_card and twitter_card['use_twitter_cards']:
            __M_writer('  <meta name="twitter:card" content="')
            __M_writer(filters.html_escape(str(twitter_card.get('card', 'summary'))))
            __M_writer('">\n  \n')
            if 'site:id' in twitter_card:
                __M_writer('    <meta name="twitter:site:id" content="')
                __M_writer(str(twitter_card['site:id']))
                __M_writer('">\n')
            elif 'site' in twitter_card:
                __M_writer('    <meta name="twitter:site" content="')
                __M_writer(str(twitter_card['site']))
                __M_writer('">\n')
            __M_writer('  \n')
            if 'creator:id' in twitter_card:
                __M_writer('    <meta name="twitter:creator:id" content="')
                __M_writer(str(twitter_card['creator:id']))
                __M_writer('">\n')
            elif 'creator' in twitter_card:
                __M_writer('    <meta name="twitter:creator" content="')
                __M_writer(str(twitter_card['creator']))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mathjax_script(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        katex_auto_render = context.get('katex_auto_render', UNDEFINED)
        use_katex = context.get('use_katex', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.is_mathjax:
            if use_katex:
                __M_writer('    <script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.6.0/katex.min.js"></script>\n    <script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.6.0/contrib/auto-render.min.js"></script>\n')
                if katex_auto_render:
                    __M_writer('      <script>\n        renderMathInElement(document.body,\n          {\n            ')
                    __M_writer(str(katex_auto_render))
                    __M_writer('\n          }\n        );\n      </script>\n')
                else:
                    __M_writer('      <script>\n        renderMathInElement(document.body);\n      </script>\n')
            else:
                __M_writer('    <script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"> </script>\n    \n')
                if mathjax_config:
                    __M_writer('      ')
                    __M_writer(str(mathjax_config))
                    __M_writer('\n')
                else:
                    __M_writer('      <script type="text/x-mathjax-config">\n        MathJax.Hub.Config({tex2jax: {inlineMath: [[\'$latex \',\'$\'], [\'\\\\(\',\'\\\\)\']]}});\n      </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_tags(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        hidden_tags = context.get('hidden_tags', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.tags:
            __M_writer('  <div class="columns tags" itemprop="keywords">\n')
            for tag in post.tags:
                if tag not in hidden_tags:
                    __M_writer('        <div class="column has-text-centered">\n          <a class="tag is-primary is-medium p-category" href="')
                    __M_writer(str(_link('tag', tag)))
                    __M_writer('" rel="tag">')
                    __M_writer(filters.html_escape(str(tag)))
                    __M_writer('</a>\n        </div>\n')
            __M_writer('  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_pager(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.prev_post or post.next_post:
            __M_writer('  <div class="columns">\n    <div class="column">\n      <nav class="pagination pager hidden-print">\n')
            if post.prev_post:
                __M_writer('          <a class="pagination-previous previous" href="')
                __M_writer(str(post.prev_post.permalink()))
                __M_writer('" rel="prev" title="')
                __M_writer(filters.html_escape(str(post.prev_post.title())))
                __M_writer('">')
                __M_writer(str(messages("Previous post")))
                __M_writer('</a>\n')
            if post.next_post:
                __M_writer('          <a class="pagination-next next" href="')
                __M_writer(str(post.next_post.permalink()))
                __M_writer('" rel="next" title="')
                __M_writer(filters.html_escape(str(post.next_post.title())))
                __M_writer('">')
                __M_writer(str(messages("Next post")))
                __M_writer('</a>\n')
            __M_writer('      </nav>\n    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_open_graph_metadata(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        blog_title = context.get('blog_title', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_open_graph:
            __M_writer('  <meta property="og:site_name" content="')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('">\n  <meta property="og:title" content="')
            __M_writer(filters.html_escape(str(post.title()[:70])))
            __M_writer('">\n  <meta property="og:url" content="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\n  \n')
            if post.description():
                __M_writer('    <meta property="og:description" content="')
                __M_writer(filters.html_escape(str(post.description()[:200])))
                __M_writer('">\n')
            else:
                __M_writer('    <meta property="og:description" content="')
                __M_writer(filters.html_escape(str(post.text(strip_html=True)[:200])))
                __M_writer('">\n')
            __M_writer('  \n')
            if post.previewimage:
                __M_writer('    <meta property="og:image" content="')
                __M_writer(str(url_replacer(permalink, post.previewimage, lang, 'absolute')))
                __M_writer('">\n')
            __M_writer('  \n  <meta property="og:type" content="article">\n\n')
            __M_writer('  \n')
            if post.date.isoformat():
                __M_writer('    <meta property="article:published_time" content="')
                __M_writer(str(post.formatted_date('webiso')))
                __M_writer('">\n')
            __M_writer('  \n')
            if post.tags:
                for tag in post.tags:
                    __M_writer('      <meta property="article:tag" content="')
                    __M_writer(filters.html_escape(str(tag)))
                    __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/carpet/templates/post_helper.tmpl", "source_encoding": "utf-8", "uri": "post_helper.tmpl", "line_map": {"16": 0, "21": 2, "22": 11, "23": 25, "24": 42, "25": 77, "26": 95, "27": 127, "33": 3, "41": 3, "42": 4, "43": 5, "44": 6, "45": 7, "46": 7, "47": 7, "48": 7, "49": 7, "55": 79, "60": 79, "61": 80, "62": 81, "63": 81, "64": 81, "65": 83, "66": 84, "67": 84, "68": 84, "69": 85, "70": 86, "71": 86, "72": 86, "73": 88, "74": 89, "75": 90, "76": 90, "77": 90, "78": 91, "79": 92, "80": 92, "81": 92, "87": 97, "94": 97, "95": 98, "96": 99, "97": 100, "98": 102, "99": 103, "100": 106, "101": 106, "102": 110, "103": 111, "104": 115, "105": 116, "106": 118, "107": 119, "108": 119, "109": 119, "110": 120, "111": 121, "117": 13, "123": 13, "124": 14, "125": 15, "126": 16, "127": 17, "128": 18, "129": 19, "130": 19, "131": 19, "132": 19, "133": 23, "139": 27, "144": 27, "145": 28, "146": 29, "147": 32, "148": 33, "149": 33, "150": 33, "151": 33, "152": 33, "153": 33, "154": 33, "155": 35, "156": 36, "157": 36, "158": 36, "159": 36, "160": 36, "161": 36, "162": 36, "163": 38, "169": 44, "179": 44, "180": 45, "181": 46, "182": 46, "183": 46, "184": 47, "185": 47, "186": 48, "187": 48, "188": 50, "189": 51, "190": 51, "191": 51, "192": 52, "193": 53, "194": 53, "195": 53, "196": 55, "197": 56, "198": 57, "199": 57, "200": 57, "201": 59, "202": 66, "203": 67, "204": 68, "205": 68, "206": 68, "207": 70, "208": 71, "209": 72, "210": 73, "211": 73, "212": 73, "218": 212}}
__M_END_METADATA
"""
