# /tools/Xilinx/Vivado/2020.1/bin/vivado -nolog -nojournal -mode tcl -source test3.tcl
import sys
sys.path.append("../lib")
import time
import os
import subprocess
from subprocess import PIPE
from collections import defaultdict
from run_util import *
from util import get_dir, get_id_from_path, output_report
#
gradebook = dict()
# sensitive field list. Sensitive filed is the field in the 
# Verilog test bench that we want to keep a record of.
# Values associated with the sensitive fields will be 
# saved in the report. 
#
# format is
# *field* = {value} in the Verilog Testbench. 
#
sensitive_words = ["CompileError", "warning",
            "tb1_ANDI_1", "tb1_NOR_1", "tb1_SLT_1"]

# name and path for generated report
report_name = "/home/yb/sambashare/F21-lab2/auto_report_1.csv"

# test bench TB files' names
tb = "/home/yb/sambashare/F21-lab2/tb/*"

submission_path = "/home/yb/sambashare/F21-lab2/submissions"

def run():
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

        print("--------------------------------------")
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

        # finalized result
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

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        raise e
    finally:
        output_report(report_name, gradebook, sensitive_words)
