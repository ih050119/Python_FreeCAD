import subprocess
import time
import os

prefix = 'modified_'
model_folder = 'model/'

# Start FreeCAD application
freecad_exe = "C:/Program Files/FreeCAD 0.20/bin/FreeCAD.exe" # this may need to be changed to the full path of FreeCAD executable file
freecad = subprocess.Popen([freecad_exe], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Wait for the file with "modified_" prefix to be created
while True:
    for filename in os.listdir(model_folder):
        if filename.endswith('.FCStd') and prefix in filename:
            print("The file was created:", filename)
            # Close the application
            freecad.terminate()
            break
    else:
        # Continue the while loop
        continue
    # Break the while loop
    break
