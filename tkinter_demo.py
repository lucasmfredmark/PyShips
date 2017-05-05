#!/usr/bin/python3

import tkinter
#import game

def getCoordinates(x):
    print(x.widget.find_closest(x.x, x.y))

class Application(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title('Battleships Game')

        label = tkinter.Label(self.parent, text='Start new game', font=('Helvetica', 20), pady=10)
        label.pack()

        c1 = tkinter.Canvas(self.parent, width=350, height=350, highlightthickness=0)

        for x in range(10):
            for y in range(10):
                field = c1.create_rectangle(35 * x, 35 * y, 35 * x + 35, 35 * y + 35, width=1, fill='#ddd')
                c1.tag_bind(field, '<ButtonPress-1>', getCoordinates)

        c2 = tkinter.Canvas(self.parent, width=350, height=350, highlightthickness=0)
        c1.pack(side='left', fill='both', expand=True)
        c2.pack(side='right', fill='both', expand=True)

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
