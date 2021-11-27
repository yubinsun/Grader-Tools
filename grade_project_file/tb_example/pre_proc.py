import re
import fileinput
import os

# get IF pipe instance name
if_pipe_ins_name = ""

if_pipe_ins_re = 'IF_pipe_stage\s*[a-zA-Z1-9_]+[\s\(]*'

result = "None"
with open("mips_32.v") as f:
    for line in f:
        result = re.match(if_pipe_ins_re,line.strip())
        # print(line)
        if result is not None:
            result = result[0]
            print(result)
            result = result.replace("IF_pipe_stage","",1).replace("(",'').strip(" ")
            break
print(result)
if_pipe_ins_name = result

if if_pipe_ins_name != "None":
    with fileinput.FileInput("tb_mips_32_grade.v", inplace=True) as file:
        for line in file:
            print(line.replace("#IFTOBEREPLACED#", if_pipe_ins_name), end='')
else:
    os.system("rm tb_mips_32_grade.v")


# Data mem instance name
data_mem_ins_name = ""
data_mem_re = 'data_memory\s*[a-zA-Z1-9_]+[\s\(]*'

result = "None"
with open("mips_32.v") as f:
    for line in f:
        result = re.match(data_mem_re,line.strip())
        # print(line)
        if result is not None:
            result = result[0]
            print(result)
            result = result.replace("data_memory","",1).replace("(",'').strip(" ")
            break
print(result)
data_mem_ins_name = result

if data_mem_ins_name != "None":
    with fileinput.FileInput("tb_mips_32_grade.v", inplace=True) as file:
        for line in file:
            print(line.replace("#DMTOBEREPLACED#", data_mem_ins_name), end='')
    with fileinput.FileInput("tb_mips_32_sw.v", inplace=True) as file:
        for line in file:
            print(line.replace("#DMTOBEREPLACED#", data_mem_ins_name), end='')
else:
    os.system("rm tb_mips_32_grade.v")
