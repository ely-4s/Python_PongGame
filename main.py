from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game By Elyas Ahmadi ;)")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_padlle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_padlle.go_up, "w")
screen.onkey(l_padlle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    #detecting collision with the pabbles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_padlle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detecting r_padle misses
    if ball.xcor() >380:
        ball.reset_position()
        scoreboard.l_point()

    #detecting l_padle misses
    if ball.xcor() <-380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()