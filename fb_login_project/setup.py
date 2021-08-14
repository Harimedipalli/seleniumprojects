import os
from distutils import sysconfig

directory = os.getcwd()
site_packages_path = sysconfig.get_python_lib()
file_path = os.path.join(site_packages_path, "MySeleniumPath.pth")

if os.path.isfile(file_path):
    os.remove(file_path)
with open(file_path, 'w+') as as_pth:
    as_pth.write(directory+'\n')
    as_pth.write(directory + os.sep + "AppDrivers" + os.sep + "\n")
    as_pth.write(directory+os.sep+"PageActions"+os.sep+"\n")
    as_pth.write(directory+os.sep+"PageObjects"+os.sep+"\n")
    as_pth.write(directory+os.sep+"Keywords"+os.sep+"\n")

print("\tInstalling Requirements for selenium project\n")
os.system("pip install -r requirements.txt")

