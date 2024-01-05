from pathlib import Path

path = Path("C:\\Users\\jmigu\\Desktop")  # creating a path object in Windows.
# we can also do it with a raw string using the "r" in the begining. In a raw string the "\" it is not an escape sequence.
path = Path(r"C:\Users\jmigu\Desktop.ex")

# To creat a path object that represents the current folder.
path_current_folder = Path()

# A relative path. In the curretn folder go to the subfolder "test_folder".
relative_path = Path(r"09 Python Standard Library\test_folder\test_file.py")

# We can use the "/" to combine path obejects.
combine_path = Path(r"C:\Users\jmigu\Desktop") / Path(r"test_folder")
# We can use the "/" to combine path with a string.
combine_path = Path(r"C:\Users\jmigu\Desktop") / "new folder"
print(combine_path)

# The home method returns the home directory of the current user.
Path.home()

path.exists()  # to check if the path exxists
path.is_file()  # to check if the path is a file
path.is_dir
print(path.name)
print(path.stem)  # file name without extension
print(path.suffix)  # to get the extension
print(path.parent)
path = path.with_name("file.txt")
print(path)
print(path.absolute())
path = path.with_suffix(".py")
print(path)
