"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

Name: Audrey Tsang
This is a program for a Breakout game.
the breakoutgraphics.py creates the game window, paddle, bricks, and ball.
When mouse clicks, the game will start and if the ball hits bricks then user will get point.
If the ball jump out of window for three times, user will run out of lives, and game over.
In the end, it will show total scores and 'Game Over!' in the window.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width//2-ball_radius, y=window_height//2-ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Create a score board
        self.score = 0
        self.scoreboard = GLabel("Score:"+str(self.score), x=0, y=self.window.height-10)
        self.scoreboard.font = 'helvetica, -30'
        self.scoreboard.color = 'violet'
        self.window.add(self.scoreboard)
        # Initialize our mouse listeners
        onmouseclicked(self.set_ball_velocity)
        onmousemoved(self.move_paddle)
        self.switch = False
        self.number_bricks = brick_rows*brick_cols


        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                if i == 0:
                    self.brick.y = brick_offset
                else:
                    self.brick.y = i*(brick_height+brick_spacing)+brick_offset
                if j == 0:
                    self.brick.x = 0
                else:
                    self.brick.x = j*(brick_width+brick_spacing)
                if i < brick_rows//5:
                    self.brick_color = 'red'
                elif brick_rows//5 <= i < brick_rows//5*2:
                    self.brick_color = 'orange'
                elif brick_rows//5*2 <= i < brick_rows//5*3:
                    self.brick_color = 'yellow'
                elif brick_rows//5*3 <= i < brick_rows//5*4:
                    self.brick_color = 'green'
                else:
                    self.brick_color = 'blue'
                self.brick.filled = True
                self.brick.fill_color = self.brick_color
                self.brick.color = self.brick_color
                self.window.add(self.brick, x=self.brick.x, y=self.brick.y)

    #  Makes the paddle move with mouse
    def move_paddle(self, mouse):
        if mouse.x-self.paddle.width/2 < 0:
            self.paddle.x = 0
        elif mouse.x > self.window.width-self.paddle.width/2:
            self.paddle.x = self.window.width-self.paddle.width
        else:
            self.paddle.x = mouse.x-self.paddle.width/2

    #  When mouse clicks, creates a random velocity for the ball
    def set_ball_velocity(self, mouse):
        if not self.switch:
            self.switch = True
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self, new_dx):
        self.__dx = new_dx

    def set_dy(self, new_dy):
        self.__dy = new_dy

    #  Check if there is any collision and reacting depends on different objects
    def check_collisions(self):
        for neighbor_x in range(self.ball.x, self.ball.x+self.ball.width+1, self.ball.width):
            for neighbor_y in range(self.ball.y, self.ball.y+self.ball.height+1, self.ball.height):
                obj = self.window.get_object_at(neighbor_x, neighbor_y)
                if obj is not None:
                    if obj is self.paddle:
                        if self.__dy > 0:
                            self.__dy = -self.__dy
                            return
                    elif obj is self.scoreboard:
                        pass
                    else:
                        self.window.remove(obj)
                        self.score += 10
                        self.scoreboard.text = "Score:"+str(self.score)
                        self.__dy = -self.__dy
                        self.number_bricks -= 1
                        return

    #  When the ball fall out window, restart the game
    def reset_ball(self):
        self.window.add(self.ball, x=self.window.width//2-self.ball.width, y=self.window.height//2-self.ball.height)
        self.switch = False

    #  When running out of lives, the game ends
    def game_over(self):
        self.window.clear()
        end_game = GLabel("Game Over!", x=self.window.width/5, y=(self.window.height-50)/2)
        end_game.font = 'helvetica, -50'
        end_game.color = 'purple'
        self.window.add(end_game)
        self.window.add(self.scoreboard, x=(self.window.width-self.scoreboard.width)/2, y=self.window.height/2)
