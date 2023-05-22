# -*- coding: utf-8 -*-
__title__ = "ID to Mark"                           # Name of the button displayed in Revit UI
__doc__ = """Version = 1.0
Yazdığınız kodları test etmenizi sağlar"""              # Button Description shown in Revit UI
__author__ = "Baha YALNIZ" 

# Regular + Autodesk
import os, sys, math, datetime, time                                    # Regular Imports
from Autodesk.Revit.DB import *                                         # Import everything from DB (Very good for beginners)

# pyRevit
from pyrevit import revit, forms                                        # import pyRevit modules. (Lots of useful features)

# Custom Imports


# .NET Imports
import clr                                  # Common Language Runtime. Makes .NET libraries accessinble
clr.AddReference("System")                  # Refference System.dll for import.
from System.Collections.Generic import List # List<ElementType>() <- it's special type of list from .NET framework that RevitAPI requires
# List_example = List[ElementId]()          # use .Add() instead of append or put python list of ElementIds in parentesis.

doc   = __revit__.ActiveUIDocument.Document   # Document   class from RevitAPI that represents project. Used to Create, Delete, Modify and Query elements from the project.
uidoc = __revit__.ActiveUIDocument          # UIDocument class from RevitAPI that represents Revit project opened in the Revit UI.
app   = __revit__.Application                 # Represents the Autodesk Revit Application, providing access to documents, options and other application wide data and settings.
PATH_SCRIPT = os.path.dirname(__file__)     # Absolute path to the folder where script is placed.



if __name__ == '__main__':

    eleman_id = ElementId(359569)
    eleman = doc.GetElement(eleman_id)
    
    # print(eleman.get_Parameter(BuiltInParameter.ALL_MODEL_MARK).AsString())
      

          
    # AVOID  placing Transaction inside of your loops! It will drastically reduce perfomance of your script.
    t = Transaction(doc,__title__)  # Transactions are context-like objects that guard any changes made to a Revit model.

    # You need to use t.Start() and t.Commit() to make changes to a Project.
    t.Start()  # <- Transaction Start

    all_floors = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Floors).WhereElementIsNotElementType().ToElements()
    
    n = 0
    for floor in all_floors:
        floor_mark = floor.get_Parameter(BuiltInParameter.ALL_MODEL_MARK)
        floor_mark.Set(str(floor.Id))
 
    t.Commit()  # <- Transaction End

