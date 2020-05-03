import turtle

star = '*'
tstar =' '

for i in range(1,6):
    for j in range(5-i):
        print(tstar,end=' ')
    for x in range(2*i-1):
        print(star,end=' ')
    print();

t = turtle.Turtle()

len = 100
for x in range(1,6):
    for y in range(4):
        t.forward(len)
        t.left(72)

    t.forward(len)
t.hideturtle()
