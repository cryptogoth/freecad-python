import os
# homedir = os.getenv('HOME')
homedir = os.getcwd()

basedir = homedir # os.path.join(homedir, "Documents", "Open Source Ecology")
filename = "Seh2_wall_24.FCStd"
filepath = os.path.join(basedir, filename)

import sys
sys.path.append('/c/Program\ Files/FreeCAD\ 0.19/lib/')

# import App
# import Gui
import Part
import Sketcher
newDoc = FreeCAD.newDocument(filename)

#FreeCAD.openDocument(filepath)

newDoc.addObject('Sketcher::SketchObject', 'Sketch003')

newDoc.Sketch003.Placement = App.Placement(App.Vector(0.000000, 0.000000, 0.000000), App.Rotation(0.000000, 0.000000, 0.000000, 1.000000))
#newDoc.Sketch003.MapMode = "Deactivated"

# Define a sketch to create a Pad
sketch_name = 'Sketch003'
active_sketch = newDoc.getObject(sketch_name)

geoList = []
geoList.append(Part.LineSegment(App.Vector(0.000000,0.000000,0),App.Vector(2.241769,0.000000,0)))
geoList.append(Part.LineSegment(App.Vector(2.241769,0.000000,0),App.Vector(2.241769,1.301982,0)))
geoList.append(Part.LineSegment(App.Vector(2.241769,1.301982,0),App.Vector(0.000000,1.301982,0)))
geoList.append(Part.LineSegment(App.Vector(0.000000,1.301982,0),App.Vector(0.000000,0.000000,0)))
active_sketch.addGeometry(geoList,False)
conList = []
conList.append(Sketcher.Constraint('Coincident',0,2,1,1)) # Constraint 0
conList.append(Sketcher.Constraint('Coincident',1,2,2,1)) # Constraint 1
conList.append(Sketcher.Constraint('Coincident',2,2,3,1)) # Constraint 2
conList.append(Sketcher.Constraint('Coincident',3,2,0,1)) # Constraint 3
conList.append(Sketcher.Constraint('Horizontal',0)) # Constraint 4
conList.append(Sketcher.Constraint('Horizontal',2)) # Constraint 5
conList.append(Sketcher.Constraint('Vertical',1)) # Constraint 6
conList.append(Sketcher.Constraint('Vertical',3)) # Constraint 7
active_sketch.addConstraint(conList)
active_sketch.addConstraint(Sketcher.Constraint('Coincident',0,1,-1,1)) # Constraint 8 
active_sketch.addConstraint(Sketcher.Constraint('DistanceY',0,1,2,2,10)) # Constraint 9

newDoc.addObject('PartDesign::Body','Body')
newDoc.Body.Group = [newDoc.getObject(sketch_name)]

newBody = newDoc.getObject('Body')
newBody.Visibility = True
newPad = newBody.newObject('PartDesign::Pad','Pad')
newPad.Profile = newDoc.getObject(sketch_name)
newPad.Length = 10.007600
newPad.Length2 = 99.999800
newPad.UseCustomVector = 0
newPad.Visibility = True
newPad.Direction = (1, 1, 1)
newPad.Type = 0
newPad.UpToFace = None
newPad.Reversed = 0
newPad.Midplane = 0
newPad.Offset = 0
newDoc.getObject(sketch_name).Visibility = True

newDoc.getObject('Body').Visibility = True
newDoc.getObject('Pad').Visibility = True

newDoc.recompute()
newDoc.saveAs(filepath)

# tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
# ActiveSketch.ViewObject.TempoVis = tv
# if ActiveSketch.ViewObject.EditingWorkbench:
#   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
# if ActiveSketch.ViewObject.HideDependent:
#   tv.hide(tv.get_all_dependent(App.getDocument(filename).getObject('Sketch003'), ''))
# if ActiveSketch.ViewObject.ShowSupport:
#   tv.show([ref[0] for ref in ActiveSketch.Support if not ref[0].isDerivedFrom("PartDesign::Plane")])
# if ActiveSketch.ViewObject.ShowLinks:
#   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
# tv.hide(ActiveSketch)
# del(tv)

# ActiveSketch = App.getDocument(filename).getObject('Sketch003')
# if ActiveSketch.ViewObject.RestoreCamera:
#   ActiveSketch.ViewObject.TempoVis.saveCamera()

### End command Sketcher_NewSketch
