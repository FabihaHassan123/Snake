import pygame
import random

# Initialise Pygame
pygame.init()

FPS = 15
fpsClock = pygame.time.Clock()

# Boundary
boundaryR = 825
boundaryL = 0
boundaryT = 0
boundaryB = 600

# Set the screen size
screenSize = boundaryR, boundaryB

# Screen
screen = pygame.display.set_mode(screenSize)

# Colours
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
grey = (100, 100, 100)
pink = (219, 112, 147)
purple = (255, 50, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)

# Font
font = pygame.font.Font('freesansbold.ttf', 32)
bigfont = pygame.font.Font('freesansbold.ttf', 60)

# Snake variables
snakeSide = 15

body1 = [(375, 300, snakeSide, snakeSide), (390, 300, snakeSide, snakeSide), (405, 300, snakeSide, snakeSide),
         (420, 300, snakeSide, snakeSide), (435, 300, snakeSide, snakeSide), (450, 300, snakeSide, snakeSide)]
body2 = [(375, 360, snakeSide, snakeSide), (390, 360, snakeSide, snakeSide), (405, 360, snakeSide, snakeSide),
         (420, 360, snakeSide, snakeSide), (435, 360, snakeSide, snakeSide), (450, 360, snakeSide, snakeSide)]

direction1 = 0
direction2 = 0

# Mouse Variables
mouseX = 600
mouseY = 330


# Mouse Functions

def new_pos():
    """ Generate random coordinates for mouse """
    mouseX = random.randrange(0, boundaryR, 15)
    mouseY = random.randrange(0, boundaryB, 15)
    return mouseX, mouseY


def drawMouse(mouseX, mouseY):
    """ Draw mouse """
    pygame.draw.rect(screen, white, (mouseX, mouseY, 15, 15))
    pygame.draw.rect(screen, white, (mouseX+15, mouseY+8, 7, 7))
    pygame.draw.rect(screen, pink, (mouseX-15, mouseY+13, 15, 2))


# Winner screen
def winner(player):
    if player == "player2":
        screen.fill(black)
        for segment in body1:
            pygame.draw.rect(screen, grey, segment)
        drawMouse(mouseX, mouseY)
        Snake.drawSnake(snake2)
        win = bigfont.render("Yellow Wins!", True, green)
        screen.blit(win, (350, 250))

    if player == "player1":
        screen.fill(black)
        for segment in body2:
            pygame.draw.rect(screen, grey, segment)
        drawMouse(mouseX, mouseY)
        Snake.drawSnake(snake1)
        win = bigfont.render("Blue Wins!", True, green)
        screen.blit(win, (350, 250))


# Function to detect collisions
def collisions():
    snakeHead1 = body1[-1]
    snakeHead2 = body2[-1]
    snakeBody1 = body1[0:-1]
    snakeBody2 = body2[0:-1]

    if snakeHead1 in snakeBody1:
        winner("player2")
        return True
    elif snakeHead2 in snakeBody2:
        winner("player1")
        return True
    elif snakeHead1 in body2:
        winner("player2")
        return True
    elif snakeHead2 in body1:
        winner("player1")
        return True


# Function to draw grid
def drawGrid():
    for x in range(0, boundaryR, 15):
        for y in range(0, boundaryB, 15):
            pygame.draw.rect(screen, grey, (x, y, 15, 15), 1)


