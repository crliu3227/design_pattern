# 如果用过类似于Photoshop的平面设计软件，一定都知道图层的概念。
# 图层概念的提出，使得设计、图形修改等操作更加便利。
# 设计师既可以修改和绘制当前图像对象，又可以保留其它图像对象，逻辑清晰，且可以及时得到反馈。
from copy import copy, deepcopy


class SimpleLayer():
    def __init__(self):
        self.background = [0, 0, 0, 0]   # background表示背景RGBA元素
        self.content = "blank"   # content表示内容

    def get_content(self):
        return self.content

    def get_background(self):
        return self.background

    # 在前景上画画
    def paint(self, painting):
        self.content = painting

    # 设置透明度
    def set_parent(self, parent):
        self.background[3] = parent

    # 背景填充
    def fill_background(self, back):
        self.fill_background = back

    def clone(self):
        return copy(self)

    def deep_clone(self):
        return deepcopy(self)


# 新建图层，填充蓝底并画一只狗，简单表示
if __name__ == "__main__":
    doglayer = SimpleLayer()
    doglayer.paint('dog')
    doglayer.fill_background([0, 0, 255, 0])

    another_doglayer = doglayer.clone()

# 如果需要再生成一个同样的图层，再填充同样的颜色，再画一只同样狗，该如何做呢？
# 还是按照新建图层、填充背景、画的顺序么？
# 此时可以通过复制的方法来实现，而复制这个动作就是原型模式的精髓
# 但需要注意的是copy与deepcopy方法的不同
