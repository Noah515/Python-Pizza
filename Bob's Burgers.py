cheese = 24.12;
pepperoni = 23.23;
hawaiian = 35.06;
total = 0.00;
DONE = False
print("""
+-------------------------------------------+
|Python Pizza |
+---------------------------------+---------+
| A\tCheese\tPizza                | $""" + str(cheese) + """  |
+---------------------------------+---------+
| B\tPepperoni Pizza            | $""" + str(pepperoni) + """   |
+---------------------------------+---------+
| C\tHawaiian Pizza            | $""" + str(hawaiian) + """    |
+---------------------------------+---------+
""");
while(not DONE):
     print("Total:", total);
     Item = input("Select a letter or type 'done': ");
     if Item is "A":
          total += cheese;
     elif Item is "B":
          total += pepperoni;
     elif Item is "C":
          total += hawaiian;
     elif Item is "done":
          print("Final total:", total);
          DONE = True



