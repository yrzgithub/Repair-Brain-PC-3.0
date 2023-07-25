from os import system


# sudo dnf install python3-tkinter

requirements_txt = "requirements.txt"
required_modules = []

with open(requirements_txt,"r") as file:
    required_modules = file.read().split("\n")
    file.close()

print("Reuired modules : \n",*required_modules,sep="\n",end="\n")

for module in required_modules:
    print(f"\nInstalling {module}\n")
    system(f"pip install {module}")

input("\n\nPress enter to exit...")