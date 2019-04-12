from pathlib import Path
from setuptools import setup

package_name = Path(".").absolute().name

with open("README.md", "r") as fh:
    long_description = fh.read()

    description = long_description.strip()
    description = description.split("\n")
    description = description[0]
    description = description.lstrip("#")
    description = description.strip()

setup(
    name=package_name,
    description=description,

    author="Parantapa Bhattacharya",
    author_email="pb+pypi@parantapa.net",

    long_description=long_description,
    long_description_content_type="text/markdown",

    packages=[package_name],

    use_scm_version=True,
    setup_requires=['setuptools_scm'],

    url="http://github.com/parantapa/%s" % package_name,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
