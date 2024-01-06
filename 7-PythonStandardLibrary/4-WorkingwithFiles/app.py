from pathlib import Path
from time import ctime
import shutil

path = Path(
    "python-programming-course-developers/7-PythonStandardLibrary/4-WorkingwithFiles/ecommerce/__init__.py")
# path.exists()
# path.rename("init.txt")
# path.unlink()  # to delete the file
# print(ctime(path.stat().st_ctime))  # creation date
print(path.read_bytes())  # prints the bytes of the path
print(path.read_text())  # prints the text of the file
path.write_text("...")
# path.write_bytes()

# To copy a file to another file
target = Path() / "__init__.py"
target.write_text(path.read_text())


# a better way is using shutil
shutil.copy(path, target)
