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
def on_button_pressed_a():
    basic.show_string("yes! sum is even")
input.on_button_pressed(Button.A, on_button_pressed_a)
def on_button_pressed_a2():
    basic.show_string("yes! sum is odd")
input.on_button_pressed(Button.A, on_button_pressed_a2)