import PyPDF2
name=input("Enter file name")
path=input("Enter path(no need to give the name and extension)")
pdfFileObj = open(path+name+'.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
page=pdfReader.numPages
file = open(name+'.txt', "a+")
for i in range(page):
    pageObj = pdfReader.getPage(i)
    convert=pageObj.extractText()
    file.write(convert)
file.close()
pdfFileObj.close()