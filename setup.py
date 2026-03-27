from setuptools import setup, find_packages
# from .My_Preprocess1.my_pipeline import MyPipeline

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="varsha-preprocess",
    version="0.1.2",   
    packages=find_packages(),
    install_requires=["numpy", "pandas"],

    description="Custom preprocessing pipeline library",

    #  key part for readme
    long_description=long_description,
    long_description_content_type="text/markdown",
)