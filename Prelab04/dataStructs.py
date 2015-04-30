#!/usr/local/bin/python3.4
import glob
import sys
import filecmp

def getWordFrequency():
	#os.chdir("/mydir")
	dictionary = {}
	files = glob.glob('./files/*')
	for i in files:
		with open(i,"r") as readfile:
			for line in readfile:
				for word in line.split():
					length = len(word) 
					ch = word[length - 1]
					if ch < 'A' or (ch > 'Z' and ch < 'a' ) or ch > 'z':
						nwword = word[0:-1]
					else:
						nwword = word
					if nwword not in dictionary:
						dictionary[nwword] = 1
					else:
						dictionary[nwword] += 1
	return dictionary

def findCount( groupKey ):
	count = 0
	with open(groupKey, 'r') as inputFile:
		for line in inputFile:
			for word in line.split():
				count += 1
	return count

def checkDup( name, filenames ):
	group = [name[6:9]]
	for filename in filenames:
		if name != filename:
			if filecmp.cmp(name, filename):
				group.append(filename[6:9])

	list.sort(group)
	return group

def getDuplicates():
#Import filenames
	filenames = glob.glob('files/*.txt')

	groupDict = {}
	readNames = []

	for name in filenames:
		if name not in readNames:
			group = checkDup( name, filenames )
			readNames.append(group)
			length = len(group)

			if length > 1:
				groupKey = group[0]
				groupKeyPath = "files/%s.txt"%(groupKey)
				wordCount = findCount( groupKeyPath )
				groupTuple = ( wordCount, group )
				groupDict[groupKey] = groupTuple


	return groupDict

def getPurchaseReport():
	filenames = glob.glob('./purchases/*')
	items = []
	with open('purchases/Item List.txt', 'r') as itemList:
		for line in itemList:
			items.append(line)

	sumDict = {}
	for file in filenames:
		sum2 = 0
		with open( file, 'r' ) as inputFile:
			allLines = inputFile.readlines()
			transactionLines = allLines[2:]
			for line in transactionLines:
				parts = line.split()
				sum2 += float(parts[1])
#print file
		sumDict[file[19:22]] = float(sum2)
#print sumDict
	return sumDict

def makedic(filename):
	dicto = {}
	with open(filename,"r") as readfile:
		for line in readfile:
			splitline = line.split()
			if(len(splitline)) == 2:
				product = splitline[0]
				price = splitline[1]

				dicto[product] = price
	return dicto

def getTotalSold():
	dictionary = {}
	files = glob.glob('./purchases/*')
        files.remove('./purchases/Item List.txt')
	pricedict = makedic('./purchases/Item List.txt')
	keys = pricedict.keys()
	for each in keys:
		if each != "Name":
			sum2 = 0
			for name in files:
				purdict = makedic(name)

				if each in purdict:
					sum2 += int(purdict[each])
				
				dictionary[each] = sum2
	return dictionary

			

if __name__ == "__main__":

    #su = getWordFrequency()
    su2 = getPurchaseReport()
   

    print("addMultiplesOf : {0} ".format(su2))
