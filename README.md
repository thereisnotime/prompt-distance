# Prompt Distance (PD)

A whitepaper proposing **Prompt Distance**: the minimum number of prompts required to reproduce a software artifact from an empty directory using a frontier LLM.

In short: a way to say "this product is one prompt away from not existing" with a citation.

Read the full paper: [WHITEPAPER.md](WHITEPAPER.md)

## TL;DR

```
PD(x) = min { |P| : eval(M, P) ≅ x }
```

| Class | Meaning |
|-------|---------|
| PD-0 | Already exists as a library or Unix utility. No project was needed. |
| PD-1 | One-shottable. The project is its own README. |
| PD-2..9 | A short conversation. Usually one real design decision. |
| PD-10..99 | Actual software. |
| PD-100+ | Compilers, kernels, anything touching timezones. |
| PD-∞ | The hard part is not code. See: the Dave Boundary. |

Scores decay as models improve (**prompt rot**), so they must be dated:
`PD(x) = 3 (claude-fable-5, 2026-06)`.

## Usage

When reviewing a product, estimate its PD, date it, and disclose the transcript. Undated or transcript-free claims of "I one-shotted it" are inadmissible and shall be treated as Weekend Conjectures.

Low PD means the software is trivial. It does not mean the business is. Those are different papers.
