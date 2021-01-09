# math and memory game!!
item1 = randint(0,20)
item2 = randint(0,10) 
item3= item1 + item2
basic.show_number(item1)
basic.show_number(item2)

basic.show_string("add the next two numbers")
basic.show_number(16)
basic.show_number(23)
basic.show_string("if #: 28 press 'A'")
basic.show_string("if #: 29 press 'B'")
def on_button_pressed_a():
    basic.show_string("incorrect:(")
input.on_button_pressed(Button.A, on_button_pressed_a)
def on_button_pressed_b():
    basic.show_string("correct!")
input.on_button_pressed(Button.B, on_button_pressed_b)