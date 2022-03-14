

import os
import platform
import subprocess
import sys

def main(*args):
 current_directory = os.getcwd()
 build_dir = os.path.join(current_directory, 'build')

if not os.path.exists('build'):
  os.makedirs('build')
#os.system("cmake -S . -B build")
#os.system("cmake --build build")
#os.system("cd build\\")
#os.system("cmake --build . --config Release")
#os.system("cpack -G WIX --Config Release")

subprocess.run(["cmake","-S",".","-B","build","CMakeLists.txt"])
#subprocess.run(["cmake","-S",".","-B","build/Release","CMakeLists.txt"])

subprocess.run(["cmake", "--build","build"])
os.system("cd build/")

list_dir=subprocess.call(["cmake", "--build","build","--config","Release","--","/m"])

os.system("cd ..")
os.system("dir")
subprocess.call(["candle.exe" ,"*.wxs" ,"-o","obj/"])
subprocess.call(["light.exe", "obj\*.wixobj", "-o", "bin\SoftwareProductName.msi"]) 
#p = subprocess.run([exe, *args], cwd=build_dir, capture_output=True, text=True)
#print(p.stdout)
#tmp=subprocess.call("./a.out")
print("printing result")
print(tmp)

if __name__ == '__main__':
    args = []
    if len(sys.argv) > 1:
        args += sys.argv[1]
    main(*args)