from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# creating a snake
snake = Snake() 

# creating a food
food = Food()

# creating a scoreboard
scoreboard = Scoreboard()

# control snake movement
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

   
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # snake-food colision
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        scoreboard.point_gained()
        snake.extend()
        
    # wall colision detection
    if snake.snake_head.xcor() > 285 or snake.snake_head.xcor() < -285 or snake.snake_head.ycor() > 285 or snake.snake_head.ycor() < -285:
        is_game_on = False
        scoreboard.game_over()
      
    # tail colision detectio
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()
            
screen.exitonclick()