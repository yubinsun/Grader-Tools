"""
Decription: This script "flats" all files in a folder.
Use this to convert submission with subfolders into one one
folder.
HOW TO USE:
eg. Convert structures from
Submission: change "path" variable in the main function.
+All_Submissions
    +Submission1
        +project_folder
            +folder1
                +file1
                +file2
        +report.txt
    +submission2
        +report.txt
        +file1
        +file2

To structure like this:
+All_Submissions
    +Submission1
        +file1
        +file2
        +report.txt
    +submission2
        +report.txt
        +file1
        +file2
"""
import sys
sys.path.append("../lib")
import os,shutil
from util import get_dir

def change_non_std_char(root = None):
    if root is not None:
        os.chdir(root)
    dir = os.listdir(".")
    for i in dir:
        dst = i.replace(" ","_")
        dst = dst.replace("(","_")
        dst = dst.replace(")","")
        dst = dst.replace("#","")
        dst = dst.replace("'", "")
        shutil.move(i,dst)


def folder_to_files(root = os.getcwd(), depth = 0 ):
    if depth == 3:
        return False
    os.chdir(root)
    #
    change_non_std_char(root)
    os.system("rm -rf __MACOSX")
    os.system("rm -rf _MACOSX")
    # start next level
    dir = get_dir(".")
    if dir == []:
        return True
    for i in dir:
        os.chdir(i)
        os.system("rm -rf __MACOSX")
        os.system("rm -rf _MACOSX")
        os.system("mv * ../")
        os.chdir("..")
        os.system("rm -rf " + i)
    return folder_to_files(root,depth+1)

if __name__ == '__main__':
    # move files from sub-director to root directory

    # submission_path = "sub_tmp/"
    # path = os.path.join(os.getcwd(),submission_path)
    path = "/home/yb/112L_W21/lab4/submissions"
    os.chdir(path)
    change_non_std_char(path)
    dir = get_dir(".")

    for f in dir:
        print(f)
        if not folder_to_files(os.path.join(path,f)):
            print("ERROR: " + f)