import sys
import os
import fileinput

from label_data import labels

with open('latex-project.tex', 'r') as file:
    project = file.read();

with open('label-template.tex', 'r') as file:
    label_template = file.read();

label_source = ""

for label in labels:
    label_src = label_template
    label_src = label_src.replace('$NAME$', label.name)
    label_src = label_src.replace('$PIC$', label.pic)
    label_src = label_src.replace('$MIR_TYPE$', label.mir_type)
    label_src = label_src.replace('$MIR_ID$', label.mir_id)
    label_src = label_src.replace('$IP$', label.ip)
    label_src = label_src.replace('$WIFI$', label.wifi)
    label_source += label_src

label_source = label_source.replace('_','\_')
label_source = label_source.replace('%','\%')

project = project.replace('$LABEL_SOURCE$', label_source)

with open('output.tex', 'w') as file:
    file.write(project)

os.system("pdflatex output.tex && mv output.pdf labels.pdf && rm output.*")
