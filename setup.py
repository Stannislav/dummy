from setuptools import find_packages, setup


setup(
    name="dummy",
    version="0.0.1",
    package_dir={"": "src"},
    packages=find_packages("src"),
)
