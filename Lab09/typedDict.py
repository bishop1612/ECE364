#!/usr/local/bin/python3.4
import glob
import sys
import os
import filecmp
import re
import math

class Entry:
    def __init__(self,k=0,v=''):
        if(type(k) != int ):
            raise TypeError("k must be an integer")
        if(type(v) != str):
            raise TypeError("v must be a string")
        self.key = k
        self.value = v

    def __str__(self):
        return ("{0}: {1}".format(self.key,self.value))

    def __hash__(self):
        t = (self.key,self.value)
        return hash(t)

class Lookup:
    def __init__(self,name):
        if(name == ""):
            raise ValueError("name cannot be empty")
        self._name = name
        self._entrySet = set()

    def __str__(self):
        return ("{0}: {1} entries".format(self._name,len(self._entrySet)))

    def addEntry(self,entry):
        if entry not in  self._entrySet:
            self._entrySet.add(entry)
        else:
            raise ValueError("{0} exists".format(entry))

    def updateEntry(self,entry):
        if entry not in  self._entrySet:
            raise KeyError("{0} does not exist".format(entry))
        else:
            self._entrySet.remove(entry)
            self._entrySet.add(entry)

    def addOrUpdateEntry(self,entry):
        if entry not in  self._entrySet:
            self._entrySet.add(entry)
        else:
            self._entrySet.update(entry)

    def removeEntry(self,entry):
        if entry not in  self._entrySet:
            raise KeyError("{0} does not exist".format(entry))
        else:
            self._entrySet.remove(entry)

    def getEntry(self,key):
        c = 0
        for i in self._entrySet:
            if i.key == key:
                c = 1
                return i
        if c == 0 :
            raise KeyError("Key entry does not exist")

    def addOrUpdateFromDictionary(self,someDict):
        for key,value in someDict.items():
            exp = Entry(key,value)
            self.addOrUpdateEntry(exp)


    def getAsDictionary(self):
        newDict = {}
        for i in self._entrySet:
            newDict[i.key] = i.value
        return newDict

    def getKeys(self):
        keylist = []
        for i in self._entrySet:
            keylist.append(i.key)
        list = sorted(keylist)
        return list

    def getValues(self):
        keylist = []
        for i in self._entrySet:
            keylist.append(i.value)
        return sorted(keylist)

    def getElementCount(self):
        return len(self._entrySet)


if __name__ == "__main__":

    exp = Entry(11,"04/01/2015")
    lk = Lookup("04/01/2015")
    lk.addOrUpdateEntry(exp)
    print(lk.getEntry(11))
    print(lk)
    newDict = {}
    newDict[7] = "hello"
    newDict[5] = "2"
    lk.addOrUpdateFromDictionary(newDict)
    print(lk.getValues())