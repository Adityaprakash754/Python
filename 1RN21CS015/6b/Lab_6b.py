import os
import sys
import pathlib
import zipfile

dirName = input("Enter directory name: ")
if not os.path.isdir(dirName):
    print("The directory" , dirName , "doesn't exist.")
    sys.exit(0)

curDirectory = pathlib.Path(dirName)
with zipfile.ZipFile("myfile.zip", mode = "w") as archive:
    for file_path in curDirectory.rglob ("*") :
        archive.write(file_path, arcname = file_path.relative_to(curDirectory))

if os.path.isfile("myfile.zip") :
    print("Archive", "myfile.zip" , "created successfully")
else:
    print("Error in creating zip archive")