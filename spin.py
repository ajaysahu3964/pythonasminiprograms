import turtle

T=turtle.turtle()
screen=turtle.screen()
screen.bgcolor('black')
T.Speed(0)
Screen.setup(700,700)

col=('yellow','red','cyan','purple')for c in range(450);
T.pencolor(col[c%4])
T.forward(c)
T.right(89)
T.forward(c*2)
T.right(89)