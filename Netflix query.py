import csv
import math

def timesWatched (arr,search):
    timesFound = 0
    for counter in arr:
        if counter == search :
            timesFound += 1
    return timesFound


def arrayGetter ():
    arr=[]
    with open('NetflixViewingHistory.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=",")
        line_count = 1
        
        for row in csv_reader:
            print(line_count, row[0])
            if line_count == 0:
                line_count += 1
            else:
                arr.append(row[0])
                line_count += 1
    return arr





watched = []
theArray = arrayGetter()


mostWatched = ""
mostInDay = 0
increment = 0.01
checkpoint = math.floor(increment * len(theArray))
counter = 0
print("|",end='')
for searcher in theArray:
    num = timesWatched(theArray,searcher)
    
    if num >= mostInDay : 
        mostWatched = searcher
        mostInDay = num
    
    if counter == checkpoint:
        print(".",end='')
        checkpoint += math.floor(increment * len(theArray))
    
    counter += 1
print("|")
print("On the date:",mostWatched,"\nYou watched:",mostInDay,"episodes")