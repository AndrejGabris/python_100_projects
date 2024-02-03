from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

R_PADDLE_START_POSITION = (350, 0)
L_PADDLE_START_POSITION = (-350, 0)

# screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


# paddles
r_paddle = Paddle(R_PADDLE_START_POSITION)
l_paddle = Paddle(L_PADDLE_START_POSITION)

# ball
ball = Ball()

# scoreboard
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")



is_game_on = True
while is_game_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)
    
    # wall colision detection    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    # right paddle colision detection
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x_to_left()
 
    # left paddle colision detection       
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:    
        ball.bounce_x_to_right()
        
    # left lost    
    if ball.xcor() < -380:
        r_paddle.goto(R_PADDLE_START_POSITION)
        l_paddle.goto(L_PADDLE_START_POSITION)
        ball.left_lost()
        scoreboard.r_point()
        
    # left lost    
    if ball.xcor() > 380:
        r_paddle.goto(R_PADDLE_START_POSITION)
        l_paddle.goto(L_PADDLE_START_POSITION)
        ball.right_lost()
        scoreboard.l_point()



screen.exitonclick()