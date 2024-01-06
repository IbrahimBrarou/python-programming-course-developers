from pathlib import Path
from zipfile import ZipFile

# create zip and write to it

with ZipFile("files.zip", mode="w") as zip:
    for path in Path("python-programming-course-developers/7-PythonStandardLibrary/5-WorkingWithZipFiles/ecommerce").rglob("*.*"):
        zip.write(path)


# read from zip and extracting
with ZipFile("files.zip", mode="r") as zip:
    print(zip.namelist())
    info = zip.getinfo(
        "python-programming-course-developers/7-PythonStandardLibrary/5-WorkingWithZipFiles/ecommerce/__init__.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("extract")
