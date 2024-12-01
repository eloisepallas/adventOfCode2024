
## -------- PART ONE ------------------------------------------------------------------------
# -----------------------------------------------------------------------
# listed by location ID
# pair smallest number in left list with smallest number in right list
# second smallest in left list with second smallest in right list etc
# -----------------------------------------------------------------------
locations = open("inputday1.txt", "r")
locData = locations.read()
#print(type(locData))

#print(locData)
locToList = locData.split()
print(type(locToList))

#List A
listLeft = []

#List B
listRight = []

# if i % 2  append to listA else append listB
# create 2 lists - listLeft and listRight
for i in range(len(locToList)):
    if i % 2 == 0:
        listLeft.append(int(locToList[i]))
    else:
        listRight.append(int(locToList[i]))

# make sure they return the correct stuff
# sort through list a and return smallest number
listLeft.sort()
listRight.sort()
# sort through list b and return smallest number
# distance from a to b return
differenceList = []

for i in range(len(listLeft)):
    # difference between listLeft listRight
    diff = abs(listLeft[i] - listRight[i])
    differenceList.append(diff)
    # append to list

# add all of the values from this list together
print(sum(differenceList))


## ----- PART TWO --------------------------------------------------------------
# new empty list
# for each element of listLeft look at i-th element in list. 
# duplicates = Determine how many of that i is in listRight
# Multiply i by  duplicates count
# Append this value to empty list

similarityScore = []

for i in range(len(listLeft)):
    duplicates = listRight.count(listLeft[i])
    print(duplicates)
    if duplicates != None:
        count = listLeft[i] * duplicates
        similarityScore.append(count)
print(sum(similarityScore))

#----------------------------------------------------------------------------------