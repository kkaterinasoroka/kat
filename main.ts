//  math and memory game!!
let item1 = randint(0, 20)
let item2 = randint(0, 10)
let item3 = item1 + item2
basic.showNumber(item1)
basic.showNumber(item2)
basic.showString("add the next two numbers")
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
