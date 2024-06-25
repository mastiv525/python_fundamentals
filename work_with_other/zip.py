from pathlib import Path
from zipfile import ZipFile

with ZipFile("files.zip", "w") as zip:
    for path in Path("work_with_other").rglob("*.*"):
        zip.write(path)

# with ZipFile("files.zip") as zip:
#     print(zip.namelist()