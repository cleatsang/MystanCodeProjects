"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Name: Audrey Tsang
This is a program for a Breakout game, the breakout.py runs the game.
When mouse clicks, the game will start and if the ball hits bricks then user will get point.
If the ball jump out of window for three times, user will run out of lives, and game over.
In the end, it will show total scores and 'Game Over!' in the window.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics


FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts

#  Global variable
number_lives = NUM_LIVES


def main():
    number_lives = NUM_LIVES
    graphics = BreakoutGraphics()
    # Add the animation loop here!
    while True:
        dx = graphics.get_dx()
        dy = graphics.get_dy()
        #  Pause
        pause(FRAME_RATE)
        #  Check
        if number_lives > 0:
            graphics.ball.move(dx, dy)
            # If the ball falls under the bottom of window
            if graphics.ball.y > graphics.window.height:
                graphics.reset_ball()
                graphics.switch = False
                number_lives -= 1
                graphics.set_dx(0)
                graphics.set_dy(0)
            #  If the ball jumps out of window
            if graphics.ball.y <= 0:
                graphics.set_dy(-dy)
            if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width >= graphics.window.width:
                graphics.set_dx(-dx)
            #  Update
            graphics.check_collisions()
            if graphics.number_bricks == 0:
                graphics.game_over()
                break
        else:
            graphics.game_over()
            break


if __name__ == '__main__':
    main()
