import csv
import math

def timesWatched (theArray,search):
    timesFound = 0
    for counter in theArray:
        if counter == search :
            timesFound += 1
    return timesFound








watched = []
arr = []
with open('NetflixViewingHistory.csv') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")
    line_count = 0
    
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            arr.append(row[1])
            line_count += 1


mostWatched = ""
mostInDay = 0
increment = 0.25
checkpoint = math.floor(increment * len(arr))
counter = 0
print("|",end='')
for searcher in arr:
    num = timesWatched(arr,searcher)
    
    if num >= mostInDay : 
        mostWatched = searcher
        mostInDay = num
    
    if counter == checkpoint:
        print(".",end='')
        checkpoint += math.floor(increment * len(arr))
    
    counter += 1
print("|")
print("On the date:",mostWatched,"\nYou watched:",mostInDay,"episodes")