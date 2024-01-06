from pathlib import Path


path = Path(
    "python-programming-course-developers/7-PythonStandardLibrary/3-WorkingWithDirectories/ecommerce")
"""
path.exists()
path.mkdir()
path.rmdir()
path.rename("ecommerce2")
 """


print(path)
# only folders inside the ecommerce folder
print([p for p in path.iterdir() if p.is_dir()])
# only files in the ecommerce folder that have .py extension
print([p for p in path.glob("*.py")])
# recursive glob: searches for py files in ecommerce folder and its children
print([p for p in path.rglob("*.py")])
