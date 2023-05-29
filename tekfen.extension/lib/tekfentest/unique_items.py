# -*- coding utf-8 -*-

# Regular + Autodesk
import os, sys, math, datetime, time                                    # Regular Imports
from Autodesk.Revit.DB import *                                         # Import everything from DB (Very good for beginners)


# pyRevit
from pyrevit import revit, forms                                        # import pyRevit modules. (Lots of useful features)

# Custom Imports

# .NET Imports
import clr                                  # Common Language Runtime. Makes .NET libraries accessinble
clr.AddReference("System")                  # Refference System.dll for import.

from System.Collections.Generic import List
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# Import RevitNodes
clr.AddReference("RevitNodes")

import Revit

# Import Revit elements
from Revit.Elements import *

# Import DocumentManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

import System

# Lists the unique items in a list

def unique_items(lst):
    unique_items = List[type(lst[0])]()
    list_id = []
    list_id = list_id.append(i.Id for i in lst)
    unique_id = []
    for item in lst:
        if item.Id not in unique_id:
            unique_id.append(item.Id)
            unique_items.Add(item)
    return unique_items

def GetBicFromInput(var):	
    bic = None
    if var:
        cattype = var.GetType().ToString()
        if cattype == "Revit.Elements.Category": bic = System.Enum.ToObject(BuiltInCategory, var.Id)
        elif cattype == "Autodesk.Revit.DB": bic = System.Enum.ToObject(BuiltInCategory, var.Id)
        elif cattype == "Autodesk.Revit.DB.BuiltInCategory": bic = var
        elif cattype == "System.String":
            bics = System.Enum.GetValues(BuiltInCategory)
            found = [x for x in bics if x.ToString() == var]
            if len(found) > 0: bic = found[0]
    return bic

def ElementTypesByCategory(bic, doc):
	collector = FilteredElementCollector(doc).OfCategory(bic).WhereElementIsElementType()
	return collector.ToElements()
