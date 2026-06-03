import pandas as pd
import matplotlib.pyplot as plt

files = {
    "DBO8185": "sasa_drug_X.xvg",
    "PERUNPDB_061": "sasa_p61_X.xvg",
    "WT": "sasa_protein_X.xvg"
}

colors = {
    "DBO8185": "#55A868",
    "PERUNPDB_061": "#DD8452",
    "WT": "black"
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
    return pd.DataFrame(data, columns=["Time", "SASA"])

dfs = {name: read_xvg(path) for name, path in files.items()}

for name, df in dfs.items():
    if df["Time"].max() > 1000:
        df["Time_ns"] = df["Time"] / 1000
    else:
        df["Time_ns"] = df["Time"]

plt.figure(figsize=(9, 5.5))

for name, df in dfs.items():
    plt.plot(
        df["Time_ns"],
        df["SASA"],
        linewidth=1.8,
        label=name,
        color=colors[name]
    )

plt.xlabel("Time (ns)", fontsize=13)
plt.ylabel("SASA (nm$^2$)", fontsize=13)
plt.title("", fontsize=14)
plt.legend(frameon=False, fontsize=11)
plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig("SASA.png", dpi=300, bbox_inches="tight")
plt.show()