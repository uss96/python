# 거북이를 이용해 별모양을 그려보는 프로그램을 for문을 이용해 작성하자

import turtle

t = turtle.Pen()
t.shape('turtle')
for i in range (5):
    t.forward(50)
    t.right(145)


turtle.exitonclick()