import  os,shutilfrom util import get_dir

from util import get_dir
# PDF

# use this after "folder_to_files"
# can only find pdf in the 1st level
# folder


# ALSO!
# assume only 1 pdf

def extract_pdf(sub_dir, dst_dir):
    os.system("mkdir -p " + dst_dir)
    os.chdir(sub_dir)
    dir = get_dir(".")

    for i in dir:
        print(i)
        os.chdir(i)
        os.system("cp *.pdf " + dst_dir +"/"+i+".pdf")
        # os.system("cp *.docx " + dst_dir + "/" + i + ".docx")
        os.chdir(sub_dir)

# submission folder
sub_directory = "/home/yb/112L_W21/lab4/submissions/"

dst_dir = "/home/yb/112L_W21/lab4/pdf_report"
extract_pdf(sub_directory, dst_dir)
