# Home-Assistant-Dinner-Selector
A method to choose your weekly evening meals from a list you define.

Firstly, a disclaimer. I am very new to Home Assistant and Python, so can only offer minimal help with this. My HA instnce is on a windows VM.

The evening meal selector was borne from being fed up of the weekly arguments of who has to decide on what to have for evening meals for the coming week.

Required steps:

1.  You must have Appdaemon running on your HA instance (Install through HA. Supervisor -> Add-Ons. ensure you follow the install instructions exactly).
2.  Ensure you put the .py files in the Appdaemon apps folder. The location of the .csv files is up to you, but ensure you change the location in the .py files.
3.  Place your meal choices in the relevant file. I have used:
    a.  sunday_dinner.csv   -   Us Brits love a good Sunday Roast
    b.  takeaway.csv        -   List all of your favorite takeaways in a single row.
    c.  week_dinners.csv    -   This is used Mon - Thurs & Sat.
    nb. The above can be changed as required
4.  As I do the shopping on a Saturday afternoon, the dinner_selector.py file will update in AppDaemon at 1010 on Saturday morning and writes the menu to Dinner_Menu.csv.
5.  DinnerUpdater uses Dinner_Menu to create sensors in HA, that can then be used in a card on lovelace.


