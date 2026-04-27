import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import os
import warnings
import zmq
import subprocess

warnings.filterwarnings("ignore", category=RuntimeWarning, message="Proactor event loop does not implement add_reader family of methods required for zmq")

import subprocess
import sys

# List of required modules


# ANSI color codes
class colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BOLDBLACK = '\033[1m\033[30m'
    BOLDRED = '\033[1m\033[31m'
    BOLDGREEN = '\033[1m\033[32m'
    BOLDYELLOW = '\033[1m\033[33m'
    BOLDBLUE = '\033[1m\033[34m'
    BOLDMAGENTA = '\033[1m\033[35m'
    BOLDCYAN = '\033[1m\033[36m'
    BOLDWHITE = '\033[1m\033[37m'



os.environ['PYDEVD_DISABLE_FILE_VALIDATION'] = '1'
os.environ['PYZMQ_WARNINGS'] = 'ignore'

required_modules = [
    "numpy",
    "pandas",
    "streamlit",
    "streamlit_option_menu",
    "pickle",  # Note: pickle is part of Python's standard library; no installation needed.
    "matplotlib",
    "sklearn",
]

# Check and install modules
def install_modules(modules):
    for module in modules:
        try:
            # Import the module to check if it's already installed
            __import__(module)
            print(f"'{module}' is already installed.")
        except ImportError:
            # If not installed, install it using pip
            print(f"'{module}' is not installed. Installing now...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])

if __name__ == "__main__":
    install_modules(required_modules)
print(colors.BLUE+ "Running Aids_disease_prediction.ipynb"+ colors.RESET)
notebook_path = "Scripts/Aids_disease_prediction.ipynb"
with open(notebook_path) as f:
    nb = nbformat.read(f, as_version=4)
ep = ExecutePreprocessor(timeout=600)  # Adjust timeout as needed
ep.preprocess(nb, {'metadata': {'path': '.'}})
print(colors.GREEN+"Run successful\n","1 done\n"+colors.RESET)

print(colors.BLUE+"Running chronic_kidney_disease.ipynb"+colors.RESET)
notebook_path = "Scripts/chronic_kidney_disease.ipynb"
with open(notebook_path) as f:
    nb = nbformat.read(f, as_version=4)
ep = ExecutePreprocessor(timeout=600)  # Adjust timeout as needed
ep.preprocess(nb, {'metadata': {'path': '.'}})
print(colors.GREEN+"Run successful\n","2 done\n"+colors.RESET)

print(colors.BLUE+"Running diabetes.ipynb"+colors.RESET)
notebook_path = "Scripts/diabetes_prediction.ipynb"
with open(notebook_path) as f:
    nb = nbformat.read(f, as_version=4)
ep = ExecutePreprocessor(timeout=600)  # Adjust timeout as needed
ep.preprocess(nb, {'metadata': {'path': '.'}})
print(colors.GREEN+"Run successful\n","3 done\n"+colors.RESET)

print(colors.BLUE+"Running heart_disease_prediction.ipynb"+colors.RESET)
notebook_path = "Scripts/heart_disease_prediction.ipynb"
with open(notebook_path) as f:
    nb = nbformat.read(f, as_version=4)
ep = ExecutePreprocessor(timeout=600)  # Adjust timeout as needed
ep.preprocess(nb, {'metadata': {'path': '.'}})
print(colors.GREEN+"Run successful\n","4 done\n"+colors.RESET)

print(colors.BLUE+"Running parkinsons_disease.ipynb"+colors.RESET)
notebook_path = "Scripts/parkinsons_disease.ipynb"
with open(notebook_path) as f:
    nb = nbformat.read(f, as_version=4)
ep = ExecutePreprocessor(timeout=600)  # Adjust timeout as needed
ep.preprocess(nb, {'metadata': {'path': '.'}})
print(colors.GREEN+"Run successful\n","5 done\n"+colors.RESET)

print(colors.BOLDMAGENTA+"FILE OPERATION SUCCESSFUL\n"+colors.RESET)

print(colors.RED+"Trying to trigger Streamlit Web App"+colors.RESET)

web_app = "runtime.exe"

subprocess.run(web_app)