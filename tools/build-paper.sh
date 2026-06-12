#!/usr/bin/env bash
# Build a SIGBOVIK-style two-column PDF from WHITEPAPER.md.
# Requires: pandoc, pdflatex (texlive).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$REPO_ROOT/WHITEPAPER.md"
OUT_DIR="$REPO_ROOT/paper"
OUT_PDF="$OUT_DIR/prompt-distance.pdf"
TMP_MD="$(mktemp --suffix=.md)"
trap 'rm -f "$TMP_MD"' EXIT

mkdir -p "$OUT_DIR"

# Preprocess:
# - drop the H1 title and the version/date lines (pandoc metadata supplies them)
# - GitHub math needs braces escaped as \\{ ; real LaTeX wants \{
sed -e '1,/^---$/d' \
    -e 's/\\\\{/\\{/g' \
    -e 's/\\\\}/\\}/g' \
    "$SRC" > "$TMP_MD"

BUILD_DIR="$(mktemp -d)"
trap 'rm -f "$TMP_MD"; rm -rf "$BUILD_DIR"' EXIT

# implicit_figures off: captions are written manually so GitHub shows them too
pandoc "$TMP_MD" \
  -f markdown-implicit_figures \
  --resource-path="$REPO_ROOT" \
  -s -o "$BUILD_DIR/paper.tex" \
  -M title="Prompt Distance: A Unified Metric for Software Triviality in the Post-Generative Era" \
  -M author="thereisnotime" \
  -M date="Draft v0.1 — prepared for submission to SIGBOVIK 2027" \
  -V documentclass=article \
  -V classoption=twocolumn \
  -V fontsize=10pt \
  -V geometry:margin=0.75in \
  -V linkcolor=blue \
  -V header-includes='\usepackage{microtype}\usepackage{dblfloatfix}\usepackage{titlesec}\titleformat*{\section}{\large\bfseries}\titleformat*{\subsection}{\normalsize\bfseries}'

# longtable can't run in two-column mode; convert to full-width table*.
# pdflatex also can't take these Unicode chars raw; swap for math macros.
perl -0pi -e '
  s/∞/\\(\\infty\\)/g;
  s/≅/\\(\\cong\\)/g;
  s/≤/\\(\\le\\)/g;
  s/≥/\\(\\ge\\)/g;
  s/ε/\\(\\varepsilon\\)/g;
  s/\\begin\{longtable\}\[\]/\\begin{table*}[!tb]\n\\centering\n\\begin{tabular}/g;
  s/\\columnwidth/\\textwidth/g;
  s/\\end\{longtable\}/\\bottomrule\n\\end{tabular}\n\\end{table*}/g;
  s/\\bottomrule\\noalign\{\}\n\\endlastfoot\n//g;
  s/\\end(first)?head\n//g;
' "$BUILD_DIR/paper.tex"

cp -r "$REPO_ROOT/figures" "$BUILD_DIR/"
(cd "$BUILD_DIR" && pdflatex -interaction=nonstopmode paper.tex >/dev/null && pdflatex -interaction=nonstopmode paper.tex >/dev/null)
cp "$BUILD_DIR/paper.pdf" "$OUT_PDF"

echo "Built: $OUT_PDF"
