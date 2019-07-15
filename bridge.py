# 在一个画图程序中，常会见到这样的情况：有一些预设的图形，如矩形、圆形等，
# 还有一个对象-画笔，调节画笔的类型（如画笔还是画刷，还是毛笔效果等）并设定参数（如颜色、线宽等），
# 选定图形以及画笔，就可以在画布上画出想要的图形了。要实现以上需求，先从最抽象的元素开始设计，即形状和画笔


class Shape():
    def __init__(self, name, *param):
        pass

    def get_name(self):
        return self.name

    def get_param(self):
        return self.name, self.param


class Pen():
    def __init__(self, shape):
        self.shape = shape

    def draw(self):
        pass

# 形状对象和画笔对象是最为抽象的形式。接下来，构造多个形状，如矩形和圆形：


class Rectangle(Shape):
    def __init__(self, long, width):
        self.name = "Rectangle"
        self.param = "Long: %s Width: %s" % (long, width)
        print("Create a rectangle:%s" % self.param)


class Circle(Shape):
    def __init__(self, radius):
        self.name = "Circle"
        self.param = "Radius: %s" % radius
        print("Create a circle:%s" % self.param)

# 紧接着是构造多种画笔，如普通画笔和画刷：


class NormalPen(Pen):
    def __init__(self, shape):
        super(NormalPen, self).__init__(shape)
        self.type = "Normal Line"

    def draw(self):
        print("DRAWING %s: %s----PARAMS: %s" %
              (self.type, self.shape.get_name(), self.shape.get_param()))


class BrushPen(Pen):
    def __init__(self, shape):
        super(BrushPen, self).__init__(shape)
        self.type = "Brush Line"

    def draw(self):
        print("DRAWING %s: %s----PARAMS: %s" %
              (self.type, self.shape.get_name(), self.shape.get_param()))


if __name__ == "__main__":
    normal_pen = NormalPen(Rectangle("20cm", "10cm"))
    brush_pen = BrushPen(Circle("15cm"))
    normal_pen.draw()
    brush_pen.draw()
