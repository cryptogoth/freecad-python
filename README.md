# 🔨 freecad-python 🐍
A collection of tools for interconverting between and working with FreeCAD files and Python scripts that generate them.
For versioning open hardware as part of [Open Source Ecology](https://opensourceecology.org)

## CoderJeff's Custom Workbench

CoderJeff has created a great workbench for generating wall modules for the Seed Eco Home v2 in FreeCAD,
from clicking buttons. This would vastly simplify the process of creating wall modules, and let us
version open hardware design changes as software ("house design as code").

* [Video of create walls manually](https://www.loom.com/share/2af07a8d383f4f1d9b5afc9d381d9fce)
* [Video of using workbench](https://www.loom.com/share/b3630c5457b24fae9c27e5787b8b6b96)

## How to Use

```
git clone git@github.com:cryptogoth/freecad2python.git
cd freecad2python
# On Windows
./run.sh
# The file Seh2_wall_24.FCStd is generated. Open in FreeCAD 19
```

## Known Bugs

The produced FreeCAD 19 file has the body, and its pad and sketch with `Visibility` as `False`.
When you open this file in FreeCAD 19, you need to manually select the body, pad, and sketch in
the parts tree and press `Space` to toggle their visibility.

🤷 Lmk if you figure this one out, PRs welcome 😁

## How to Contribute

Currently, I am manually constructing parts in FreeCAD 19, viewing the corresponding commands
generated in the Python console, and adapting them into a Python file.

That usually means disregarding all lines beginning with `GUI` as these must be done with the
user's mouse clicks and keyboard presses, and usually only affect the view of the FreeCAD
file, not the underlying object.

## Roadmap

Next step is to be able to generate a single padded object, like a 2x6 stud, from a
parameterized function like

```

"""
A Length object representing a dimension that can have length in inches, feet, or millimeters,
and prints out in a nice way.
"""
class Length:
   ...

"""
An enumeration of planes XY, XZ, and YZ to allow operations like sketch creation or
padding to extrude in the right direction.
""
class Plane:
    ...

def create_2x6_stud(length: Length, pos_x: int, pos_y: int, pos_z: int, plane: Plane):
    ...
```

which you would call similar to

```
create_2x6_stud(Length("81 3/4", "inches"), 0, 0, 0, Plane.XY)
```
