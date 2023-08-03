## What is SolidPython?
SolidPython is a tool for creating 3d CAD models using Python and OpenSCAD.  Creating 3D CAD models using Python can be simple, fast, and powerful.

## How does SolidPython work?
SolidPython works by using Python to generate an OpenSCAD model/script that can be viewed in OpenSCAD and exported from OpenSCAD to various formats for manufacturing or 3d printing.

SolidPython can also be used for OpenSCAD code generation for people already familiar with OpenSCAD who  want to generate complex OpenSCAD code snippers using a dynamic programming language.

## Installation
***Note: There is an older version of SolidPython, this document is for SolidPython2, which is the actively maintained fork.***

SolidPython can be installed using pip. To install the latest release:
```
pip install solidpython2
```

To view and export your models you may also want to [install OpenSCAD](https://openscad.org/downloads.html).

## Creating Your First Model
After you have installed SolidPython and OpenSCAD you can create your first 3D model using Python.  To start create a file named `cube.py`

```python
# import openscad
from solid2 import *

# construct a 3d model
model = cube(4)

# save your model for use in OpenSCAD
model.save_as_scad()
```

After you have created your `cube.py` file run your file to generate your 3D model.

```
python cube.py
```

This will generate an OpenSCAD model file named `cube.scad`.  Open this file in OpenSCAD and you can view the model you just created.

## Updating Your Model
Each time you modify your SolidPython model, just run `python cube.py` to update `cube.scad`.  If you leave OpenSCAD open, every time you execute your SolidPython code, the changes in your model should be automatically reflected in the OpenSCAD window.

When editing your SolidPython file it can be tedious to regenerate your SCAD model every time you make a change.  To make this easier you can use a tool like the Python [watchdog package](https://pypi.org/project/watchdog/) to automatically regenerate your SCAD file when you change your SolidPython script.

After installing the watchdog command line utility you can automatically regenerate your SCAD model with a command like:
```
watchmedo shell-command -c "python cube.py" cube.py
```

**Note: This command may differ slightly between different operating systems.**


## Creating More Complex Models
SolidPython supports most language OpenSCAD language features for generating complex CAD models.  Arithmetic operators can be used to add and subtract geometry.  Various transformations such as scaling, translating, mirroring etc can be chained together to create new geometry.  And various modifier functions are available to change the color, transparence, and debug geometry. The example below shows a few of the many features of OpenSCAD.  Many more detailed examples are available in the [SolidPython repository examples](https://github.com/jeff-dh/SolidPython/tree/master-2.0.0-beta-dev/solid2/examples) directory.

```python
# import openscad
from solid2 import *

# set the number of faces for curved shapes
set_global_fn(100)

# create enclosure base
base = cube(100, 50, 20)
hole = cube(90, 40, 20).translate(5, 5, 5)
base = base - hole

# create enclosure lid
lid = cube(100, 50, 5).translate(0, 0, 0)
label = text('box').translate(5, 5, 5)
lid = lid + label

# create reusable screw hole function
def screw_hole():
    head = cylinder(2, 2.5)
    body = cylinder(1, 10)
    return (head + body).mirror(0, 0, 1)

# cut out screw holes
offset = 3
lid -= screw_hole().translate(3, 3, 0.5)
lid -= screw_hole().translate(3, 47, 0.5)
lid -= screw_hole().translate(97, 3, 0.5)
lid -= screw_hole().translate(97, 47, 0.5)

base -= screw_hole().translate(3, 3, 23)
base -= screw_hole().translate(3, 47, 23)
base -= screw_hole().translate(97, 3, 23)
base -= screw_hole().translate(97, 47, 23)

# move lid into position
lid = lid.translate(0, 0, 20)

# make lid transparent
lid = lid.background()

# create model
model = base + lid

# save your model for use in OpenSCAD
model.save_as_scad()

```

## Using SolidPython and OpenSCAD Extensions
SolidPython also has some build in support for OpenSCAD extensions and has its own extension system for creating reusable functionality. Most notably many of the features in the [OpenSCAD BOSL2 library](https://github.com/BelfrySCAD/BOSL2/wiki) are also supported in SolidPython. BOSL2 includes the ability to attach objects, create gears, screws, and much more.  See [SolidPython repository](https://github.com/jeff-dh/SolidPython/tree/master-2.0.0-beta-dev/solid2/examples) for examples on how to use the BOSL2 extension.

## Further Reading
For more information, please checkout:

* [SolidPython README](https://github.com/jeff-dh/SolidPython)
* [Detailed examples in the SolidPython repository](https://github.com/jeff-dh/SolidPython/tree/master-2.0.0-beta-dev/solid2/examples)
* [OpenSCAD cheat sheet](https://openscad.org/cheatsheet/)
* [OpenSCAD documentation](https://openscad.org/documentation.html)
* [OpenSCAD BOSL2 library wiki](https://github.com/BelfrySCAD/BOSL2/wiki)
