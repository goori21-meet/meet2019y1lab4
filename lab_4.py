import turtle
turtle.shape ('turtle')
finn=turtle.clone()
finn.shape('square')
finn.goto(100,100)
finn.goto(0,100)
finn.goto(0,0)
finn.goto(100,0)
finn.goto(100,100)
charlie=turtle.clone()
charlie.shape('triangle')
charlie.penup()
charlie.goto(200,0)
charlie.pendown()
charlie.goto(250,100)
charlie.goto(300,0)
charlie.goto(200,0)
finn.penup()
finn.goto(400,0)
finn.pendown()
finn.goto(450,0)
finn.stamp()
finn.goto(450,100)
turtle.mainloop()
