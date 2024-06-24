from pathlib import Path
from time import ctime
import shutil

path = Path(r"python_fundamentals\fundamentals.py")
print(path.exists())
print(path.is_file())
print(path.is_dir())
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
path = path.with_name("file.txt")
print(path)
print(path.absolute())

path = Path(r"C:\Users\Alan\Documents\GitHub\python_fundamentals")

paths = [p for p in path.iterdir() if p.is_dir()]
py_files = [p for p in path.glob("*.py")]
py_files_r = [p for p in path.rglob("*.py")]
print(paths)
print(py_files)
print(py_files_r)

# files


path = Path(r"C:\Users\Alan\Documents\GitHub\python_fundamentals\important.py")
# path.exists()
# path.rename("init.txt")
# path.unlink()
print(ctime(path.stat().st_ctime))

print(path.read_text())
# path.write_text("....")
# path.write_bytes()


source = Path(r"C:\Users\Alan\Documents\GitHub\python_fundamentals\important.py")
target = Path() / "important.py"

shutil.copy(source, target) #clean way to copy file