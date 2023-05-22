# -*- coding: utf-8 -*-
__title__ = "ChatGPT"                           # Name of the button displayed in Revit UI
__doc__ = """ChatGPT kodlarını çalıştırmanızı sağlar"""              # Button Description shown in Revit UI
__author__ = "Baha YALNIZ" 

import clr
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *

import random

doc = __revit__.ActiveUIDocument.Document
transaction = Transaction(doc, "Create Cuboids")

transaction.Start()

# Generate random points
points = [XYZ(random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 10)) for i in range(3)]

cuboid = doc.ItemFactoryBase.NewFamilyInstance(points[0], doc.GetElement(ElementId(BuiltInCategory.OST_GenericModel)), Autodesk.Revit.DB.Structure.StructuralType.NonStructural)
    

# Create cuboids
# for point in points:
#     p1 = point
#     p2 = XYZ(point.X + random.uniform(1, 5), point.Y + random.uniform(1, 5), point.Z + random.uniform(1, 5))
#     bbox = BoundingBoxXYZ()
#     bbox.Min = p1
#     bbox.Max = p2
#     print(bbox.Max)
    
#     cuboid = doc.Create.NewFamilyInstance(bbox, doc.GetElement(ElementId(BuiltInCategory.OST_GenericModel)), Autodesk.Revit.DB.Structure.StructuralType.NonStructural)
    
transaction.Commit()
