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
        self._isfirstclick = True
        self._point1 = None
        self._point2 = None

        root = Tk()

        self._drawingspace = Canvas(root, bg="black", height=300, width=300)
        self._drawingspace.pack(side=TOP)

        self._drawingspace.bind("<Button-1>", self.callback)

        button = Button(root, text="Start Again", command=self.clearall)
        button.pack(side=BOTTOM)

        root.mainloop()

    def redraw(self):
        self._drawingspace.delete(ALL)
        for line in self._lineCollection:
            start = line.getEp1()
            end = line.getEp2()
            self._drawingspace.create_line(start.getX(), start.getY(), end.getX(), end.getY(), fill="red")

    def clearall(self):
        self._drawingspace.delete(ALL)
        self._lineCollection = []

    def callback(self, event):
        if self._isfirstclick:
            self._point1 = Point(event.x, event.y)
            self._isfirstclick = False
        else:
            self._point2 = Point(event.x, event.y)
            line = Line(self._point1, self._point2)
            self._lineCollection.append(line)
            self.redraw()
            self._isfirstclick = True

def main():
    app = View()

if __name__ == "__main__":
    main()
