from setuptools import setup, find_packages
from .My_Preprocess1.my_pipeline import MyPipeline

setup(
    name="myml",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas"
    ],
    author="Varsha",
    description="Custom ML preprocessing library from scratch",
)