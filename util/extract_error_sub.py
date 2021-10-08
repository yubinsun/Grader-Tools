
import  os,shutil
from util import get_dir

# 6 digits submissions is unique
id = ["252841", "290529", "255139", "251673", "285934",
"253196", "255644", "280027", "223660", "236721",
"250777", "285377", "285469", "254916"]

src = "/home/yb/112L_W21/lab4/submissions/"
dst = "/home/yb/112L_W21/Lab4/error_sub/"

count = 0
os.chdir(src)
dir = get_dir(".")
for f in dir:
    for i in id:
        ii = str(i)

        if ii in f:
            os.system("cp -r "+os.path.join(src,f)+" " +dst+" ")
            print("cp -r "+os.path.join(src,f)+" " +dst+" ")
            count+= 1

print(len(id),'/',count)