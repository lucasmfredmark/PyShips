#!/usr/bin/env python3

import tkinter
from classes.BattleshipsGame import BattleshipsGame

class Application(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.game = BattleshipsGame()
        self.initUI()

    def initUI(self):
        # constants
        BOARD_SIZE = 350
        TILE_COUNT = self.game.BOARD_SIZE
        TILE_BORDER = 1
        TILE_SIZE = (BOARD_SIZE / TILE_COUNT) - (TILE_BORDER / TILE_COUNT)

        # functions
        def click_tile(event):
            print(event.widget.find_closest(event.x, event.y)[0])

        # gui stuff
        self.parent.resizable(False, False)
        self.parent.title('Battleships Game')

        status_label = tkinter.Label(self.parent, text='Start new game', font=('Helvetica', 20), pady=10)
        canvas_1 = tkinter.Canvas(self.parent, width=BOARD_SIZE, height=BOARD_SIZE, highlightthickness=0)
        canvas_2 = tkinter.Canvas(self.parent, width=BOARD_SIZE, height=BOARD_SIZE, highlightthickness=0)
        #label = tkinter.Label(self.parent, text='Start new game', font=('Helvetica', 20), pady=10)

        # generate grids for both canvases
        for x in range(TILE_COUNT):
            for y in range(TILE_COUNT):
                c1_rect = canvas_1.create_rectangle(TILE_SIZE * x, TILE_SIZE * y, (TILE_SIZE * x) + TILE_SIZE, (TILE_SIZE * y) + TILE_SIZE, width=1, fill='#ddd', activefill='#eee')
                c2_rect = canvas_2.create_rectangle(TILE_SIZE * x, TILE_SIZE * y, (TILE_SIZE * x) + TILE_SIZE, (TILE_SIZE * y) + TILE_SIZE, width=1, fill='#ddd', activefill='#eee')
                canvas_1.tag_bind(c1_rect, '<ButtonPress-1>', click_tile)
                canvas_2.tag_bind(c2_rect, '<ButtonPress-1>', click_tile)

        status_label.pack()
        #label.pack(side='bottom')
        canvas_1.pack(side='left', padx=(10, 5))
        canvas_2.pack(side='right', padx=(5, 10))

def main():
    root = tkinter.Tk()
    Application(root)
    root.mainloop()

if __name__ == '__main__':
    main()
