import os 
import shutil

fromdir  = "C:/Users/nithi/Downloads"
todir  = "C:/Users/nithi/Documents/Python_Projects/downloadedText"
listOfFiles = os.listdir(fromdir)

for file in listOfFiles:    
    name,ext = os.path.splitext(file)
    if ext  == "":
        continue
    if ext in [".doc", ".pdf", ".docx", ".txt"]:
        path1 = fromdir+"/"+file
        path2 = todir+"/"+"documentFiles"
        path3 = todir+"/"+"documentFiles"
        if os.path.exists(path2):
            print("Moving ", file + "...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving ", file + "...")
            shutil.move(path1,path3)