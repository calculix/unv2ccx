© Ihor Mirzov, August 2019 
Distributed under GNU General Public License v3.0

<br/><br/>



# Universal to Calculix converter (unv to inp)

Converts [Universal](http://sdrl.uc.edu/sdrl/referenceinfo/universalfileformats/file-format-storehouse/universal-file-datasets-summary) (.unv) file from [Salome](https://www.salome-platform.org/) to [CalculiX](http://dhondt.de/) .inp mesh: reads UNV_file,
creates an internal FEM object, then writes the INP_file.

This converter is based on Joël's Cugnoni UNV parser written in 2007 and available with [CalculiX Launcher](http://www.calculixforwin.com/) distribution. I allowed myself to slightely improve it and translate into Python 3. INPWriter's methods are fully refactored and now allow to convert beams.

See folder [tests-elements](./tests-elements) for list of tested elements. All generated INP files are processed by [CalculiX CAE](https://github.com/imirzov/ccx_cae) without any errors.

<br/><br/>



# How to use

You'll need [Python 3](https://www.python.org/downloads/).

The main script is [unv2ccx.py](unv2ccx.py), it depends on:
- [UNVParser.py](UNVParser.py)
- [INPWriter.py](INPWriter.py)

Usage is simple:

    python3 unv2ccx.py UNV_file INP_file

<br/><br/>



# Your help

Please, you may:

- simply use this converter
- ask questions
- post issues here, on the GitHub
- attach your models and screenshots
