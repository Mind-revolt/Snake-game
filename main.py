import turtle
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
# 1st step creating snake body

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')

# title method names a program

screen.title('Snake game')
# tracer is an animation that sets settings for animation
# to turn off the tracer write 0 in parentheses, to make animation update
# automatically with each step turn off the tracer.
screen.tracer(0)

# starting_positions = [(0, 0), (-20, 0), (-40, 0)]
# segments = []
# stamp method creates a copy of our instance
#                     snake.stamp()
#                     snake.color('white')
#                     snake.goto(-20, 0)
#                     snake.stamp()
#                     snake.color('white')
#                     snake.goto(-40, 0)

# First for loop is for creating starting body of snake
# for position in starting_positions:
#     new_segment = Turtle('square')
#     new_segment.color('white')
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)


# code after importing created Snake class

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


#     detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()
        print("nom nom nom")

#     detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    #  detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()

# let's create an infinite movement until the game is turned off
# while game_is_on:
#     # moving the body simultaneously requires to use an animation method
#     # called update
#     # place it before the for loop to move segments after it's complete
#     screen.update()
#     # delay the movement of the whole segment with sleep method
#     time.sleep(0.1)
# to move the snake we need a forwards call to repeat the segments
# so that the snake moves with its entire body

# 2nd step - Create movement
# to move the segments following the first segment link them from 3 to 2, from 2 to 1
# that way they will follow each other, So range should be in a reverse order
# for seg_num in range(len(segments) - 1, 0, -1):
#     # now we need two coordinates to which position each segment should go
#     # it has to be a position of the next segment. Last follows the second last, and second last follows first
#     new_x = segments[seg_num - 1].xcor()
#     new_y = segments[seg_num - 1].ycor()
#     segments[seg_num].goto(new_x, new_y)
# after the for loop of setting segments in following order
# we have to move the first segment
# segments[0].forward(20)
