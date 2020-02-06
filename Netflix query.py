import csv


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
for searcher in arr:
    num = timesWatched(arr,searcher)
    print(num)
    if num > mostInDay : 
        mostWatched = searcher
        mostInDay = num
print(mostWatched , num)

