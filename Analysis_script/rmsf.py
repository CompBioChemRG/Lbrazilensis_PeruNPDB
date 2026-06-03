import pandas as pd
import matplotlib.pyplot as plt

files = {
    "DBO8185": "rmsf_drug_X.xvg",
    "PERUNPDB_061": "rmsf_p61_X.xvg",
    "WT": "rmsf_protein_X.xvg"
}

colors = {
    "DBO8185": "#55A868",
    "PERUNPDB_061": "#DD8452",
    "WT": "gray"
}

def read_xvg(filepath):
    data = []
    with open(filepath, "r") as f:
        for line in f:
            if line.startswith(("#", "@")) or line.strip() == "":
                continue
            parts = line.split()
            if len(parts) >= 2:
                data.append([float(parts[0]), float(parts[1])])
    return pd.DataFrame(data, columns=["Residue", "RMSF"])

dfs = {name: read_xvg(path) for name, path in files.items()}

plt.figure(figsize=(9, 5.5))

# Domain 309–441
plt.axvspan(
    309, 441,
    color="gray",
    alpha=0.18,
    label=""
)

# RMSF curves
for name, df in dfs.items():
    plt.plot(
        df["Residue"],
        df["RMSF"],
        linewidth=1.8,
        label=name,
        color=colors[name]
    )

# Highlighted residues
highlight_residues = {
    "Phe237": 237,
    "Gln424": 424
}

for residue_name, residue_pos in highlight_residues.items():
    plt.axvline(
        residue_pos,
        color="red",
        linestyle="--",
        linewidth=1.4,
        alpha=0.9
    )
    plt.text(
        residue_pos + 3,
        plt.ylim()[1] * 0.92,
        residue_name,
        rotation=90,
        color="red",
        fontsize=11,
        va="top"
    )

# Axis limits (adjust according to your data)
plt.xlim(1, 442)
plt.ylim(0, 1.5)

plt.xlabel("Residue", fontsize=18)
plt.ylabel("RMSF (nm)", fontsize=18)
plt.legend(frameon=False, fontsize=10, loc="upper left")
plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig("rmsf.png", dpi=300, bbox_inches="tight")

plt.show()