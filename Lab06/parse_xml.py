#!/usr/local/bin/python3.4
import glob
import sys
import os
import filecmp
import re


def convertToAttrib():
    with open("points.xml","r") as f:
        lines = f.read()
    o = open("points_out.xml",'w', newline="\r\n")
    lines = lines.strip(" ")
    print(lines)
    ID = re.findall(r"<ID>(.*?)</ID>",lines)
    Y = re.findall(r"<Y>(.*?)</Y>",lines)
    X = re.findall(r"\s(([0-9]+).([0-9]*)|-.*)",lines)
    print(X)
    '''
    while(True):
        line = f.readline()
        if(line == ""):
            break
        pattern = "\<point\>"
        if(re.match(pattern,line)):
            while(not re.match("\<\/point\>",line)):
                line = f.readline()
                if(re.match("\<ID\>(\w+)\<\/ID\>",line)):
                    obj = re.match("\<ID\>(\w+)\<\/ID\>")
                    ID.append(obj.group(1))
                    '''


    o.write("<?xml version=\"1.0\"?>")
    o.write("\n<coordinates>")
    for i in range(0,len(ID)):
        o.write("\n<point ID=")
        o.write("\"")
        o.write(ID[i])
        o.write("\"")
        o.write(" ")
        o.write("X=")
        o.write("\"")
        o.write(X[i][0])
        o.write("\"")
        o.write(" ")
        o.write("Y=")
        o.write("\"")
        o.write(Y[i])
        o.write("\"")
        o.write("/>")
    o.write("\n</coordinates>")
    o.close()
    f.close()
    return


def getGenres():
    with open("books.xml","r") as f:
        lines = f.read()
    genre = re.findall(r"\<genre\>(.*?)\<\/genre\>",lines)
    genre.sort()
    genre_set = set(genre)
    list = [i for i in genre_set]
    list.sort()
    f.close()
    return list

def getAuthorOf(bookname):
    with open("books.xml","r") as f:
        lines = f.read()
    author = re.findall(r"<author>(.*?)</author>",lines)
    title = re.findall(r"<title>(.*?)</title>",lines)
    for i in range(0,len(author)):
        if(title[i] == bookname):
            return author[i]


    return

def getBookInfo(bookId):
    with open("books.xml","r") as f:
        lines = f.read()
    author = re.findall(r"<author>(.*?)</author>",lines)
    title = re.findall(r"<title>(.*?)</title>",lines)
    ID = re.findall(r"<book id=\"(.*?)\">",lines)
    for i in range(0,len(ID)):
        if(ID[i] == bookId):
            return (title[i],author[i])

    return None

def getBooksBy(authorname):
    with open("books.xml","r") as f:
        lines = f.read()
    author = re.findall(r"<author>(.*?)</author>",lines)
    title = re.findall(r"<title>(.*?)</title>",lines)
    ID = re.findall(r"<book id=\"(.*?)\">",lines)
    lis = []
    for i in range(0,len(author)):
        if(author[i] == authorname):
            lis .append(title[i])
    return (lis)

def getBooksBelow(bookPrice):
    with open("books.xml","r") as f:
        lines = f.read()
    author = re.findall(r"<author>(.*?)</author>",lines)
    title = re.findall(r"<title>(.*?)</title>",lines)
    price = re.findall(r"<price>(.*?)</price>",lines)
    ID = re.findall(r"<book id=\"(.*?)\">",lines)
    lis = []
    for i in range(0,len(author)):
        if(float(price[i]) < bookPrice):
            lis .append(title[i])
    return (lis)

def searchForWord(word):
    with open("books.xml","r") as f:
        lines = f.read()
    author = re.findall(r"<author>(.*?)</author>",lines)
    title = re.findall(r"<title>(.*?)</title>",lines)
    price = re.findall(r"<price>(.*?)</price>",lines)
    ID = re.findall(r"<book id=\"(.*?)\">",lines)
    lis = []
    for i in range(0,len(author)):
        if(float(price[i]) < bookPrice):
            lis .append(title[i])
    return (lis)

if __name__ == "__main__":
    convertToAttrib()
    getAuthorOf("Maeve Ascendant")
    getBookInfo("bk101")
    getBooksBy("Ralls, Kim")
    getBooksBelow(10)