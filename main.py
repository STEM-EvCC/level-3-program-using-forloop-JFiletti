# Name: John Filetti 

# Program: LVL 3 with for loop

# Description: Program that iterates through three lists to calculate number of flights, 
# success rate, and flights that take place before 2000



mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

##variable declarations
goodFlight = 0 
flightPercentGood = 0
flightCount = 0
i = 0##input iterator
o = 0##output iterator

##list iterator
for (spaceFlight,flightYear,flightSuccess) in zip(mission_names, mission_years, mission_success) : 
    if flightSuccess == True : 
        goodFlight += 1
        flightCount += 1
    else :
        flightCount += 1
     
for (spaceFlight, flightYear) in zip(mission_names,mission_years) :
    
    if mission_years[i] >= 2000 :
        mission_names.pop(i)   
    
    i += 1
    
flightPercentGood = goodFlight / flightCount *100
##output to screen
print ("Total number of missions: "+str(flightCount))
print("Number of successful missions: "+str(goodFlight))
print(f"Success rate: {flightPercentGood:.2f}%")
print("Missions launched before the year 2000:")
for (spaceFlights) in zip(mission_names) :   
     print("- "+ str(mission_names[o])+ "\n")     
     o += 1

    

       
        

