#!/usr/bin/env python3
"""Generate the GitHub social preview card (1280x640)."""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REPO_ROOT, ".github", "social-preview.png")

fig = plt.figure(figsize=(12.8, 6.4), dpi=100)
fig.patch.set_facecolor("#faf8f5")
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 1280)
ax.set_ylim(0, 640)
ax.axis("off")

ax.text(640, 480, "Prompt Distance", ha="center", fontsize=52,
        family="serif", weight="bold", color="#1a1a1a")
ax.text(640, 418, "A Unified Metric for Software Triviality in the Post-Generative Era",
        ha="center", fontsize=17, family="serif", style="italic", color="#444444")

ax.text(640, 330,
        r"$PD(x) = \min\,\{\, |P| \,:\, \mathrm{eval}(M,\, P) \cong x \,\}$",
        ha="center", fontsize=26, color="#1a1a1a")

ax.text(640, 250, "How many prompts is your product from not existing?",
        ha="center", fontsize=20, family="serif", color="#1a1a1a")

classes = [
    ("PD-0", "#888888"), ("PD-1", "#c0392b"), ("PD-2..9", "#d35400"),
    ("PD-10..99", "#b7950b"), ("PD-100+", "#1e8449"), ("PD-∞", "#555555"),
]
total_w, box_w, gap = 1280, 150, 14
start = (total_w - (box_w * len(classes) + gap * (len(classes) - 1))) / 2
for i, (label, color) in enumerate(classes):
    x = start + i * (box_w + gap)
    ax.add_patch(plt.Rectangle((x, 130), box_w, 50, facecolor=color,
                               edgecolor="none", alpha=0.9))
    ax.text(x + box_w / 2, 155, label, ha="center", va="center",
            fontsize=15, family="serif", weight="bold", color="white")

ax.text(640, 80, "thereisnotime/prompt-distance   ·   peer review acceptance rate: 0%",
        ha="center", fontsize=14, family="serif", color="#666666")

fig.savefig(OUT, facecolor=fig.get_facecolor())
print(f"Written: {OUT}")
