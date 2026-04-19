---
date: 2026-04-18
tags: python, rust, performance, ruff, uv, polars, pyo3, maturin, pydantic, cpython
category: programming, technology
language: en
---

# Rust Ecosystem in Python

For years, the Python ecosystem has grappled with the "two-language problem": we
write code in Python for its ergonomics, but when performance becomes critical,
we drop down to C or C++. This transition has always been painful, introducing
memory safety risks and considerable maintenance complexity. However, we are
witnessing a paradigm shift. **Rust has become the new standard for building
Python infrastructure.**

This phenomenon is no accident. Rust offers what C++ never could: guaranteed
memory safety at compile time and a concurrency model that allows us to safely
bypass the dreaded *Global Interpreter Lock* (GIL).

## Critical Infrastructure: The Invisible Engine

We often don't realize it, but many of the libraries we use daily have been
silently rebuilt in Rust to optimize critical processes.

- **{program}`pydantic-core`**: With the arrival of Pydantic V2, the validation
  engine was completely rewritten in Rust. The result is a performance
  improvement of between 5x and 50x. Since Pydantic is the foundation for
  frameworks like {program}`FastAPI`, this change has accelerated thousands of
  applications without developers having to change a single line of their
  models.
- **{program}`cryptography`**: One of the most downloaded packages on PyPI now
  uses Rust for critical parts of its logic. This not only improves speed but
  drastically reduces the attack surface for memory errors in an area where
  security is paramount.

## Development and Management Tools: The Astral Era

If one company exemplifies this revolution, it is *Astral*. Their approach
hasn't just been "make it faster," but to consolidate fragmented tools.

- **{program}`ruff`**: It has replaced *flake8*, *isort*, *black*, and others
  in a single binary. The difference isn't just marginal; it's instantaneous even
  in monorepos with millions of lines.
- **{program}`uv`**: It's not just a package installer. It's a complete
  management system for Python versions, virtual environments, and dependencies.
  As I shared in my [article on uv](/en/blog/2024/uv-alternativa-rapida-a-pip-y-venv.md),
  its speed is due to intensive use of parallelism and extremely aggressive
  cache management.
- **{program}`ty`**: The new type checker aiming to succeed *Mypy* and
  *Pyright*. By performing static analysis in Rust, it offers real-time feedback
  in the editor—something that was previously prohibitive in large projects.

## Libraries for Processing and Services

Beyond tooling, data processing has seen a quantitative leap thanks to modern
standards and native optimization.

- **{program}`polars`**: Unlike *Pandas*, {program}`polars` uses a fully
  vectorized and lazy execution engine written in Rust, based internally on the
  **Apache Arrow** memory standard. This allows for efficient memory layout and
  *zero-copy* operations that maximize modern hardware performance.
- **{program}`connectorx`**: This is the fastest way to load data from SQL
  databases into DataFrames. Its native integration with {program}`polars`
  (via the `pl.read_database` command with `engine="connectorx"`) allows for
  moving millions of rows into a DataFrame using parallel connections without the
  usual Python bottlenecks.
- **{program}`tiktoken`**: OpenAI's tokenization library. In the world of LLMs,
  converting text into tokens is a constant and heavy task; doing it in Rust
  allows processing thousands of documents per second without blocking Python's
  main loop.

Regarding servers, while {program}`robyn` attempts to be a complete alternative
to {program}`FastAPI`, projects like **{program}`granian`** are proving that a
high-performance HTTP server can be built in Rust that is more stable and
faster than traditional *Uvicorn*-based ones.

## Specific Use Cases and Utilities

Even in more everyday tasks, Rust is gaining ground as a direct optimization
tool:

- **{program}`fastexcel`**: Based on the **Calamine** Rust library, it is
   incredibly fast at reading heavy Excel files. In fact, it serves as the
  default and most efficient Excel reading engine for {program}`polars`.
- **{program}`rensa`**: Positioned as a modern alternative to `datasketch` or
  `pyminhash` for text similarity tasks using *MinHash*. In my experience, it has
  been fundamental for **automatic conversation template detection**, allowing
  for almost instant deduplication of large datasets.
