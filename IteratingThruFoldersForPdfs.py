import os

def getPdfs(dirName):
    allPdfs = []
    for root, dirs, files in os.walk(dirName):
        for file in files:
            if file.endswith('.pdf'):
                allPdfs.append(file)
    return allPdfs

dirName = '.'
pdfs = getPdfs(dirName)
print(pdfs)