"""
Hey There! Here I have tried to create a simple snake game,
and I challenged myself to finish it in 10 mins.
I failed to do that.boomer :(......
But I completed this in about 18 mins.

"""

import random
import curses

#initializing the screen.
screen = curses.initscr() 

#setting curser to zero, so it doesn't bother us. :)
curses.curs_set(0)
screenHeight,screenWidth = screen.getmaxyx()
window = curses.newwin(screenHeight, screenWidth, 0, 0)
window.keypad(1)
window.timeout(100)


#Creating Snake
snake_x = screenWidth/4
snake_y = screenHeight/2

#Dimentions of the snake body (three tiles long)
snakeBody = [
    [snake_y, snake_x],
    [snake_y, snake_x-1],
    [snake_y, snake_x-2]
]

#creating the food , and fixing the starting place of the food at the middle of the window.

food = [screenHeight/2, screenWidth/2]

#ASC_PI helps us to use extended characters of curses libarary.
window.addch(int(food[0]), int(food[1]), curses.ACS_PI)

#We have to tell our little snake friend where he is going initially.
key = curses.KEY_RIGHT

# Now starting an infinite loop for every movement of the snake.

while True:
    next_key = window.getch() #check the next key
    key = key if next_key == -1 else next_key

    #condition for loosing the game [hitting the borders or bitting it self]
    if snakeBody[0][0] in [0, screenHeight] or snakeBody[0][1] in [0, screenWidth] or snakeBody[0] in snakeBody[1:]:
        curses.endwin()
        quit()
    
    new_head = [snakeBody[0][0], snakeBody[0][1]]


    # Defining the key movements.
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_DOWN:
        new_head[1] += 1

    snakeBody.insert(0, new_head)

    # Checking if snake got to the food. (Gotta give those points)
    if snakeBody[0] == food:
        food = None
        while food in None:
            newFood = [
                random.randint(1, screenHeight-1),
                random.randint(1, screenWidth-1)
            ]

            #Checking if food does not pop-up inside the snakeBody, and poping up new food on the screen
            food = newFood if newFood not in snakeBody else None
        
        window.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snakeBody.pop()
        window.addch(int(tail[0]), int(tail[1]), ' ')

    window.addch(int(snakeBody[0][0]), int(snakeBody[0][1]), curses.ACS_CKBOARD)    


        

