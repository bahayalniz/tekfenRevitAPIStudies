# -*- coding utf-8 -*-

__title__   = "Seçilileri Listele"
__author__  = "Baha YALNIZ"
__doc__     = '''Secili elementleri listeler.'''

#VARIABLES
uidoc = __revit__.ActiveUIDocument

#CUSTOM IMPORT
from tekfentest._selection import get_selected_elements

if __name__ == '__main__':
    print(get_selected_elements(uidoc))