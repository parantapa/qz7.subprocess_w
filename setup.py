from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="qz7.subprocess_w",
    description="Popen wrapper for graceful process termination",

    author="Parantapa Bhattacharya",
    author_email="pb+pypi@parantapa.net",

    long_description=long_description,
    long_description_content_type="text/markdown",

    packages=["qz7.subprocess_w"],

    use_scm_version=True,
    setup_requires=['setuptools_scm'],

    url="http://github.com/parantapa/qz7.subprocess_w",
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
