© Ihor Mirzov, 2019-2023  
Distributed under GNU General Public License v3.0

[![PyPi](https://badgen.net/badge/icon/pypi?icon=pypi&label)](https://pypi.org/project/unv2ccx)
[![PyPi downloads](https://img.shields.io/pypi/dm/unv2ccx.svg)](https://pypistats.org/packages/unv2ccx)  
[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/calculix/unv2ccx)
[![Github All Releases](https://img.shields.io/github/downloads/calculix/unv2ccx/total.svg)](https://github.com/calculix/unv2ccx/releases)

<br/><br/>



---

[Downloads](https://github.com/calculix/unv2ccx/releases) |
[How to use](#how-to-use) |
[Screenshots](#screenshots) |
[Your help](#your-help) |
[For developers](#for-developers) |
[TODO](#todo)

---

<br/><br/>



# Salome to CalculiX converter (unv to inp)

Converts [Salome](https://www.salome-platform.org/) .unv file to [CalculiX](http://dhondt.de/) .inp format.

This converter is based on Joël's Cugnoni UNV parser available with [CalculiX Launcher](http://www.calculixforwin.com/) distribution. I allowed myself to slightely improve it and translate into Python 3. INPWriter's methods are fully refactored and now allow to convert beams. See folder [examples](./examples) for list of tested UNV elements. All generated INP files are processed by CalculiX GraphiX and [CalculiX Adanced Environment](https://github.com/calculix/cae) without any errors.

Thanks to [Niclas Stenberg](https://github.com/Xnst) for fixing bug with empty sets.

<br/><br/>



# How to use

Download Linux and Windows binaries from the [releases page](https://github.com/calculix/unv2ccx/releases). Binaries don't need to be installed.

Result INP-file name is the same as UNV-file name. So only one argument should be passed to the converter:

    in Linux:       ./unv2ccx file.unv
    in Windows:     unv2ccx.exe file.unv

<br/><br/>



# Screenshots

1D and 2D UNV elements in Salome:  
![UNV 2D](./Compound_Mesh_2D_unv.png "UNV 2D")
Converted 1D and 2D elements in CalculiX GraphiX:  
![INP 2D](./Compound_Mesh_2D_inp.png "INP 2D")

3D UNV elements in Salome:  
![UNV 3D](./Compound_Mesh_3D_unv.png "UNV 3D")
Converted 3D elements in CalculiX GraphiX:  
![INP 3D](./Compound_Mesh_3D_inp.png "INP 3D")

<br/><br/>



# Your help

Please, you may:

- Star this project.
- Simply use this software and ask questions.
- Share your models and screenshots.
- Report problems by [posting issues](https://github.com/calculix/unv2ccx/issues).
- Or even [become a sponsor to me](https://github.com/sponsors/imirzov).

<br/><br/>



# For developers

[![PyPI pyversions](https://img.shields.io/pypi/pyversions/unv2ccx.svg)](https://www.python.org/downloads/)
[![Visual Studio Code](https://img.shields.io/badge/--007ACC?logo=visual%20studio%20code&logoColor=ffffff)](https://code.visualstudio.com/)

To run this converter from source you'll need [Python 3](https://www.python.org/downloads/).

Install *unv2ccx* package with command:

    pip3 install unv2ccx

In your code use unv2ccx package in this way:

    import unv2ccx
    c = unv2ccx.Converter(unv_file_name)
    c.run()

If you have Python version >= 3.8 create binary with [nuitka](https://nuitka.net/):

    pip3 install nuitka
    
    In Windows:
    set CC=C:\\MinGW64\\mingw64\\bin\\gcc.exe
    python3 -m nuitka --follow-imports --mingw64 __init__.py

    In Linux:
    python3 -m nuitka --follow-imports __init__.py

If you have Python version < 3.8 create binary with [pyinstaller](https://www.pyinstaller.org/):

    pip3 install pyinstaller
    pyinstaller __init__.py --onefile

Read [here](https://packaging.python.org/tutorials/packaging-projects/) about how to create packages for [pypi.org](https://pypi.org/):

    python3 -m pip install --user --upgrade setuptools wheel twine
    python3 setup.py sdist bdist_wheel
    twine upload dist/*

<br/><br/>



# TODO

- Multiprocessing for tests.
- Correctly convert UNV surface set into INP surface.
- Use pyuff module
- Support keyword *HEADING
- Support keyword *SURFACE