# Snake Class
class Snake(object):
    def __init__(self, colour, body):
        self.colour = colour
        self.body = body

    # Function to draw snake
    def drawSnake(self):
        for segment in self.body:
            pygame.draw.rect(screen, self.colour, segment)

    # Function to move snake
    def moveSnake(self, direction):
        headx = self.body[-1][0]
        heady = self.body[-1][1]

        if direction == "R":
            if headx != boundaryR - 15:
                self.body.append(((headx + 15), heady, snakeSide, snakeSide))
                if not Snake.eatMouse(self, mouseX, mouseY):
                    del self.body[0]
            else:
                self.body.append((boundaryL, heady, snakeSide, snakeSide))
                if not Snake.eatMouse(self, mouseX, mouseY):
                    del self.body[0]

        if direction == "L":
            if headx != boundaryL:
                self.body.append(((headx - 15), heady, snakeSide, snakeSide))
                if not Snake.eatMouse(self, mouseX, mouseY):
                    del self.body[0]
            else:
                self.body.append((boundaryR - 15, heady, snakeSide, snakeSide))
                if not Snake.eatMouse(self, mouseX, mouseY):
                    del self.body[0]

        if direction == "U":
            if heady != boundaryT:
                self.body.append((headx, (heady - 15), snakeSide, snakeSide))
                if not Snake.eatMouse(self, mouseX, mouseY):
                    del self.body[0]
            else:
                self.body.append((headx, boundaryB - 15, snakeSide, snakeSide))
                if not Snake.eatMouse(self, mouseX, mouseY):
                    del self.body[0]

        if direction == "D":
            if heady != boundaryB - 15:
                self.body.append((headx, (heady + 15), snakeSide, snakeSide))
                if not Snake.eatMouse(self, mouseX, mouseY):
                    del self.body[0]
            else:
                self.body.append((headx, boundaryT, snakeSide, snakeSide))
                if not Snake.eatMouse(self, mouseX, mouseY):
                    del self.body[0]

    # Function to eat mouse
    def eatMouse(self, mouseX, mouseY):
        headx = self.body[-1][0]
        heady = self.body[-1][1]
        snakeHead = (headx, heady)
        mouseB = (mouseX, mouseY)
        mouseH = (mouseX+15, mouseY)

        if snakeHead == mouseB or snakeHead == mouseH:
            return True


""" Main Loop"""

running = True
endgame = False

while running:

    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Arrow key player1 controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if direction1 == "R" or direction1 == 0:
                    pass
                else:
                    direction1 = "L"

            if event.key == pygame.K_RIGHT:
                if direction1 == "L":
                    pass
                else:
                    direction1 = "R"

            if event.key == pygame.K_UP:
                if direction1 == "D":
                    pass
                else:
                    direction1 = "U"

            if event.key == pygame.K_DOWN:
                if direction1 == "U":
                    pass
                else:
                    direction1 = "D"

            # WASD player2 controls
            if event.key == pygame.K_a:
                if direction2 == "R" or direction2 == 0:
                    pass
                else:
                    direction2 = "L"

            if event.key == pygame.K_d:
                if direction2 == "L":
                    pass
                else:
                    direction2 = "R"

            if event.key == pygame.K_w:
                if direction2 == "D":
                    pass
                else:
                    direction2 = "U"

            if event.key == pygame.K_s:
                if direction2 == "U":
                    pass
                else:
                    direction2 = "D"

    # Draw the mouse
    drawMouse(mouseX, mouseY)

    # Initialise and draw player1 snake
    snake1 = Snake(blue, body1)
    Snake.drawSnake(snake1)
    Snake.moveSnake(snake1, direction1)

    # Initialise and draw player2 snake
    snake2 = Snake(yellow, body2)
    Snake.drawSnake(snake2)
    Snake.moveSnake(snake2, direction2)

    # Detect if snake ate mouse
    if Snake.eatMouse(snake1, mouseX, mouseY) or Snake.eatMouse(snake2, mouseX, mouseY):
        mouseX, mouseY = new_pos()
        drawMouse(mouseX, mouseY)

    # Detect collisions and reset variables
    if collisions():
        direction1 = 0
        direction2 = 0
        body1 = [(375, 300, snakeSide, snakeSide), (390, 300, snakeSide, snakeSide), (405, 300, snakeSide, snakeSide),
                 (420, 300, snakeSide, snakeSide), (435, 300, snakeSide, snakeSide), (450, 300, snakeSide, snakeSide)]
        body2 = [(375, 360, snakeSide, snakeSide), (390, 360, snakeSide, snakeSide), (405, 360, snakeSide, snakeSide),
                 (420, 360, snakeSide, snakeSide), (435, 360, snakeSide, snakeSide), (450, 360, snakeSide, snakeSide)]
        mouseX = 600
        mouseY = 330

        # restart screen loop
        restart = font.render("Press space to restart", True, purple)
        screen.blit(restart, (150, 500))
        endgame = True

        while endgame:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        endgame = False

            pygame.display.update()

    pygame.display.update()
    fpsClock.tick(FPS)
pygame.quit()
quit()
