import sys
sys.path.append("../lib")
import  os,shutil
from util import get_dir

# 6 digits submissions is unique
id = ["000000"]

src = "/home/yb/sambashare/F21-lab1/error_sub/"
dst = "/home/yb/sambashare/F21-lab1/error_sub2/"

os.system("mkdir " + dst)
print("mkdir " + dst)

processed = []

count = 0
os.chdir(src)
dir = get_dir(".")
for f in dir:
    for i in id:
        ii = str(i)

        if ii in f:
            os.system("cp -r "+os.path.join(src,f)+" " +os.path.join(dst,"")+" ")
            print("cp -r "+os.path.join(src,f)+" " +os.path.join(dst,"")+" ")
            count+= 1
            if i in processed:
                # sometimes they turn in 2 copies
                print("Duplicate! id:" + i)
            processed.append(i)


print(len(id),'/',count)
