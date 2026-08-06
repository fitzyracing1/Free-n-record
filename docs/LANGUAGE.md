# Free(n) Task Language (.free)

The `.free` format is a simple, human-readable, language-neutral way to declare Tasks and their relationships.  
It is **not** a full programming language; it is a declaration format that a Runtime or a host language can load.

## Minimal Syntax (v0.1)

```
task <name>:
  deps: <name1>, <name2>, ...
  n: <integer>          # optional hint
  body: |
    <opaque text or host-language snippet>
```

## Example

```
task prepare:
  body: |
    context["data"] = load_input()

task compute:
  deps: prepare
  n: 2
  body: |
    result = heavy_work(context["data"], depth=n)
    context["result"] = result

task report:
  deps: compute
  body: |
    emit(context["result"])
```

## Design Notes

- The `body` is intentionally opaque. A Python runtime may treat it as Python; a future compiler may translate it.
- Dependencies are by name only.
- `n` on a Task is a *hint*; the Runtime may override it according to global State and resources.
- Comments start with `#`.

## Future

A more formal grammar, type annotations, and first-class support for AI / quantum primitives may appear in later versions.  
The core protocol remains independent of this surface syntax.
