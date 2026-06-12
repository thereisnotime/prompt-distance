# Prompt Distance (PD)

A whitepaper proposing **Prompt Distance**: the minimum number of prompts required to reproduce a software artifact from an empty directory using a frontier LLM.

In short: a way to say "this product is one prompt away from not existing" with a citation.

> "How defensible is the product?"
> "Two prompts."
> *(overheard at a board meeting, 2026)*

Read the full paper: [WHITEPAPER.md](WHITEPAPER.md), or as a two-column PDF: [paper/prompt-distance.pdf](paper/prompt-distance.pdf) (prepared for SIGBOVIK 2027; build it yourself with `tools/build-paper.sh`, requires pandoc + texlive)

## TL;DR

$$PD(x) = \min \\{ |P| : \mathrm{eval}(M, P) \cong x \\}$$

| Class | Meaning | Example |
|-------|---------|---------|
| PD-0 | Already exists as a library or Unix utility. No project was needed. | rsync with a landing page; `cron` as a service, $9/mo |
| PD-1 | One-shottable. The project is its own README. | AI summarizer for {meetings, emails, PDFs}; ChatGPT with your logo and a waitlist |
| PD-2..9 | A short conversation. Usually one real design decision. | CRUD dashboard with dark mode; the fourth Trello clone this quarter; "Uber for X" where X didn't ask |
| PD-10..99 | Actual software. | your product, allegedly; the billing system everyone is afraid of |
| PD-100+ | Compilers, kernels, anything touching timezones. | Postgres; anything that parses dates and apologizes for it |
| PD-∞ | The hard part is not code. See: the Dave Boundary. | the reverse proxy nobody dares restart; whatever Dave maintains |

Scores decay as models improve (**prompt rot**), so they must be dated:
`PD(x) = 3 (claude-fable-5, 2026-06)`.

## Usage

When reviewing a product, estimate its PD, date it, and disclose the transcript. Undated or transcript-free claims of "I one-shotted it" are inadmissible and shall be treated as Weekend Conjectures.

Low PD means the software is trivial. It does not mean the business is. Those are different papers.

## Peer Review

This paper is under continuous open review. To submit a formal review, [open a peer review issue](https://github.com/thereisnotime/prompt-distance/issues/new?template=peer-review.yml) using the structured form. Every submission receives an individual decision from the Program Committee, typically within one minute, which we consider a feature of the venue.

The acceptance rate to date is 0%. The committee is aware and considers this evidence of rigor.
