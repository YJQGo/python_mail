# import
from PyPDF2 import PdfFileReader as pdf_read, PdfFileWriter as pdf_write
import os
from tkinter import filedialog

# file-path
fileinfo = []
temp = filedialog.askopenfilename(title='打开要添加目录的pdf文件', filetypes=[('PDF', '*.pdf'), ('All Files', '*')],
                                  initialdir=os.getcwd() + '\\old-pdf')
fullFilepath = temp.replace('/', '\\')
fileinfo.append(fullFilepath)
file_name = fullFilepath.split('\\')[-1]
fileinfo.append(file_name)
filepath = fullFilepath.replace(file_name, '')
fileinfo.append(filepath)

temp = filedialog.askopenfilename(title='打开对应的目录文件', filetypes=[('TXT', '*.txt'), ('All Files', '*')],
                                  initialdir=os.getcwd() + '\\old-pdf')
fullFilepath = temp.replace('/', '\\')
fileinfo.append(fullFilepath)

readFile = fileinfo[0]
content = fileinfo[3]

# read-content
with open(content, 'r', encoding='utf-8') as f:
    directory_list = f.readlines()

# add-content
pdf_write = pdf_write()
with open(readFile, 'rb') as f:
    pdf = pdf_read(readFile)
    pages = pdf.getNumPages()
    # 将测试用.pdf里面的内容拷贝到pdf_write这个pdf对象中
    for i in range(pages):
        page_1 = pdf.getPage(i)
        pdf_write.addPage(page_1)

contentlist1 = []
contentlist2 = []
levelnum1 = 1
levelnum2 = 1

for item in directory_list:
    newitem = item.split()
    if int(newitem[0]) == 0:
        offset = int(newitem[1])
    else:
        level = int(newitem[0])
        title = newitem[1]
        pagenum = int(newitem[2])

        if level == 1:
            parent1 = pdf_write.addBookmark('Chap{}  '.format(levelnum1) + title, pagenum + offset)
            contentlist1.append(parent1)
            levelnum1 += 1
            levelnum2 = 1

        if level == 2:
            parent2 = pdf_write.addBookmark('{} - '.format(levelnum2) + title, pagenum + offset, contentlist1[-1])
            contentlist2.append(parent2)
            levelnum2 += 1

        if level == 3:
            pdf_write.addBookmark(title, pagenum + offset, contentlist2[-1])

with open(fileinfo[2] + fileinfo[1][0:-4] + '-带书签.pdf', 'wb+') as f:
    pdf_write.write(f)

os.startfile(fileinfo[2])
