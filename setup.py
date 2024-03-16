"""
https://packaging.python.org/tutorials/packaging-projects/
"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="IDNlatestEarthquake",
    version="0.1",
    author="Farrel Zandra",
    author_email="arel.zandra@gmail.com",
    description="This package will help you to get the latest earthquake data from Indonesian BMKG "
                "(Meteorological, Climatological, and Geophysical Agency).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/quack22/indonesianLatestEarthquake",
    project_urls={
        "Portofolio Website": "https://quack22.github.io/quack22.github.io-main/",
    },
    classifiers={
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)e",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable"
    },
    # package_dir={"": "src"},
    # packages=setuptools.find_packages(where="src"),
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)