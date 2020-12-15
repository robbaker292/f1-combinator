import csv
import pprint
import functools
import itertools
import sys

pp = pprint.PrettyPrinter(indent=4, depth=3)

races = set()
results = {}
cars = {}
unusualWins = []

#current F1 points - could update this for other points systems
points = [25,18,15,12,10,8,6,4,2,1]
# pre 2010 points
#points = [10, 8, 6, 5, 4, 3, 2, 1]


# convert the finishing position from the spreadsheet into a number of points
def formatPosition(position):
	if position == "DNF" :
		return (0, 21) # consider a DNF (or DNS, etc) to be a 21st place
	if position[-1] == "F" :
		if int(position[:-1]) > len(points) :
			return (0, int(position[:-1]))
		else :
			return (points[int(position[:-1])-1] + 1, int(position[:-1]) )
	else :
		if int(position) > len(points) :
			return (0, int(position))
		else :
			return (points[int(position)-1], int(position))

# calculate the total number of points per driver for the given season
def calculateRankings(combination, results):
	season = {x:results[x] for x in combination}
	seasonResults = {}
	for (race, results) in season.items() :
		for (car, (points, place)) in results.items() :
			# print(seasonResults)
			if car not in seasonResults:
				seasonResults[car] = {'points' : points, 'places' : [0]*21}
				seasonResults[car]['places'][place-1] = 1
			else :
				seasonResults[car]['points'] += points
				seasonResults[car]['places'][place-1] += 1
	return seasonResults

# Order the results by number of points, or countback if even
def orderResults(car1, car2):
	#print(car1, car1[1]['points'])
	if car1[1]['points'] > car2[1]['points'] :
		return -1
	elif car1[1]['points'] < car2[1]['points'] :
		return 1
	else :
		for i, place in enumerate(car1[1]['places']):
			if place > car2[1]['places'][i] :
				return -1
			elif place < car2[1]['places'][i] :
				return 1
			#else, continue
		return 0

# Check that there isn't a proper tie between the top two. This happens with short seasons
def checkForTie(sortedResults):
	rank1 = sortedResults[0][1]
	rank2 = sortedResults[1][1]

	if rank1['points'] != rank2['points'] :
		return False
	else :
		for i, place in enumerate(rank1['places']):
			#print(rank1['places'], place, i)
			if place > rank2['places'][i] or place < rank2['places'][i] :
				return False
		return True

# Format the total win length so it can be seen how many wins each driver has at a given length
def formatTotalLengthWins(totalLengthWins):
	for i, wins in enumerate(totalLengthWins):
		print("Season Length: " + str(i+1) + ". Winning drivers: " + str([(x,y) for (x,y) in wins.items() if y > 0]))


#read the spreadsheet
with open(sys.argv[1], newline='') as csvfile:
	resultsreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
	for row in resultsreader:
		race = row['race']
		row.pop("race")
		results[race] = {k:formatPosition(v) for (k,v) in row.items()}
		cars |= row.keys()
		races.add(race)

#save the total number of wins per driver and grouped by length
totalWins = {k:0 for k in cars}
totalLengthWins = [totalWins.copy() for i in range(0,len(results))]
ties = 0

#just for testing
print(races)
print(cars)
print(len(totalLengthWins))
driverList = list(cars)

with open('allseasons.csv', 'w', newline='') as csvfile:
	csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	csvwriter.writerow(["comb"] + driverList)

# create a number of seasons ranging from 1 race long to the full season
for i in range(1,len(results)+1) :
#for i in range(1,3) :
	combinations = list(itertools.combinations(results,i))
	#for each generated season
	for comb in combinations:
		seasonResults = calculateRankings(comb, results)
		sortedResults = sorted(seasonResults.items(), key=functools.cmp_to_key(orderResults))

		if checkForTie(sortedResults) :
			ties += 1
		else :
			driver = sortedResults[0][0]
			totalWins[driver] += 1 #update the total wins
			totalLengthWins[i-1][driver] += 1 #update the total wins by length

			#store the first 10 wins for each driver - this will show some interesting results
			# e.g. all the seasons Gasly won
			# Should save memory rather than saving all the results
			#if totalWins[sortedResults[0][0]] < 10 :
			#	unusualWins.append((sortedResults[0][0], comb))
			#if driver in ('SAI', 'GAS', 'STR', 'OCO'):
			#	unusualWins.append((sortedResults[0][0], comb))

		outputArr = [0] * (len(driverList)+1)
		outputArr[0] = "-".join(comb)
		for d in sortedResults :
			#print(driverList.index(d[0]), d[1]['points'])
			outputArr[driverList.index(d[0])+1] = d[1]['points']
		#print(outputArr)
		with open('allseasons.csv', 'a', newline='') as csvfile:
			csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			csvwriter.writerow(outputArr)

	print("Completed " + str(len(combinations)) + " seasons of length: " + str(i))

#Print some unusual wins
print("Unusual Wins:")
pp.pprint(unusualWins)

#print the total number of wins per driver
print("Total Wins by Length:")
formatTotalLengthWins(totalLengthWins)

#print the total number of wins per driver
print("Total Wins:")
pp.pprint(totalWins)

print("Ties:")
pp.pprint(ties)
