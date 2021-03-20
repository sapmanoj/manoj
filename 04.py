import turtle

wn=turtle.Screen()
wn.title("Pong")
wn.bgcolor("blue")
wn.setup(width=800,height=600)
wn.tracer(0)


#paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("circle")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)



#paddle B



#ball
     


#main game loop
while True:
 wn.update()