# Molecular Dynamics Simulations of *Leishmania braziliensis* Protein Complexes

## Overview

This repository contains the molecular dynamics (MD) simulation files, analysis workflows, and custom scripts used in the study:

**From Proteome-Wide Target Prioritization to Natural Product Discovery: A Multiscale Computational Study of Leishmania braziliensis***

The repository provides the complete MD simulation setup and analysis procedures for the apo protein and two selected ligand-bound complexes identified through virtual screening and binding free-energy evaluation.

---

## Repository Structure

```text
Lbrazilensis_PeruNPDB/
│
├── MD_Protein/
│   ├── charmm27-David.ff/
│   ├── run
│   ├── run2
│   ├── minim.mdp
│   ├── ions.mdp
│   ├── nvt.mdp
│   ├── npt.mdp
│   └── md.mdp
│
├── MD_Protein-DBO8185/
│   ├── charmm27-David.ff/
│   ├── run
│   ├── run2
│   ├── minim.mdp
│   ├── ions.mdp
│   ├── nvt.mdp
│   ├── npt.mdp
│   └── md.mdp
│
├── MD_Protein-PeruNPDB_061/
│   ├── charmm27-David.ff/
│   ├── run
│   ├── run2
│   ├── minim.mdp
│   ├── ions.mdp
│   ├── nvt.mdp
│   ├── npt.mdp
│   └── md.mdp
│
└── Analysis_script/
    ├── VS.py
    ├── rmsd.py
    ├── rg.py
    ├── rmsf.py
    └── sasa.py
```

---

## Simulated Systems

Three independent systems were investigated:

| System                  | Description                         |
| ----------------------- | ----------------------------------- |
| MD_Protein              | Apo protein                         |
| MD_Protein-DBO8185      | Protein complexed with DBO8185      |
| MD_Protein-PeruNPDB_061 | Protein complexed with PeruNPDB_061 |

---

## Molecular Dynamics Protocol

Molecular dynamics simulations were performed using:

* GROMACS v2023
* Explicit solvent model
* Periodic boundary conditions
* Particle Mesh Ewald (PME) electrostatics
* LINCS bond constraints
* NVT equilibration
* NPT equilibration
* Production molecular dynamics simulations

Detailed simulation parameters are provided within each system directory.

---

## Analysis

The repository includes scripts used to calculate:

* Root Mean Square Deviation (RMSD)
* Root Mean Square Fluctuation (RMSF)
* Radius of Gyration (Rg)
* Solvent Accessible Surface Area (SASA)

All analysis scripts are located in:

```text
Analysis_script/
```

---

## Software Requirements

* GROMACS 2023 or newer
* Python ≥ 3.10
* NumPy
* Pandas
* Matplotlib
* gmx_MMPBSA

---

## Data Availability

The complete reference proteome of *Leishmania braziliensis*, protein–protein interaction datasets, structural models, and natural-product libraries employed in the associated study were obtained from publicly available resources, including UniProt, STRING, PeruNPDB, PubChem, AlphaFold Server, Robetta, and I-TASSER.

This repository specifically contains:

* Molecular dynamics input files
* Simulation protocols
* Analysis scripts
* Post-processing workflows

Additional supporting data, including docking results, refined protein structures, molecular dynamics trajectories, and MM/GBSA output files, are available from the corresponding author upon reasonable request.

---

## Citation

If you use the workflows, scripts, or simulation protocols contained in this repository, please cite:

Barazorda-Ccahuana HL et al.

*From Proteome-Wide Target Prioritization to Natural Product Discovery: A Multiscale Computational Study of Leishmania braziliensis*

---

## Corresponding Author

**Haruna Luz Barazorda-Ccahuana, PhD**

Computational Biology and Chemistry Research Group
Universidad Católica de Santa María (UCSM)
Arequipa, Peru

Email: [hbarazorda@ucsm.edu.pe](mailto:hbarazorda@ucsm.edu.pe)

---

## License

This repository is intended for academic and non-commercial research purposes.
