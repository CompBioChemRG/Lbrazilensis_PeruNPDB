import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# =========================
# 1. Load data
# =========================
df = pd.read_excel("data_be.xlsx")

col_compound = "Compound"
energy_cols = [c for c in df.columns if c != col_compound]

for c in energy_cols:
    df[c] = pd.to_numeric(df[c], errors="coerce")

df = df.replace([np.inf, -np.inf], np.nan)

df["Mean_DG"] = df[energy_cols].mean(axis=1, skipna=True)
df["SD_DG"] = df[energy_cols].std(axis=1, skipna=True)

df = df.dropna(subset=["Mean_DG", "SD_DG"])

# =========================
# 2. Reference
# =========================
reference = "DBO8185"

df["Compound_name"] = df[col_compound].astype(str).str.strip()
df_ref = df[df["Compound_name"] == reference]

ref_mean = df_ref["Mean_DG"].iloc[0]
ref_sd = df_ref["SD_DG"].iloc[0]

# Highlight compounds with ΔG < -9 kcal/mol
df["Highlighted"] = df["Mean_DG"] < -9
df["Reference"] = df["Compound_name"] == reference

df_high = df[(df["Highlighted"]) & (~df["Reference"])]
df_other = df[(~df["Highlighted"]) & (~df["Reference"])]

# =========================
# 3. KDE density
# =========================
x = df["Mean_DG"].values
y = df["SD_DG"].values

xy = np.vstack([x, y])
kde = gaussian_kde(xy)

xmin, xmax = x.min() - 0.3, x.max() + 0.3
ymin, ymax = 0, y.max() + 0.08

xx, yy = np.mgrid[xmin:xmax:250j, ymin:ymax:250j]
positions = np.vstack([xx.ravel(), yy.ravel()])
zz = np.reshape(kde(positions).T, xx.shape)

# =========================
# 4. Plot
# =========================
plt.figure(figsize=(10.5, 7.2))

# Density background
contour = plt.contourf(
    xx, yy, zz,
    levels=12,
    cmap="Greys",
    alpha=0.65
)

plt.contour(
    xx, yy, zz,
    levels=8,
    colors="gray",
    linewidths=0.6,
    alpha=0.8
)

cbar = plt.colorbar(contour)
cbar.set_label("Compound density", fontsize=12)

# Scatter points
plt.scatter(
    df_other["Mean_DG"],
    df_other["SD_DG"],
    s=45,
    color="#5DA5DA",
    alpha=0.9,
    label="< -9 kcal/mol"
)

plt.scatter(
    df_high["Mean_DG"],
    df_high["SD_DG"],
    s=45,
    color="#FF8C1A",
    alpha=0.9,
    label="≥ -9 kcal/mol"
)

# Reference point
plt.scatter(
    ref_mean,
    ref_sd,
    s=230,
    marker="*",
    color="limegreen",
    edgecolor="black",
    linewidth=1.2,
    label="DBO8185",
    zorder=5
)

# Vertical line (reference)
plt.axvline(
    ref_mean,
    color="black",
    linestyle="--",
    linewidth=1.5,
    alpha=0.75
)

## Optional threshold line
#plt.axvline(
#    -9,
#    color="red",
#    linestyle="--",
#    linewidth=1.3,
#    alpha=0.8,
#    label="Threshold = -9 kcal/mol"
#)

# Label top hits
top_hits = df_high.sort_values("Mean_DG").head(10)

for _, row in top_hits.iterrows():
    plt.text(
        row["Mean_DG"] + 0.05,
        row["SD_DG"] + 0.008,
        row["Compound_name"],
        fontsize=9
    )

# =========================
# 5. Formatting
# =========================
plt.title(
    "",
    fontsize=15
)

plt.xlabel("Mean binding free energy (kcal/mol)", fontsize=13)
plt.ylabel("SD (kcal/mol)", fontsize=13)

plt.xlim(-9.4, -2.7)
plt.ylim(0, 0.8)

plt.grid(alpha=0.25)
plt.legend(frameon=False, loc="upper right", fontsize=10)

plt.tight_layout()

plt.savefig("VS.png", dpi=600)
plt.savefig("VS.pdf")

plt.show()