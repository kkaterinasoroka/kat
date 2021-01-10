# math and memory game!!
item1 = randint(0,20)
item2 = randint(0,10) 
item3= item1 + item2
basic.show_number(item1)
basic.show_number(item2)
if item3 % 0:
   basic.show_string("if sum is even press 'A'") 
else:
    basic.show_string("if sum is odd press 'B'")
NExt I will use input and let the user press a or b
