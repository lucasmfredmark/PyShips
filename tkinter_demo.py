#!/usr/bin/python3

import tkinter
#import game

class Application(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        # constants
        BOARD_SIZE = 350
        TILE_COUNT = 10
        TILE_BORDER = 1
        TILE_SIZE = (BOARD_SIZE / TILE_COUNT) - (TILE_BORDER / TILE_COUNT)

        # functions
        def click_tile(event):
            print(event.widget.find_closest(event.x, event.y)[0])

        self.parent.resizable(False, False)
        self.parent.title('Battleships Game')

        label = tkinter.Label(self.parent, text='Start new game', font=('Helvetica', 20), pady=10)
        label.pack()

        c1 = tkinter.Canvas(self.parent, width=BOARD_SIZE, height=BOARD_SIZE, highlightthickness=0)

        for x in range(TILE_COUNT):
            for y in range(TILE_COUNT):
                field = c1.create_rectangle(TILE_SIZE * x, TILE_SIZE * y, (TILE_SIZE * x) + TILE_SIZE, (TILE_SIZE * y) + TILE_SIZE, width=1, fill='#ddd', activefill='#eee')
                c1.tag_bind(field, '<ButtonPress-1>', click_tile)

        c2 = tkinter.Canvas(self.parent, width=BOARD_SIZE, height=BOARD_SIZE, highlightthickness=0)

        for x in range(TILE_COUNT):
            for y in range(TILE_COUNT):
                field = c2.create_rectangle(TILE_SIZE * x, TILE_SIZE * y, (TILE_SIZE * x) + TILE_SIZE, (TILE_SIZE * y) + TILE_SIZE, width=1, fill='#ddd', activefill='#eee')
                c2.tag_bind(field, '<ButtonPress-1>', click_tile)

        label = tkinter.Label(self.parent, text='Start new game', font=('Helvetica', 20), pady=10)
        label.pack(side='bottom')

        c1.pack(side='left', padx=(10, 5))
        c2.pack(side='right', padx=(5, 10))



        #for row in range(10):
            #for column in range(10):
                #button = tkinter.Button(self.parent, width=1, height=1, relief=tkinter.FLAT)
                #button.configure(text='O')
                #button.configure(command=clickButton(row, column))
                #button.grid(row=row, column=column)

        #canvas = tkinter.Canvas(self)
        #for row in range(10):
        #    for column in range(10):
        #        canvas.create_rectangle(row * 0, column * 0, row * 30, column * 30, width=1)
        #canvas.create_rectangle(150, 10, 240, 80, outline="#f50", fill="#f50")
        #canvas.create_rectangle(270, 10, 370, 80, outline="#05f", fill="#05f")
        #canvas.pack()

def main():
    root = tkinter.Tk()
    Application(root)
    root.mainloop()

if __name__ == '__main__':
    main()
