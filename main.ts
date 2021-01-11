//  math and memory game!!
basic.showString("add the next two #s")
basic.showNumber(16)
basic.showNumber(23)
basic.showString("if #: 28 press 'A'")
basic.showString("if #: 29 press 'B'")
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showString("incorrect:(")
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showString("correct!")
})
/** item1 = 29
basic.show_string("is the sum even or odd?")
if item1 % 0:
    basic.show_string("29 is not even")
else:
    basic.show_string("29 is odd!!")
 */
