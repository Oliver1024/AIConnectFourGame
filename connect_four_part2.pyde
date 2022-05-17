from game_controller import GameController

SPACE = {'w': 700, 'h': 700}

gc = GameController(SPACE)


def setup():
    '''
    Set up the matrix
    None -> None
    '''
    size(SPACE['w'], SPACE['h'])
    colorMode(RGB, 1)


def draw():
    '''
    Starting drawing on the canvas
    None -> None
    '''
    background(0.5)
    if(mousePressed):
        gc.above_the_grid()
    gc.update()


def mousePressed():
    '''
    Handle the behavior when the mouse is pressed.
    None -> None
    '''
    gc.handle_mouse_press(mouseX, mouseY)


def mouseReleased():
    '''
    Handle the behavior when the mouse is released.
    None -> None
    '''
    gc.handle_mouse_release()
