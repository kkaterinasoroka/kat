//  math and memory game!!
let item1 = randint(0, 20)
let item2 = randint(0, 10)
let item3 = item1 + item2
basic.showNumber(item1)
basic.showNumber(item2)
if (item3 % 0) {
    basic.showString("if sum is even press 'A'")
} else {
    basic.showString("if sum is odd press 'B'")
}

