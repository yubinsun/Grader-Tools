# grade one question of all submissions
"""
Description: grade one question of all submissions.
Tested in ubuntu.

How to use: change file_name, submission_path, report_name
Change grader_shortcuts if you wish to add more shortcuts. 
"""
import os,re
import sys
sys.path.append("../lib")
sys.path.append("/lib")

from util import get_dir, output_report, get_id_from_path, clear_screen

file_name = "output/12.txt"
sensitivity_words = ["ERROR", file_name, file_name+"-comments" ]
report_name = "/home/yb/sambashare/F21-lab3/report11" # including path
submission_path = "/home/yb/sambashare/F21-lab3/formatted/" # path to all submission

grader_shortcuts = {
    ".": 10,
    "+": 10,
    "a": 10,
    "e" : "empty"
}
def manual_grader_one(path, filename):
    # path : path of one submission folder. eg. "submissions/joneDoe_123456_12345678/"
    # filename : name of the submission. eg. "question2.txt"
    report = {filename : "", filename+"-comments": ""}
    file = open(os.path.join(path, filename))
    lines = file.read()

    lines = re.sub(r"(\d{6})(\d{5})(\d{5})(\d{5})(\d{5})(\d{6})", r"\1 \2 \3 \4 \5 \6", lines)

    print("submitted file: \n\n")
    print(lines)
    while 1:

        # process score
        score = input("score in number, or comments: ")
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
    dirs = sorted(dirs)
    try:
        for c,i in enumerate(dirs):
            clear_screen()
            print("---------", i, "----------")
            print(c+1,'/',len(dirs))
            path = os.path.join(submission_folder_path, i)
            id = get_id_from_path(i)
            r = manual_grader_one(path, filename)
            report[id] = r
    except Exception as e:
        print(e)
        print(report)
    finally:
        output_report(report_name, report, sensitivity_words)
        print("report created!")
manual_grader_all(submission_path, file_name)