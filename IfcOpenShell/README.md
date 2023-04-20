# Install
1. Go to https://github.com/IfcOpenShell/IfcOpenShell/releases
2. Donwload the lastest release for your system and python version (win and py310)
3. Unzip the downloaded file and navigate to 
```
blenderbim\libs\site\packages
```
4. Copy the contents of this directory into your Python path. If you’re not sure where your Python path is, run the following code in Python:
```
import sys
print(sys.path)
```
This will give you a list of possible directories that you can install the IfcOpenShell module into. Most commonly, you will want to copy the ifcopenshell directory into one of these called site-packages.

5. Test importing the module in a Python session or script to make sure it works.
```
import ifcopenshell
print(ifcopenshell.version)
model = ifcopenshell.file()
```
