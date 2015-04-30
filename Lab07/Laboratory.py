#!/usr/local/bin/python3.4
import glob
import sys
import os
import filecmp
import re
import math

class Experiment:
    def __init__(self,experimentNo,experimentDate,virusName,unitCount,unitCost):
        self.experimentNumber = int(experimentNo)
        self.experimentDate = experimentDate
        self.virusName = virusName
        self.unitCount = int(unitCount)
        self.unitCost = float(unitCost)
        a = float(unitCount)
        b = float(unitCost)
        self.totalCost = a*b


    def __str__(self):
        return ("{0:03d}, {1}, ${2:06.2f}: {3}".format(self.experimentNumber,self.experimentDate,self.totalCost,self.virusName))


class Technician:
    def __init__(self,techName,techID):
        self.techName = techName
        self.techID = techID
        self.experiments = {}

    def addExperiment(self,experiment):
        self.experiments[experiment.experimentNumber] = experiment

    def __str__(self):
        return("{0}, {1}: {2:02d} Experiments".format(self.techID,self.techName,len(self.experiments)))

    def generateTechActivity(self):
        string = "{0}, {1}\n".format(self.techID,self.techName)
        keylist = []
        new = []
        new = self.experiments.keys()
        for key in new:
            keylist.append(key)
        keylist.sort()
        for key in keylist:
            string += str(self.experiments[key])
            string += "\n"
        return string

    def loadExperimentsFromFile(self,fileName):
        with open(fileName,"r") as f:
            f.readline()
            f.readline()
            lines = f.readlines()

        for line in lines:
            string = line.split()
            self.addExperiment(Experiment(string[0],string[1],string[2],string[3],string[4][1:]))

class Laboratory:
    def __init__(self,labName):
        self.technicians = {}
        self.labName = labName

    def addTechnician(self,technician):
        self.technicians[technician.techName] = technician

    def __str__(self):
        string = "{0}, {1:02d} Technicians\n".format(self.labName,len(self.technicians))
        keylist = []
        new = []
        new = self.technicians.keys()
        for key in new:
            keylist.append(key)
        keylist.sort()
        for key in keylist:
            string += str(self.technicians[key])
            string += "\n"
        return string

    def generateLabActivity(self):
        string = ""
        keylist = []
        new = []
        new = self.technicians.keys()
        for key in new:
            keylist.append(key)
        keylist.sort()
        for key in self.technicians.keys():
            string += self.technicians[key].generateTechActivity()
            string += "\n"
        return string

if __name__ == "__main__":

    exp = Experiment(11,"04/01/2015","akskdfa",3,2)
    tech = Technician("hello",100)
    tech2 = Technician("hello",102)
    lab = Laboratory("hell")
    tech.loadExperimentsFromFile("report 55926-36619.txt")
    tech2.loadExperimentsFromFile("report 75471-28954.txt")
    print(tech.generateTechActivity())
    lab.addTechnician(tech)
    lab.addTechnician(tech2)
    print(lab)
    print(lab.generateLabActivity())
    """
    points =  PointSet()
    print(points.count())
    # print(Pset, Pset.count())
    Pset = PointSet()
    Pset.addPoint(Point3D())
    # print(Pset, Pset.count())
    Pset.addPoint(Point3D(1.2, 3.3, 4.5))
    # print(Pset, Pset.count())
    Pset.addPoint(Point3D(4.2, 2.1, 3.3))
    # print(Pset, Pset.count())
    Pset.addPoint(Point3D(4.4, 4.4, 4.4))
    #print(Pset, Pset.count())

    m =  Pset + Point3D(111.1, 222.2, 333.3)
    #print( m )
    m = Pset + PointSet( ({Point3D(10.1, 222.2, 333.3), Point3D(111.1, 0.2, 333.4), Point3D(111.1, 2.2, 3.3)}) )
    #print(m)
    m = Pset - Point3D(10.1, 222.2, 333.3)
    print(m)

    print("Pset is:\n", Pset)
    # below tests __init__ and __str__ functions
    # print(Point3D(1.1,2.2,3.0))
    # below tests "distFrom" function
    # print( Point3D(1.1,2.2,3.0).distFrom(Point3D(1.1,10.2,9.0)) )
    # below tests "nearestPoint" function
    # print( Point3D().nearestPoint( [Point3D(1.0, 0.0, 0.0), Point3D(0.0,2.2,0.0), Point3D(0.0,0.0,3.0), Point3D(0.1,0.2,0.3)] ) )
    # print( Point3D().nearestPoint( [] ) )
    # below tests "clone" function
    # print("\toriginal:{0}\n\tclone:{1}".format(Point3D(1.1,2.2,3.3) , Point3D(1.1,2.2,3.3).clone() ))
    a = Point3D(10.0, 2.0, 5.0)
    b = Point3D(8.0, 1.2, 4.5)
    c = a + -b
    print(a)
    print(b)
    # print(-b)
    print(c)
    print(a==b)
    print(a>b)
    print(a>=b)
    print(a<b)
    print(a<=b)
    # print(c*2)
    # print(2*c)
    # print(c/2)
    """