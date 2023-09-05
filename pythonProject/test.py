#import subprocess
#subprocess.run(["git", "clone", "https://github.com/OptimalScale/LMFlow.git"])
cd LMFlow
conda create -n lmflow python=3.9 -y
conda activate lmflow
conda install mpi4py
pip install -e .
