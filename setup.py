import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="csv2gpx-schneuwlym",
    version="0.0.1",
    author="Mathias Schneuwly",
    author_email="mathias@schneuwlys.ch",
    description="This is a small script to convert tracks from a csv into a gpx file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/schneuwlym/csv2gpx",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