- **{program}`orjson`**: It remains the gold standard for JSON serialization. It
  can be integrated as a serializer in **Django** (for instance, through the
  *Django REST Framework*) to drastically improve API response speeds.

## Native Extension Development: PyO3 and Maturin

This surge would not be possible without the ecosystem for creating native
extensions. **{program}`PyO3`** is the framework that allows exposing Rust code
to Python with minimal friction. It has displaced *Cython* and direct C API
usage from *CPython* due to its ability to prevent segfaults and allow the use
of modern abstractions like generics and traits.

Its greatest advantage is the **automatic mapping of standard data types** (such
as lists, dictionaries, and strings), which greatly reduces the manual work at
the interface between both languages. However, for an extension to be truly
effective and leverage Rust's full potential, it is vital to follow recommended
design practices:

1.  **GIL Management**: The true power of Rust is unleashed by using
    `py.allow_threads` to release the *Global Interpreter Lock* during intensive
    computations, enabling true parallelism.
2.  **Error Mapping**: It is essential to transform Rust `Result` types into
    appropriate Python exceptions (`PyValueError`, `PyTypeError`) so that the
    end-user experience is consistent.
3.  **Decoupling**: A key practice is to keep the pure Rust logic in a crate
    separate from the Python bindings, which facilitates unit testing and code
    reuse.

Finally, with **{program}`maturin`**, distributing binaries (wheels) for
multiple platforms is now a trivial process compared to the traditional
complexities of *setuptools*.

## Rust in the Core: The Future of CPython

Perhaps the most impactful news is that the relationship between both languages
is no longer just "neighborly," but one of deep integration. There is an official
initiative, known as **"Rust for CPython,"** which seeks to introduce Rust into
the interpreter's own source tree.

The goal is to allow critical parts of CPython—especially those that are
difficult to maintain or error-prone in C—to be rewritten in Rust. It is expected
that **Python 3.16** will be the first version to officially include Rust
components, marking the beginning of an era where the language core will be
safer and easier to evolve.

## Critical Review: Is It Always the Solution?

Despite the benefits, this "Rustification" comes at a cost. The contribution
barrier is raised: a Python developer wanting to fix a bug in the core of
{program}`ruff` must now know Rust. Additionally, binary compilation introduces
a layer of complexity in CI/CD systems that isn't always justified for small
tools.

However, for core infrastructure, the verdict is clear: Python is the language
of the interface, but Rust is, increasingly, the language of the engine.

## References

- [Rust for CPython: Discussion and Roadmap](https://discuss.python.org/t/rust-for-cpython/). Python Discourse.
- [Py2RS: Python to Rust guide](https://rochacbruno.github.io/py2rs/index.html). Bruno Rocha.
- [Rusty Python: How we use Rust to speed up Python](https://ohadravid.github.io/posts/2023-03-rusty-python/). Ohad Ravid.
- [Nine rules for writing Python extensions in Rust](https://medium.com/data-science/nine-rules-for-writing-python-extensions-in-rust-d35ea3a4ec29). Medium.
- [PyO3: Rust bindings for Python](https://pyo3.rs/).
- [Maturin: Build and publish crates with pyo3](https://www.maturin.rs/).
- [Pydantic-core: The engine of Pydantic V2](https://github.com/pydantic/pydantic-core).
- [Polars: Blazingly fast DataFrames with Apache Arrow](https://pola.rs/).
- [ConnectorX: Fast SQL to DataFrame library](https://github.com/sfu-db/connector-x).
- [Fastexcel: Fast Excel reader based on Calamine](https://github.com/ToucanToco/fastexcel).
- [Rensa: High-performance MinHash library](https://github.com/beowolx/rensa).
- [Orjson: Fast JSON library for Python](https://github.com/ijl/orjson).
- [Tiktoken: OpenAI's fast tokenizer](https://github.com/openai/tiktoken).
- [Robyn: A high-performance web framework](https://robyn.tech/).
- [Granian: A Rust HTTP server for Python](https://github.com/emmett-framework/granian).
- [Astral: The future of Python tooling](https://astral.sh/).
