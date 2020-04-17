import turtle
t = turtle.Turtle()
t.shape('turtle')

list_color = []


list_color.append('red')
list_color.append('green')
list_color.append('blue')

t.begin_fill()
t.fillcolor(list_color[0])
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(200)
t.end_fill()

t.begin_fill()
t.fillcolor(list_color[1])
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(200)
t.end_fill()

t.begin_fill()
t.fillcolor(list_color[2])
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.end_fill()





test = []
test.append(int(input("국어 점수는: ")))

test.append(int(input("수학 점수는: ")))

test.append(int(input("영어 점수는: ")))

test.append(int(input("과학 점수는: ")))

test.append(int(input("사회 점수는: ")))

print("입력 자료: ",test)

test.sort()

ex = test

ex.reverse()

print("정렬 자료: ",ex)

final = sum(test)/5

print("평균 점수: ",final)


