from os import chdir
from pathlib import Path

def main() -> None:
    print("Current working directory: ", Path.cwd())
    print("Home directory: ", Path.home())

    # Path returns path object
    # You can also create your own path object
    # This object does not check if the path exists

    path = Path("/usr/bin/python3")
    
    # You can check if the path exists though
    print(path.exists())
    
    # Alternatively you can create a new path like this:
    path = Path("/usr") / "bin" / "python3"
    print(path.exists())

    # use \ in windows and r 
    # path = Path(r"c:\windows\System")

    # Reading the path from file:
    path = Path.cwd() / "settings.yaml"
    print(path.exists())

    # Reading files in general:
    with path.open() as file:
        print(file.read())

    # And alternatively:
    print(path.read_text())

    # Path to file:
    path = Path("settings.yaml")
    full_path = path.resolve()
    print("Parent of this path", full_path.parent)
    # Can continue till you reach the root directory
    print("Parent of this path", full_path.parent.parent)

    # to print filename, extension and stem
    print("Filename", full_path.name)
    print("Extension", full_path.suffix)
    print("Stem", full_path.stem)
    
    # Is a file a directory or a file:
    print("Is a directory", full_path.is_dir())
    print("Is a file", full_path.is_file())

    # Creating and deleting new files:
    new_file = Path.cwd() / "new_file.txt"
    new_file.touch()

    # Writing text:
    new_file.write_text("Hello, world!")

    # Deleting a file:
    new_file.unlink()

    # Creating directory:
    new_dir = Path.cwd() / "new_dir"
    # new_dir.mkdir()

    # Deleting directory:
    # new_dir.rmdir()

    # To change the directory:
    chdir(new_dir)
    print("Current working directory", path.cwd())










    




        




if __name__ == "__main__":
    main()
