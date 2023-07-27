from os import system
from os.path import isdir

if not isdir("venv"):
    print("venv not found....Creating venv...\n\n")
    system("python -m venv venv")
    print("\n\nvenv created")
    import setup

else:
    print("venv already exists")