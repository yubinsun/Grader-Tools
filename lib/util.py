# general util shared by modules

import os
import time


def get_dir(l = "."):
    dir = os.listdir(l)
    _dir = []
    for i in dir:
        if os.path.isdir(os.path.join(l,i)):
            _dir.append(i)
    return _dir

def get_id_from_path(pathname):
    student_id = pathname.split("_")[1]
    if student_id == "LATE":
        student_id = pathname.split("_")[2]
    return int(student_id)

def output_report(report_name, report, sensitive_words):
    # gradebook = { ID = {sensitive_words : data} }
    # export result
    try:
        file = open(report_name, 'w')
        file.write("ID")
        # write header
        for word in sensitive_words:
            file.write("," + word)
        file.write('\n')
        # body
        for i in report:
            # ID
            file.write(str(i))
            # fields according to sensitive words list
            for word in sensitive_words:
                if word in report[i]:
                    file.write(',' + str(report[i][word]))
                else:
                    file.write(',')
            file.write('\n')
    except Exception as e:
        print(e)
        print(report)
    finally:
        file.close()

def clear_screen():
    time.sleep(0.01)
    # for windows -- DO NOT USE
    if os.name == 'nt':
        _ = os.system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')