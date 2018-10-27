x = 0

def setup():
    global moon
    global landscape
    global right
    global left
    size(1366, 768)
    moon = loadImage("half_moon__.png")
    landscape = loadImage("halloween background.png")
    left = loadImage("left.png")
    right = loadImage("right.png")

def draw():
    global x
    image(landscape, x, 0)
    image(moon, 1200, 25, 150, 150)
    if x != 0:
        image(left, 10, 350, 100, 100)
    if x != -2655:
        image(right, 1256, 350, 100, 100)
    if x + 5 <= 0 and mouseX <= 110:
        x += 5
    if x - 5 >= -2655 and mouseX >= 1256:
        x -= 5
