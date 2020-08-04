
from setuptools import find_packages, setup

setup(
    name="jax_low_n_protein_engineering",
    version="0.1",
    packages=["jax_low_n_protein_engineering"],
    package_data={"low-n-protein-engineering": ["low_n_tutorial_files"],},
    install_requires=[
        "jax",
        "jaxlib",
        "numpy",
        "optuna",
        "scikit-learn",
        "tqdm",
        "jax_unirep",
        "biopython",
        "seaborn"
    ],
    include_package_data=True,
)