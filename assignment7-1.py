import turtle
#1번
t=turtle.Turtle()
t.shape('turtle')

def cCircle(r):
    t.penup()
    t.goto(0,-r)
    t.pendown()
    t.circle(r)
    t.penup()
    t.goto(0,0)
    t.pendown()
    return r

print(cCircle(100))
print(cCircle(70))
print(cCircle(40))
