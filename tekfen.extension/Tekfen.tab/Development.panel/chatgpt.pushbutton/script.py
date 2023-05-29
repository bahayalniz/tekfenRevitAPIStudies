# -*- coding: utf-8 -*-
__title__ = "ChatGPT"                           # Name of the button displayed in Revit UI
__doc__ = """ChatGPT kodlarını çalıştırmanızı sağlar"""              # Button Description shown in Revit UI
__author__ = "Baha YALNIZ" 

import clr
clr.AddReference('RevitAPI')
clr.AddReference('System')
import Autodesk
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Structure import StructuralType

import random

doc = __revit__.ActiveUIDocument.Document
active_view  = doc.ActiveView
active_level = doc.ActiveView.GenLevel

print(active_level)


t = Transaction(doc, "Create Cuboids")

t.Start() 

# Generate random points
# points = [XYZ(random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 10)) for i in range(3)]

# element = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_GenericModel).WhereElementIsElementType().FirstElement()

# print(element)

pt_start = XYZ(0,0,0)
pt_end   = XYZ(0,50,0)
Line.CreateBound(pt_start, pt_end)


# #CREATE A WALL
# wall = Wall.Create(doc, curve, active_level.Id, False)


# host_wall = doc.GetElement(ElementId(779500))
# pt_start = XYZ(30,0,0)
# pt_end   = XYZ(30,5,0)
# pt_mid   = (pt_start + pt_end) /2
# window_type = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Windows)\
#                     .WhereElementIsElementType().FirstElement()
    
# # CREATE A WINDOW
# window = doc.Create.NewFamilyInstance(pt_mid, window_type, host_wall, StructuralType.NonStructural )



# cuboid = doc.Create.NewFamilyInstance(points[0], element, Autodesk.Revit.DB.Structure.StructuralType.NonStructural)
    

# # Create cuboids
# for point in points:
#     p1 = point
#     p2 = XYZ(point.X + random.uniform(1, 5), point.Y + random.uniform(1, 5), point.Z + random.uniform(1, 5))
#     bbox = BoundingBoxXYZ()
#     bbox.Min = p1
#     bbox.Max = p2
#     print(bbox.Max)
    
#     cuboid = doc.Create.NewFamilyInstance(bbox, doc.GetElement(ElementId(BuiltInCategory.OST_GenericModel)), Autodesk.Revit.DB.Structure.StructuralType.NonStructural)
    
t.Commit()
