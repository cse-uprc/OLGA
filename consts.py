import os

# Get directory paths
OLGA_FOLDER = os.getcwd()   # get the current working directory
EXTENSIONS_FOLDER = os.path.join(OLGA_FOLDER,"Extensions")  # get extensions folder
TMP_FOLDER = os.path.join(OLGA_FOLDER,"tmp")    # tmp folder

# Get specific file paths
COMMANDS_FILE = os.path.join(TMP_FOLDER,".commands")
CONFIG_FILE = os.path.join(OLGA_FOLDER,".config")