# /tools/Xilinx/Vivado/2020.1/bin/vivado -nolog -nojournal -mode tcl -source test3.tcl
import time
import os
import subprocess
from subprocess import PIPE
from collections import defaultdict
from run_util import *
from util import get_dir, get_id_from_path, output_report
#
gradebook = dict()
# sensitive field list
# format is
# *field* = {value}
sensitive_words = ["CompileError", "warning",
            "SW1", "SW2", "SW3",  "NO_DEPENDENCY_ANDI",
            "NO_DEPENDENCY_NOR", "NO_DEPENDENCY_SLT", "NO_DEPENDENCY_SLL",
            "NO_DEPENDENCY_SRL", "NO_DEPENDENCY_SRA", "NO_DEPENDENCY_XOR",
            "NO_DEPENDENCY_MULT", "NO_DEPENDENCY_DIV", "ANDI_No_Forwarding",
            "Forward_EX_MEM_to_EX_B", "Forward_MEM_WB_to_EX_A1", "SLL_No_Forwarding",
            "Forward_EX_MEM_to_EX_A", "Forward_MEM_WB_to_EX_A2", "XOR_No_Forwarding",
            "MULT_No_Forwarding", "Forward_MEM_WB_to_EX_B", "DATA_HAZARD_RS_DEPENDENCY",
            "DATA_HAZARD_RT_DEPENDENCY", "CONTROL_HAZARD_BRANCH", "CONTROL_HAZARD_JUMP"
            ]

# name for generated report
report_name = "/home/yb/112L_W21/lab4/auto_report_2.csv"

# TB files' names
tb = "/home/yb/112L_W21/lab4/tb/*"

submission_path = "/home/yb/112L_W21/lab4/submissions"

# vivado path
vivado_path = ["/tools/Xilinx/Vivado/2020.1/bin/vivado",
               "-nolog", "-nojournal", "-mode", "tcl", "-source"]


#
os.chdir(submission_path)

# get subdirectories
dir = get_dir(submission_path)

counter = 0
# run TB for every folder inside submission folder
for i in dir:
    # start time
    t1 = time.time();

    # copy files for TB
    r = subprocess.run("cp " + tb + " " + os.path.join(submission_path,i), shell=True)

    # student canvas id
    student_id = get_id_from_path(i)

    d = defaultdict(str)

    print("-------------------" + "-------------------")
    os.chdir(os.path.join(submission_path,i))
    print("current dir :", os.getcwd())

    # running the process
    r = subprocess.Popen("./run.sh",stdout=PIPE,  stderr=PIPE, shell=True)
    # live output
    out = ""
    for line in iter(r.stdout.readline,''):
        if r.poll() is not None:
            break
        print(line.decode("utf-8"), end = "")
        out += line.decode("utf-8")
        if parse(line.decode("utf-8")) is not None:
            key,value = parse(line.decode("utf-8"))
            if key in d:
                d["warning"] += "duplicate key *" + key + "*:"
            d[key] = value.strip()

    # finilized result
    if student_id in gradebook:
        print("Warning: duplicate ID")
        d["warning"] += "duplicate ID;"
    gradebook[student_id] = d
    # clean up
    os.chdir(submission_path)
    counter += 1
    print(str(counter) + "/"+str(len(dir))+" finished")
    # time for one iteration
    print(time.strftime("%H:%M:%S", time.localtime()),'\t\t,', time.time() - t1,
          "\n---------------------------------------------")
    # break



output_report(report_name, gradebook, sensitive_words)

