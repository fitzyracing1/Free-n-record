# Contributing to Free(n) Computing Platform

Thank you for your interest in contributing to the Free(n) Computing Platform.

Free(n) is a language-neutral open specification for adaptive, iterative, resource-aware computing. Contributions that improve clarity, correctness, examples, or reference implementations are welcome.

## How to Contribute

1. **Discuss first**  
   Open an issue describing the change before submitting a large PR. This keeps the specification coherent.

2. **Specification changes**  
   - Edit files under `docs/` or `reference/`.  
   - Keep language precise and implementation-agnostic.  
   - Update the roadmap if the change affects versioning.

3. **Reference implementations**  
   - Place language-specific code under `runtime/<language>/`.  
   - Include a short README explaining how to run the example.  
   - Prefer minimal, readable code that demonstrates the State / Scheduler / Execution loop.

4. **Examples**  
   - Add `.free` files under `examples/`.  
   - Keep them short and focused on one concept (hello, scheduler, distributed, AI, etc.).

5. **Pull requests**  
   - Use clear commit messages.  
   - Reference related issues.  
   - Ensure the PR description explains *why* the change is needed.

## Design Principles

- Everything is a task.
- Everything is iterative.
- Everything adapts to available resources.
- State is always `(n, i, context)`.
- Prefer simplicity over cleverness.
- Keep the core protocol language-neutral.

## Code of Conduct

Please read and follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## License

By contributing you agree that your contributions will be licensed under the MIT License.
