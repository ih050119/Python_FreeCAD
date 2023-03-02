
import sys
import FreeCAD as App, FreeCADGui

def run():
	App.open("C:/Users/supernova/Downloads/FreeCAD-Python/model/table.FCStd")
	spreadsheet = App.getDocument('table').getObject('Spreadsheet')
	spreadsheet.set('D1', '500')
	App.ActiveDocument.recompute()
	App.getDocument("table").saveAs("C:/Users/supernova/Downloads/FreeCAD-Python/model/modified_table2.FCStd")
	App.closeDocument("table")

if __name__ == '__main__':
	run()

