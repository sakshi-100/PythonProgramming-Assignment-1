# Program that asks the user for their birth year and calculates their age
from datetime import date
 
def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
 
    return age
     
print(calculateAge(date(2004, 10, 22)), "years")