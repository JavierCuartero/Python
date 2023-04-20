# Installation

You''ll find the information here: https://blenderbim.org/docs-python/ifcopenshell-python/installation.html


There are different methods of installation, depending on your situation.

* Pre-built packages is recommended for users wanting to use the latest IfcOpenShell builds.
* PyPI is recommended for developers using Pip.
* Conda is recommended for developers using Anaconda.
* Docker is recommended for developers using Docker.
* Using the BlenderBIM Add-on is recommended for non-developers wanting a graphical interface.
* From source with precompiled binaries is recommended for developers actively working with the Python code.
* Compiling from source is recommended for developers actively working with the C++ core.

## Pre-built packages
Pre-built packages are prepared sporadically depending on whether there are changes in the IfcOpenShell C++ core.

1. Choose which version to download based on your operating system, Python version, and computer architecture.
2. Unzip the downloaded file and copy the ifcopenshell directory into your Python path. If you’re not sure where your Python path is, run the following code in Python:
```
import sys
print(sys.path)
```
This will give you a list of possible directories that you can install the IfcOpenShell module into. Most commonly, you will want to copy the ifcopenshell directory into one of these called site-packages.

3. Test importing the module in a Python session or script to make sure it works.
```
import ifcopenshell
print(ifcopenshell.version)
model = ifcopenshell.file()
```
