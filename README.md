© Ihor Mirzov, August 2019  
Distributed under GNU General Public License v3.0

<br/><br/>



# Salome universal to Calculix converter (unv to inp)

Converts [Salome](https://www.salome-platform.org/) .unv mesh to [CalculiX](http://dhondt.de/) .inp format.

This converter is based on Joël's Cugnoni UNV parser available with [CalculiX Launcher](http://www.calculixforwin.com/) distribution. I allowed myself to slightely improve it and translate into Python 3. INPWriter's methods are fully refactored and now allow to convert beams. See folder [tests-elements](./tests-elements) for list of tested UNV elements. All generated INP files are processed by [CalculiX CAE](https://github.com/imirzov/ccx_cae) without any errors.

<br/><br/>



# Download

Download Linux and Windows binaries from the [releases page](https://github.com/imirzov/unv2ccx/releases). Binaries don't need to be installed.

<br/><br/>



# How to use

Result INP-file name is the same as UNV-file name. So only one argument should be passed to the converter:

    in Linux:       ./unv2ccx file.unv
    in Windows:     ./unv2ccx.exe file.unv
    crossplatform:  python3 unv2ccx.py file.unv

For the last command you'll need [Python 3](https://www.python.org/downloads/) to be installed on your OS. The main script is *unv2ccx.py*, it depends on *UNVParser.py* and *INPWriter.py* - other files you won't need.

<br/><br/>



# Examples

UNV 115 element converted to C3D8:  
![UNV 115](./tests-elements/115.png "UNV 115")

UNV 118 element converted to C3D10:  
![UNV 118](./tests-elements/118.png "UNV 118")

<br/><br/>



# Your help

Please, you may:

- simply use this converter
- ask questions
- post issues here, on the GitHub
- attach your models and screenshots

<br/><br/>



# For developers

Create binary with [pyinstaller](https://www.pyinstaller.org/) (both in Linux and in Windows):

    pip3 install pyinstaller
    pyinstaller unv2ccx.py --onefile