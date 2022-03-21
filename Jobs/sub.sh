#!/bin/bash
#SBATCH -p paratera
#SBATCH -N 1
#SBATCH -n 24
module purge
module load intel/19.0.3-zyq
module load lammps/lammps_22Aug18
srun lmp_intel_cpu_intelmpi -in $1
