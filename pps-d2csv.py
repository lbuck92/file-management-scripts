# Data Import for PPS Experiment #2 Text File -> CSV File
# Takes in text file and puts data in SPSS-friendly CSV
# Last Update: 5/16/19; Author: Lauren E. Buck

import csv
import sys

fileName = "male-05.txt"
csvFile = "pps2-data.txt"
import_file = open(fileName, 'r')
export_file = open(csvFile, 'a+')
female = male = monster = ifemale = imale = False
avs = []
f = []
m = []
mo = []
ifm = []
im = []

def readFile():
    print("Reading file...")
    for n in import_file:
        if "Female-Regular" in n:
            female = True
        elif "Male-Regular" in n:
            male = True
        elif "Monster" in n:
            monster = True
        elif "Female-Intimidating" in n:
            ifemale = True
        elif "Male-Intimidating" in n:
            imale = True
        elif "Distance" in n:
            spltstr = n.split(" ")
            dn = spltstr[1]
            rt = spltstr[6]
            rt = rt[:-1]

            if female:
                f.extend((dn,rt))
            elif male:
                m.extend((dn,rt))
            elif monster:
                mo.extend((dn,rt))
            elif ifemale:
                ifm.extend((dn,rt))
            elif imale:
                im.extend((dn,rt))
            female = male = monster = ifemale = imale = False

    getAverages(f)
    getAverages(m)
    getAverages(mo)
    getAverages(ifm)
    getAverages(im)

def getAverages(arr):
    dist1 = dist2 = dist3 = dist4 = dist5 = 0

    for n in range(len(arr)):
        if arr[n] == "-0.7":
            dist1+=float(arr[n+1])
        elif arr[n] == "-1":
            dist2+=float(arr[n+1])
        elif arr[n] == "-1.2":
            dist3+=float(arr[n+1])
        elif arr[n] == "-1.5":
            dist4+=float(arr[n+1])
        elif arr[n] == "-2":
            dist5+=float(arr[n+1])

    dist1 = dist1/5
    dist2 = dist2/5
    dist3 = dist3/5
    dist4 = dist4/5
    dist5 = dist5/5

    avs.extend((dist1,dist2,dist3,dist4,dist5))

def dataToCSV():
    print ("Adding data to the file...")
    splt0 = fileName.split("-")
    splt1 = splt0[0]
    splt2 = splt0[1]
    splt2 = splt2[:-4]

    newRow = [splt2,splt1,avs[0],avs[1],avs[2],avs[3],avs[4],avs[5],avs[6],
    avs[7],avs[8],avs[9],avs[10],avs[11],avs[12],avs[13],avs[14],avs[15],
    avs[16],avs[17],avs[18],avs[19],avs[20],avs[21],avs[22],avs[23],avs[24]]
    with open(r'pps2-data.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(newRow)

def main():
    readFile()
    dataToCSV()

main()
