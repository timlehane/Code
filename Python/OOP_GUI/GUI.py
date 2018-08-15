from tkinter import *

class Point(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def setX(self, x):
        self._x = x

    def setY(self, y):
        self._y = y

    def __str__(self):
        return "%d %d" % (self._x, self._y)

class Line(object):
    def __init__(self, ep1, ep2):
        self._ep1 = ep1
        self._ep2 = ep2

    def getEp1(self):
        return self._ep1

    def getEp2(self):
        return self._ep2

    def setEp1(self, ep1):
        self._ep1 = ep1

    def setEp2(self, ep2):
        self._ep2 = ep2

    def __str__(self):
        return "%d %d %d %d" % (self._ep1._x, self._ep1._y, self._ep2._x, self._ep2._y)

class View(object):

    def __init__(self):
        self._lineCollection = []

        root = Tk()

        frame = Frame(root)
        frame.pack()

        l1 = Label(frame, text="End Point 1 X")
        l1.grid(column="1", row="1")
        self._e1 = Entry(frame)
        self._e1.grid(column="1", row="2")

        l2 = Label(frame, text="End Point 1 Y")
        l2.grid(column="2", row="1")
        self._e2 = Entry(frame)
        self._e2.grid(column="2", row="2")

        l3 = Label(frame, text="End Point 2 X")
        l3.grid(column="1", row="3")
        self._e3 = Entry(frame)
        self._e3.grid(column="1", row="4")

        l4 = Label(frame, text="End Point 2 Y")
        l4.grid(column="2", row="3")
        self._e4 = Entry(frame)
        self._e4.grid(column="2", row="4")

        but = Button(frame, text="Draw", command=self.callback)
        but.grid(column="1", row="5")

        self._drawingspace = Canvas(root, bg="black", height=300, width=300)
        self._drawingspace.pack(side=TOP)

        root.mainloop()

    def redraw(self):
        self._drawingspace.delete(ALL)
        for line in self._lineCollection:
            start = line.getEp1()
            end = line.getEp2()
            self._drawingspace.create_line(start.getX(), start.getY(), end.getX(), end.getY(), fill="red")

    def callback(self):
        point1 = Point(self._e1.get(), self._e2.get())
        point2 = Point(self._e3.get(), self._e4.get())
        line = Line(point1, point2)
        self._lineCollection.append(line)
        self.redraw()

def main():
    app = View()

if __name__ == "__main__":
    main()
