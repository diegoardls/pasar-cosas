import os, shutil
directorio = "C:/Users/drack/Downloads"
for archivo in os.listdir(directorio):
    if archivo.endswith(".png"):
        shutil.move(os.path.join(directorio, archivo), os.path.join(directorio, "Images"))
    elif archivo.endswith(".pdf"):
        shutil.move(os.path.join(directorio, archivo), os.path.join(directorio, "Document"))
