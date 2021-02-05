# from turtle import Turtle, Screen
#
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)
# myScreen = Screen()
# print(myScreen.canvheight)
# myScreen.exitonclick() #click to stop the program
#

# from prettytable import PrettyTable
# table_test = PrettyTable() #use PrettyTable class to create an object
# table_test.add_column("City name",["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
# table_test.align = "l"
# print(table_test)

from prettytable import from_csv
fp = open("test.csv", "r")
pt = from_csv(fp)
fp.close()
print(pt)