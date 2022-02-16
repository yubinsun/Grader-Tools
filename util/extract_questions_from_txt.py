"""
Description: Use to extract each question from one txt file.
Designed for lab3.txt. Extract questions from lab3.txt into
output/ in the original folder. 

How to use: change report_name, submission_path, patterns
"""
import re, os, sys

sys.path.append("../lib")
from util import get_dir, get_id_from_path, output_report

submission_path = "/home/yb/sambashare/F21-lab3/formatted"  # path to all submission
report_name = "/home/yb/sambashare/F21-lab3/extract_questions_report"  # including path
patterns = {
    "11": "Program[ ]*1[\S\s]*?-----[ ]*end[ ]*-----",
    "12": "Program[ ]*1\.2[\S\s]*?-----[ ]*end[ ]*-----",
    "21": "Program[ ]*2[\S\s]*?-----[ ]*end[ ]*-----",
    "22": "Program[ ]*2\.2[\S\s]*?-----[ ]*end[ ]*-----",
    "31": "Program[ ]*3[\S\s]*?-----[ ]*end[ ]*-----",
    "32": "Program[ ]*3\.2[\S\s]*?-----[ ]*end[ ]*-----",
    "41": "Program[ ]*4[\S\s]*?-----[ ]*end[ ]*-----",
    "43": "Program[ ]*4\.3[\S\s]*?-----[ ]*end[ ]*-----"
}
sensitivity_words = ["ERROR", "11", "12", "21", "22", "31", "32", "41", "43"]


def extract(submission_file_path, submission_file_name="lab3.txt", output_path="output/",
            possible_submission_file_name="*lab3*.txt"):
    # extract one submission
    # output_path : relative to path
    print(submission_file_path)
    output_report = {"ERROR": ""}
    try:
        # in case "lab3.txt" has prefix.
        os.system(
            "mv " + os.path.join(submission_file_path, possible_submission_file_name) + " " + os.path.join(
                submission_file_path, submission_file_name))
        f = open(os.path.join(submission_file_path, submission_file_name))
        lines = f.read()
        f.close()
    except FileNotFoundError as e:
        print("FILE NOTE FOUND");
        output_report["ERROR"] += "FILE NOTE FOUND"
        lines = ""
    except Exception as e:
        print(e);
        output_report["ERROR"] += str(e)
        lines = ""

    for pat in patterns:
        try:
            r = re.search(patterns[pat], lines)
            out = ""
            if r is None:
                print(pat, "not found")
                output_report[pat] = "not found"

            else:
                print(pat, 'OK')
                output_report[pat] = "OK"
                out = r[0]
            os.makedirs(os.path.join(submission_file_path, output_path), exist_ok=True)
            wfile = open(os.path.join(submission_file_path, output_path, pat + '.txt'), 'w')
            wfile.write(out)
            wfile.close()
        except Exception as e:
            print(e)
            output_report["ERROR"] += str(e)
    return output_report


def extract_submissions(sub_path):
    report = {}
    dirs = get_dir(sub_path)
    for i in dirs:
        path = os.path.join(sub_path, i)
        id = get_id_from_path(i)
        r = extract(path)
        report[id] = r;

    output_report(report_name, report, sensitivity_words)


extract_submissions(submission_path)
