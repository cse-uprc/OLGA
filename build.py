import os
import importlib
import consts

# setup temp folder and .commands file
try:
    os.makedirs(consts.TMP_FOLDER)
except FileExistsError:
    pass

open(consts.COMMANDS_FILE, "w").close()


files = []  # empty list for extension files (with no extension)
# r=root, d=directories, f = files
print("Getting list of Extensions")
for r, d, f in os.walk(consts.EXTENSIONS_FOLDER):
    for file in f:
        if ".py" in file and not (".pyc" in file):
            print(file)
            files.append(file.replace(".py", ""))

# now we have all teh extensions and can import and install each
print("Importing Extensions")
for file in files:
    print("Installing "+file)
    extension = __import__("Extensions."+file, globals(), locals(), ["install"], 0)
    extension.install()