import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CensusJSON-bdjohnson529", # Replace with your own username
    version="0.0.1",
    author="Ben Johnson",
    description="JSON file generator for US Census data",
    url="https://github.com/bdjohnson529/CensusJSON",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires =	['pandas>=1.0.1',
						'numpy>=1.18.1',
						'kml2geojson>=4.0.2'
	]
)