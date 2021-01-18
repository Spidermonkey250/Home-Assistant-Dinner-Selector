import appdaemon.plugins.hass.hassapi as hass
import csv
import random
import datetime


    
class DinnerSelector(hass.Hass):
   def initialize(self):
    # Create a time object for 10:10am
      time = datetime.time(10, 10, 0)
    # Schedule a daily callback that will call run_daily() at 10:10am
      self.run_daily(self.run_daily_callback, time)

   def run_daily_callback(self, kwargs): 
      if datetime.date.today().isoweekday() == 6:
            #List of dinners to choose from
            with open(r'/config/www/Dinners/week_dinners.csv', 'r') as wd:
               reader = csv.reader(wd)
                #Randomly choose a dinner for Mon-Thurs & Sat (change to suit)
                # row.remove(day) removes the dinner from the list so it can't be chosen again during the script
               for row in reader:
                  Monday = (random.choice(row))
                  row.remove(Monday)
                  print (Monday)
                  Tuesday = (random.choice(row))
                  row.remove(Tuesday)
                  Wednesday = (random.choice(row))
                  row.remove(Wednesday)
                  Thursday = (random.choice(row))
                  row.remove(Thursday)
                  Saturday = (random.choice(row))
                  row.remove(Saturday)
            #List of takeaways to choose from
            with open(r'/config/www/Dinners/takeaway.csv', 'r', encoding="utf8") as ta:
               reader = csv.reader(ta)
               #Randomly choose a takeaway for friday
               for row in reader:
                  Friday = (random.choice(row))
            #List of sunday dinners to choose from
            with open(r'/config/www/Dinners/sunday_dinner.csv', 'r', encoding="utf8") as sd:
               reader = csv.reader(sd)
               #Randomly choose a dinner for Sunday
               for row in reader:
                  Sunday = (random.choice(row))
            #To ensure persitance of the sensors (if you have to restart HA), write the menu to Dinner_Menu.csv
            with open('/config/www/Dinners/Dinner_Menu.csv', 'w', encoding="utf8") as dm:
               # fields
               fields = ['dinner'] 
               #Create array of the menu selected and write it to file
               data = [
                {'dinner': Monday},
                {'dinner': Tuesday},
                {'dinner': Wednesday},
                {'dinner': Thursday},
                {'dinner': Friday},
                {'dinner': Saturday},
                {'dinner': Sunday}
               ]
               writer = csv.DictWriter(dm, fields)
               for row in data:
                writer.writerow(row)


