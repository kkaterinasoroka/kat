# math and memory game!!
basic.show_string("add the next two #s")
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
"""item1 = 29
basic.show_string("is the sum even or odd?")
if item1 % 0:
    basic.show_string("29 is not even")
else:
    basic.show_string("29 is odd!!")"""
#this sectioned out program doesn't stop the string until a button is pressed, try and fix.