import os

def getPdfs(dirName):
    allPdfs = [file for root, dirs, files in os.walk(dirName) for file in files if file.endswith('.pdf')]
    return allPdfs
    
dirName = '.'
pdfs = getPdfs(dirName)
print(pdfs)