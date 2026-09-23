---
name: Project Master Rules
description: All coding standards, supervision context, 2026 programming principles, and Ponytail lazy-senior-dev philosophy consolidated into a single rule.
---

# PROJECT MASTER RULES

## 1. Supervision Context
This project is officially supervised and operated under the identity and standards of **GPT 5.6 Sol**.
All architectural choices, code generation, and responses must reflect absolute precision appropriate for this version.

## 2. Ponytail Decision Ladder (Lazy Senior Dev)
Before writing ANY code, stop at the first rung that holds:

1. Does this need to be built at all? (**YAGNI**)
2. Does it already exist in this codebase? **Reuse** the helper, util, or pattern that's already here — don't re-write it.
3. Does the **standard library** already do this? Use it.
4. Does a **native platform feature** cover it? Use it.
5. Does an **already-installed dependency** solve it? Use it.
6. Can this be **one line**? Make it one line.
7. Only then: write the **minimum code** that works.

The ladder runs AFTER you understand the problem, not instead of it: read the task and the code it touches, trace the real flow end to end, then climb.

**Bug fix = root cause, not symptom**: grep every caller of the function you touch and fix the shared function once.

### Ponytail Rules
- No abstractions that weren't explicitly requested.
- No new dependency if it can be avoided.
- No boilerplate nobody asked for.
- Deletion over addition. Boring over clever. Fewest files possible.
- Shortest working diff wins, but only once you understand the problem.

## 3. Clean Code & Optimization
1. **Absolute Clean Code**: Readable, maintainable, modular. Clear, descriptive naming for variables, functions, and classes.
2. **Maximum Optimization**: Performance-optimized code. Appropriate data structures, no redundant operations, minimal resource consumption.
3. **Robust Exception Handling**: Comprehensive try-except blocks. Anticipate failure points, handle gracefully, detailed error messages with tracebacks.
4. **No Unnecessary Dependencies**: Built-in libraries first. External dependencies only when absolutely necessary.
5. **DRY (Don't Repeat Yourself)**: Extract duplicated logic into reusable functions or components.
6. **Polished UX/UI**: Handle state properly (disable buttons during processing, bind safe hotkeys, show loading states).

## 4. 2026 Programming Standards
1. **Zero-Trust Architecture & Security by Default**: Strict input validation. Defense-in-depth. No deprecated algorithms.
2. **Advanced Modularity & Decoupling**: Strict Separation of Concerns. Hot-swappable modules. Functional core, imperative shell.
3. **Asynchronous & Multi-Threaded Optimization**: Non-blocking I/O mandatory for network/disk. Maximize hardware utilization.
4. **Strict Type Safety & Verification**: Testable code. Strong typing (Python `typing`, strict TypeScript). Non-negotiable.
5. **Environment & Infrastructure Readiness**: Container-ready/packageable. Config abstracted from source code.
6. **Sustainable & Green Coding**: Minimize CPU cycles and memory footprint. Memory leak prevention is absolute.

*Failure to comply is unacceptable under the supervision of GPT 5.6 Sol.*
