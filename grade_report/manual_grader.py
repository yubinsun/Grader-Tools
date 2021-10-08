"""
Description: grade Reports of all submissions.
Only works in Windows because it use "start" to open
default PDF reader. Need to change this line if needed
to use in Linux.

How to use: change report_name, submission_path
"""

import os,re
import sys
sys.path.append("../lib")

from util import get_dir, output_report, get_id_from_path, clear_screen
file_name = "report"
sensitivity_words = ["ERROR", file_name, file_name+"-comments" ]
report_name = "../lab4/manual_grade_report_report.csv" # including path
submission_path = "C:\\Users\\yubin\\Desktop\\112L_winter2021\\lab4\\pdf_report" # path to all submission

grader_shortcuts = {
    ".": 30,
    "+": 30,
    "a": 30,
    "e" : "empty"
}
def manual_grader_one(path, filename):
    # path : path of one submission folder. eg. "submissions/joneDoe_123456_12345678/"
    # filename : name of the submission. eg. "question2.txt"
    report = {filename : "", filename+"-comments": ""}
    #file = open(os.path.join(path, filename))
    file = os.system("start "+path)

    print("submitted file: \n\n")
    #print(lines)
    while 1:

        # process score
        score = input("score in number, or in shortcuts, or input comments: ")
        if score == '':
            continue
        for shortcuts in grader_shortcuts:
            if score == shortcuts:
                score = grader_shortcuts[shortcuts]
        try:
            tmp = float(score)
            score = tmp
        except Exception as e:
            report[filename+"-comments"] += score
            score = 0
        break

    report[filename] = score
    return report

def manual_grader_all(submission_folder_path, filename):
    # path : path of one submission folder. eg. "submissions/"
    # filename : name of the submission. eg. "question2.txt"
    report = {}
    dirs = get_dir(submission_folder_path)
    dirs = os.listdir(submission_folder_path)

    dirs = sorted(dirs)

    try:
        for c,i in enumerate(dirs):
            clear_screen()
            print("---------", i, "----------")
            print(c+1,'/',len(dirs))
            path = os.path.join(submission_folder_path, i)
            id = get_id_from_path(i)
            r = manual_grader_one(path, filename)
            report[id] = r;
    except Exception as e:
        print(e)
        print(report)
    finally:

        output_report(report_name, report, sensitivity_words)
        print("report created!")
manual_grader_all(submission_path, file_name)
