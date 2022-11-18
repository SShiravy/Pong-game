# Create the screen
# Create and move a paddle
# Create another paddle
# Create the ball and make it move
# Detect collision with wall and bounce
# Detect collision with paddle
# Detect with paddle misses
# Keep score

from turtle import Screen

from gamePlay import start_game

if __name__ == "__main__":
    screen = Screen()
    screen.bgcolor('black')
    screen.title("PONG")
    screen.setup(800, 600)
    screen.tracer(0)
    # ----
    start_game(screen)
    # ----
    screen.exitonclick()
