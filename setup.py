from setuptools import setup, find_packages

VERSION = "0.0.22"
DESCRIPTION = "gpuv"
LONG_DESCRIPTION = "gpuv longer description"

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="gpuv",
    version=VERSION,
    author="Jared Wilber, Jojo Ortiz",
    author_email="jared@cambioml.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'
    keywords=["python", "gpu", "nvidia", "gpustat", "dashboard", "gpuv"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
