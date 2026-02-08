from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="Topsis-Sarang-102353017",
    version="0.0.4",
    author="Sarang Priani",
    author_email="sarang.priani@gmail.com",
    description="Command line implementation of TOPSIS method",
    long_description=long_description,
    long_description_content_type="text/markdown",  
    packages=find_packages(),
    install_requires=["pandas", "numpy"],
    entry_points={
        "console_scripts": [
            "topsis=topsis.topsis:main"
        ]
    },
)
