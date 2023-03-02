def runStartupMacros(name):
    # Do not run when NoneWorkbench is activated because UI isn't yet completely there
    if name != "NoneWorkbench":
        # Run macro only once by disconnecting the signal at first call
        FreeCADGui.getMainWindow().workbenchActivated.disconnect(runStartupMacros)

        # Following 2 lines shall be duplicated for each macro to run
        import csv_macro
        csv_macro.run()

# The following 2 lines are important because InitGui.py files are passed to the exec() function...
# ...and the runMacro wouldn't be visible outside. So explicitly add it to __main__
import __main__
__main__.runStartupMacros = runStartupMacros

# Connect the function that runs the macro to the appropriate signal
FreeCADGui.getMainWindow().workbenchActivated.connect(runStartupMacros)