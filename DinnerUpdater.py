import appdaemon.plugins.hass.hassapi as hass
import csv
import random


#############################################
######   This script updates if:       ######
######   HA restarts                   ######
######   Changes are made to this file ######
#############################################

class DinnerUpdater(hass.Hass):
   def initialize(self):
      #Open menu file created by dinner_selector.py
    with open('/config/www/Dinners/Dinner_Menu.csv', newline='') as f:
         i = 1
         #assign each line to a day
         for row in f:
            if i == 1:
                Monday = row
            elif i == 2:
                Tuesday = row
            elif i == 3:
                Wednesday = row
            elif i == 4:
                Thursday = row
            elif i == 5:
                Friday = row
            elif i == 6:
                Saturday = row
            else:
                Sunday = row
            i = i +1
         # create the attributes to sensors in HA                
         self.set_state("sensor.monday_dinner", state=Monday, attributes={"friendly_name":"Mondays Dinner"})
         self.set_state("sensor.tuesday_dinner", state=Tuesday, attributes={"friendly_name":"Tuesdays Dinner"})
         self.set_state("sensor.wednesday_dinner", state=Wednesday, attributes={"friendly_name":"Wednesdays Dinner"})
         self.set_state("sensor.thursday_dinner", state=Thursday, attributes={"friendly_name":"Thursdays Dinner"})
         self.set_state("sensor.friday_dinner", state=Friday, attributes={"friendly_name":"Fridays Dinner"})
         self.set_state("sensor.saturday_dinner", state=Saturday, attributes={"friendly_name":"Saturdays Dinner"})
         self.set_state("sensor.sunday_dinner", state=Sunday, attributes={"friendly_name":"Sundays Dinner"})
