from datetime import date, datetime, timedelta
import re


months = ['january', 'february', 'march', 'april', 
        'may', 'june', 'july', 'august', 'september',
        'october', 'november', 'december']

mainBlockWeeks = ["Recovery", "Build1", "Build2", "Key"]


## takes the input string of the date and extracts day and month (converts it to number) and year
def get_date(inputstr):
    Day = re.search("\d{1,2}", inputstr).group()
    
    Month = inputstr.split(' ')[3].lower()  
    Month = months.index(Month) + 1 
    
    Year = re.search("\d{4}", inputstr).group()
    
    return [int(Day), int(Month), int(Year)]

def add_day(date, day):
    return date + timedelta(days = day)
#Sunday 6th of June 2021
startDate = input("Enter The Start Date: ")

startDay, startMonth, startYear = get_date(startDate)

startDate = date(startYear, startMonth, startDay )
#Saturday 7th of August 2021
endDate = input("Enter The Race Date: ")

endDay, endMonth, endYear = get_date(endDate)
endDate = date(endYear, endMonth, endDay)
if endDate  < startDate :
    print("Error: Plan start date must be before Race Date.")
    exit()

endDate = endDate + timedelta(days = 1)   #adding one to endDay to include it in the calculation of the training duration
trainingWeeks = (endDate - startDate).days // 7
if trainingWeeks < 8 :
    print("Error: The number of training weeks is less than the minimum 8 weeks required.")
    exit()

#startDate = startDate + timedelta(days = (endDate - startDate).days % 7) # to make sure the number of weeks is integer

weekNumber = 1
extraWeeks = trainingWeeks % 4
weekStartDate = startDate
weekEndDate = add_day(startDate, 6)
testWeeks = 2
for i in range(testWeeks):
    print(f"Week #{weekNumber} - Test - from {weekStartDate.day} {weekStartDate.strftime('%B')} to {weekEndDate.day} {weekEndDate.strftime('%B')}")
    weekNumber += 1
    weekStartDate = add_day(weekStartDate, 7)
    weekEndDate = add_day(weekEndDate, 7)
    
#print(f"Week #{weekNumber} - Test - from {weekStartDate.day} {weekStartDate.strftime('%B')} to {weekEndDate.day} {weekEndDate.strftime('%B')}")
    
if(extraWeeks == 1):
    print(f"Week #{weekNumber} - Filler - from {weekStartDate.day} {weekStartDate.strftime('%B')} to {weekEndDate.day} {weekEndDate.strftime('%B')}")


mainBlockWeekCounter = 0
remainingWeeks = (endDate - weekStartDate).days / 7

if(extraWeeks == 2):
    mainBlockWeekCounter = 2
    
elif(extraWeeks == 3):
    mainBlockWeekCounter = 1
    
weekNumber += 1
weekStartDate = add_day(weekStartDate, 7)
weekEndDate = add_day(weekEndDate, 7)
    
while(remainingWeeks > 2):
    print(f"Week #{weekNumber} - {mainBlockWeeks[mainBlockWeekCounter]} - from {weekStartDate.day} {weekStartDate.strftime('%B')} to {weekEndDate.day} {weekEndDate.strftime('%B')}")
    weekNumber += 1
    mainBlockWeekCounter = mainBlockWeekCounter + 1 if mainBlockWeekCounter < 3 else 0

    weekStartDate = add_day(weekStartDate, 7)
    weekEndDate = add_day(weekEndDate, 7)
        
    remainingWeeks = (endDate - weekStartDate).days / 7
    
print(f"Week #{weekNumber} - Taper - from {weekStartDate.day} {weekStartDate.strftime('%B')} to {weekEndDate.day} {weekEndDate.strftime('%B')}")

weekStartDate = add_day(weekStartDate, 7)
weekEndDate = add_day(weekEndDate, 7)
weekNumber += 1
print(f"Week #{weekNumber} - Race - from {weekStartDate.day} {weekStartDate.strftime('%B')} to {weekEndDate.day} {weekEndDate.strftime('%B')}")
    

