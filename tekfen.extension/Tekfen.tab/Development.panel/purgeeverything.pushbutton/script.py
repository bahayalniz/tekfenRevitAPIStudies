# -*- coding: utf-8 -*-
__title__ = "Purge Everything"                           # Name of the button displayed in Revit UI
__doc__ = """Version = 1.0
Belgede bulunan içiçe geçmiş olanlar dahil olmak üzere tüm familyleri ve elemanları purge eyler."""              # Button Description shown in Revit UI
__author__ = "Baha YALNIZ" 

# Regular + Autodesk
import os, sys, math, datetime, time                                    # Regular Imports
import Autodesk.Revit.DB as DB                                         # Import everything from DB (Very good for beginners)
import Autodesk.Revit.UI as UI  
from Autodesk.Revit.UI import RevitCommandId
from Autodesk.Revit.UI import UIApplication
from Autodesk.Revit.UI import ExternalCommandData

# pyRevit
from pyrevit import revit, forms                                        # import pyRevit modules. (Lots of useful features)

# .NET Imports
import clr                                  # Common Language Runtime. Makes .NET libraries accessinble
clr.AddReference("System")                  # Refference System.dll for import.

from tekfentest.unique_items import *

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# Import RevitNodes
clr.AddReference("RevitNodes")
clr.AddReference('RevitAPIUI')
import Autodesk
import Revit

# Import Revit elements
from Revit.Elements import *

# Import DocumentManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

import System

#------------------------------------------------------------------------------------------------


from System.Collections.Generic import List # List<ElementType>() <- it's special type of list from .NET framework that RevitAPI requires
# List_example = List[ElementId]()          # use .Add() instead of append or put python list of ElementIds in parentesis.

doc   = __revit__.ActiveUIDocument.Document     # Document   class from RevitAPI that represents project. Used to Create, Delete, Modify and Query elements from the project.
uidoc = __revit__.ActiveUIDocument              # UIDocument class from RevitAPI that represents Revit project opened in the Revit UI.
app   = __revit__.Application                   # Represents the Autodesk Revit Application, providing access to documents, options and other application wide data and settings.
PATH_SCRIPT = os.path.dirname(__file__)         # Absolute path to the folder where script is placed.
active_view = doc.ActiveView
uiapp = UI.UIApplication(app)



def get_nested(doc):

    collecter_flatten = List[DB.Element]()
    
    collector = DB.FilteredElementCollector(doc)\
                    .OfClass(DB.FamilyInstance)\
                    .WhereElementIsNotElementType()\
                    .ToElements()

    if len(collector) > 0:

        family_names = []
        
        for i in collector:
            family_name = i.get_Parameter(DB.BuiltInParameter.ELEM_FAMILY_PARAM).AsValueString()
            
            if family_name not in family_names:
                family_names.append(family_name)      
                collecter_flatten.Add(i)
        
        return collecter_flatten
    
    else:
        return List[DB.Element]()

    # print("Number of active family instances: " + str(len(collecter_flatten)))

    # print("-"*50)

    
def get_nested_of_list(elementList):

    collecter_flatten = List[DB.Element](elementList)
    
    for i in elementList:
        fam_doc = __revit__.ActiveUIDocument.Document.EditFamily(i.Symbol.Family)
        nested_families = get_nested(fam_doc)
        for j in nested_families:
            collecter_flatten.Add(j)

    return collecter_flatten

collecter_flatten = get_nested_of_list(get_nested(doc))

nList = collecter_flatten
output = collecter_flatten
n = len(collecter_flatten)


while n > 0:
    nList = get_nested_of_list(get_nested(doc))
    n = len(nList)
    for element in nList:
        output.Add(element)
        doc = doc.EditFamily(element.Symbol.Family)

output = unique_items(output)

for i in output:
    print(i.get_Parameter(DB.BuiltInParameter.ELEM_FAMILY_PARAM).AsValueString())
 

if __name__ == '__main__':

    t = Transaction(doc,__title__)  
    
    t.Start()  # <- Transaction Start
    
    command = UI.RevitCommandId.LookupPostableCommandId(UI.PostableCommand.PurgeUnused)
    uiapp.PostCommand(command)
    
        # Wait for the dialog box to appear
    dialogBoxShowing = False
    def OnDialogBoxShowing(sender, args):
        global dialogBoxShowing
        dialogBoxShowing = True
        args.OverrideResult(UI.TaskDialogResult.Ok)

    uiapp.DialogBoxShowing += OnDialogBoxShowing

    # Wait until the dialog box is shown
    while not dialogBoxShowing:
        uiapp.DoEvents()
        
    t.Commit()  # <- Transaction End
    
    #ALL ELEMENTS IN ACTIVE VIEW & GET CATEGORIES
    
    # all_categories = [] 
    # parameter_list = []
    
    # for i in collector:
    #     a = i.get_Parameter(BuiltInParameter.ELEM_CATEGORY_PARAM_MT).AsValueString()
        
    #     if a not in parameter_list and a != "" and i.GetType() == FamilyInstance.GetType():
    #         parameter_list.append(a)
    #         all_categories.append(i)
    
    # print("All categories from selected elements:")

    # print(all_categories)

    # print("--"*25)    
    
    
    # family_types = []
    # for i in all_categories:
    #     family_symbols = FilteredElementCollector(doc).OfCategory(i.Category.BuiltInCategory).WhereElementIsElementType() 
    #     for symbol in family_symbols:
    #         family_id = symbol.Id
    #         family_types.append(doc.GetElement(family_id))  
    
    
    # for type in family_types:
    #     print(type.Id)

    
    # family_types = List[Element]()
    
    # for i in x:
    #     types = ElementTypesByCategory(i.BuiltInCategory, doc)
    #     for j in types:
    #         if j not in family_types and j != None:
    #             family_types.Add(j)
    
    # print(doc.GetElement(family_types[0]).Id)
    # for i in family_types: print(i.LookupParameter("Family and Type"))

    

