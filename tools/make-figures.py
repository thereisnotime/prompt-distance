#!/usr/bin/env python3
"""Generate the whitepaper figures into figures/."""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REPO_ROOT, "figures")
os.makedirs(OUT, exist_ok=True)

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 9,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 150,
})
GRAY = "#444444"


def fig_prompt_rot():
    years = [2020, 2021, 2022, 2023, 2024, 2025, 2026]
    pd_scores = [220, 90, 60, 22, 8, 3, 1]
    valuation = [1.0, 1.1, 1.3, 1.6, 1.9, 2.0, 2.0]  # relative, lags reality

    fig, ax1 = plt.subplots(figsize=(4.6, 2.9))
    ax1.step(years, pd_scores, where="post", color="black", lw=1.5,
             label="PD of the same product")
    ax1.set_yscale("log")
    ax1.set_ylabel("Prompt Distance (pt, log)")
    ax1.set_xlabel("frontier model release year")
    ax1.axhline(1, color=GRAY, lw=0.6, ls=":")
    ax1.annotate("PD = 1: the product is its own README",
                 xy=(2020.1, 1.15), fontsize=7, color=GRAY)

    ax2 = ax1.twinx()
    ax2.plot(years, valuation, color=GRAY, lw=1.2, ls="--",
             label="reported valuation")
    ax2.set_ylabel("valuation (relative)", color=GRAY)
    ax2.tick_params(axis="y", colors=GRAY)
    ax2.spines["right"].set_visible(True)
    ax2.spines["right"].set_color(GRAY)
    ax2.spines["top"].set_visible(False)

    lines = ax1.get_lines()[:1] + ax2.get_lines()[:1]
    ax1.legend(lines, [l.get_label() for l in lines], fontsize=7,
               loc="center left", frameon=False)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "prompt-rot.png"))
    plt.close(fig)


def fig_triviality_plane():
    fig, ax = plt.subplots(figsize=(4.6, 3.4))
    ax.set_xscale("log")
    ax.set_xlim(0.7, 2000)
    ax.set_ylim(0, 10.4)
    ax.set_xlabel("Prompt Distance (pt, log)")
    ax.set_ylabel("revenue (log, allegedly)")
    ax.set_yticks([])
    ax.axvline(10, color=GRAY, lw=0.8, ls=":")
    ax.axhline(5, color=GRAY, lw=0.8, ls=":")

    quad = dict(fontsize=8, color=GRAY, style="italic", ha="center")
    ax.text(3, 9.9, "prompts with a Series A", **quad)
    ax.text(300, 9.9, "software businesses", **quad)
    ax.text(3, 0.4, "hobbies", **quad)
    ax.text(300, 0.4, "consulting", **quad)

    points = [
        (1, 6.4, "AI meeting summarizer (Case A)"),
        (1, 8.6, "Dropbox, per HN (2007);\nmeasurement disputed"),
        (2, 1.5, "weekend repo"),
        (6, 6.0, "internal dashboard (Case B)"),
        (400, 7.0, "compiler"),
        (1500, 2.5, "reverse proxy + Dave (Case C)"),
    ]
    for x, y, label in points:
        ax.plot(x, y, "o", color="black", ms=4)
        ax.annotate(label, xy=(x, y), xytext=(4, 4),
                    textcoords="offset points", fontsize=6.5)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "triviality-plane.png"))
    plt.close(fig)


def fig_dave_boundary():
    fig, ax = plt.subplots(figsize=(4.6, 1.9))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    ax.set_xticks([])
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_position(("data", 0.35))
    ax.annotate("", xy=(10, 0.35), xytext=(0, 0.35),
                arrowprops=dict(arrowstyle="->", color="black", lw=1))
    ax.set_xlabel("where the complexity lives", fontsize=8)
    ax.text(0.2, 0.22, "code", fontsize=8)
    ax.text(9.0, 0.22, "people", fontsize=8)

    ax.axvspan(7, 10, ymin=0.35, color="0.88")
    ax.axvline(7, ymin=0.30, ymax=0.95, color="black", ls="--", lw=1)
    ax.text(7.1, 0.92, "the Dave Boundary", fontsize=8, style="italic")
    ax.text(8.5, 0.6, "PD = $\\infty$\n(prompt-incomplete)",
            fontsize=7.5, ha="center", color=GRAY)

    marks = [(1.2, "CRUD app"), (3.4, "compiler"),
             (5.8, "9-year-old\nreverse proxy"), (8.6, "Dave")]
    for x, label in marks:
        ax.plot(x, 0.35, "o", color="black", ms=4, clip_on=False, zorder=5)
        ax.text(x, 0.44, label, fontsize=7, ha="center")
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "dave-boundary.png"))
    plt.close(fig)


if __name__ == "__main__":
    fig_prompt_rot()
    fig_triviality_plane()
    fig_dave_boundary()
    print(f"Figures written to {OUT}")
