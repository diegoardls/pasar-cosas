import os
import shutil

directory = "C:/Users/drack/Downloads"

# Crear las carpetas si no existen
if not os.path.exists(os.path.join(directory, "Images")):
    os.makedirs(os.path.join(directory, "Images"))
if not os.path.exists(os.path.join(directory, "Documents")):
    os.makedirs(os.path.join(directory, "Documents"))

# Mover los archivos
for file in os.listdir(directory):
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
        shutil.move(os.path.join(directory, file), os.path.join(directory, "Images", file))
    elif file.endswith(".pdf") or file.endswith(".txt") or file.endswith(".docx"):
        shutil.move(os.path.join(directory, file), os.path.join(directory, "Documents", file))

print(" Organización completada.")
