# Description: generate comments in batch.
# The output is formatted to be used by 
# 
# How to use: create "to_comments.csv" in the same folder,
# or change tha name and path of "input_filename" variable.
#
# The output file will be in key:value pair, and can be directly 
# used in the script to upload comments to canvas in batch.
# Key is the 6 digit canvas student id, and value is the comment for
# that student. 
# 
# Example Format of the input CSV:
# 
#       Name,ID,Project,Report,Comments
#       John Doe,252841,27,25,Missing waveforms and description of results for 9 new instructions.
#       Jane Doe,319623,70,30,
#
# Note for input file:
# ~ need to remove all "," comma in all column because it is a CSV.
# e.g. change "John, Doe" to "John Doe" in the name field. Same for the comments field.
# ~ The 'ID' field is reserved for key. It is the 6-digit "canvas student id", not the 
# 8-digit student ID. 

input_filename = "to_comments.csv"
rf = open(input_filename, encoding='utf-8-sig')
wf = open('comments.txt','w')

line = rf.readline()
print(line)
line = line.strip()
line = line.strip('\n')
line = line.strip('#')
line = line.split(',')
title = line
print(title)

for line in rf:
    line = line.strip('\n').replace('"', '')
    line = line.split(',')
    s = ''

    for (c,i) in enumerate(line):
        if (title[c] == 'ID'):
            id = i
            
        if ( i!='' and title[c]!='ID'):
            s+=(title[c]+":"+i+'; ')
    if id =='':
        continue
    s+= "Project is 70 points in total, and report is points in 30 total."
    s+= "Please contact me (yubins3@uci.edu) if you have any question.\",\n"
    s= '"'+id+'" : "'+s
    wf.write(s)
    print(s)

wf.close()
rf.close()

