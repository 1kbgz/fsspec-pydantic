# Why paths keep their filesystem

A remote path needs both an address within a backend and a filesystem that knows
how to reach it. A plain `pathlib.Path` supplies local path operations but does not
contain remote credentials or backend behavior. The package's `Path` stores those
two pieces together.

## Models hold objects and serialize strings

Applications need filesystem methods at runtime, while configuration formats need
serializable values. Pydantic metadata converts URL input into filesystem and path
objects, then serializes those objects back to URL strings.

A URL does not fully describe a filesystem session. Authentication, connection
options, and backend state can be absent from the serialized value. A model dump
therefore provides an address representation rather than a complete connection
backup.

## Existence checks depend on when validation runs

A file or directory check describes backend state at validation time. It does not
reserve the object or ensure that a later read succeeds. Remote validation can
also make network calls. Stored path kinds make repeated object use inexpensive,
but they can become stale when backend contents change.

See [Type reference](reference.md) for alias behavior and the
[validation guide](how-to-validate.md) for explicit existence checks.
