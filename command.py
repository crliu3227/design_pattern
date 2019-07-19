# 大多数饭店中，当服务员已经接到顾客的点单，录入到系统中后，根据不同的菜品，会有不同的后台反应。
# 比如，饭店有凉菜间、热菜间、主食间，那当服务员将菜品录入到系统中后，凉菜间会打印出顾客所点的
# 凉菜条目，热菜间会打印出顾客所点的热菜条目，主食间会打印出主食条目。那么这个系统的后台模式该
# 如何设计？


# 可以将该系统设计成前台服务员系统和后台系统，后台系统进一步细分成主食子系统，凉菜子系统，热菜子系统。
# 后台三个子系统设计如下：
class BackSys():
    def cook(self, dish):
        pass


class MainFoodSys(BackSys):
    def cook(self, dish):
        print("MAINFOOD:Cook %s" % dish)


class CoolDishSys(BackSys):
    def cook(self, dish):
        print("COOLDISH:Cook %s" % dish)


class HotDishSys(BackSys):
    def cook(self, dish):
        print("HOTDISH:Cook %s" % dish)

# 前台服务员系统与后台系统的交互，我们可以通过命令的模式来实现，服务员将顾客的点单内容封装成命令，
# 直接对后台下达命令，后台完成命令要求的事，即可。前台系统构建如下：


class WaiterSys():
    def __init__(self):
        self.menu = dict()
        self.commandList = []

    def set_order(self, command):
        print("Waiter: Add dish")
        self.commandList.append(command)

    def cancel_order(self, command):
        print("Waiter: Cancel dish")
        self.commandList.remove(command)

    def notify(self):
        print("Waiter: Notify...")
        for command in self.commandList:
            command.execute()

# 前台系统中的notify接口直接调用命令中的execute接口，执行命令，命令类构建如下：


class Command():
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        pass


class FoodCommand(Command):
    def __init__(self, receiver, dish):
        super(FoodCommand, self).__init__(receiver)
        self.dish = dish

    def execute(self):
        self.receiver.cook(self.dish)


class MainFoodCommand(FoodCommand):
    pass


class CoolDishCommand(FoodCommand):
    pass


class HotDishCommand(FoodCommand):
    pass


# Command类是个比较通过的类，foodCommand类是本例中涉及的类，相比于Command类进行了一定的改造。
# 由于后台系统中的执行函数都是cook，因而在foodCommand类中直接将execute接口实现，
# 如果后台系统执行函数不同，需要在三个子命令系统中实现execute接口。
# 这样，后台三个命令类就可以直接继承，不用进行修改了。

class Menu():
    def __init__(self):
        self.menu = dict()

    def load_menu(self):
        self.menu["hot"] = ["Yu-Shiang Shredded Pork",
                            "Sauteed Tofu, Home Style", "Sauteed Snow Peas"]
        self.menu["cool"] = ["Cucumber", "Preserved egg"]
        self.menu["main"] = ["Rice", "Pie"]

    def is_hot(self, dish):
        return dish in self.menu["hot"]

    def is_cool(self, dish):
        return dish in self.menu["cool"]

    def is_main(self, dish):
        return dish in self.menu["main"]


if __name__ == "__main__":
    dishes = ["Yu-Shiang Shredded Pork",
              "Sauteed Tofu, Home Style", "Cucumber", "Rice"]

    waiter = WaiterSys()

    mainfood = MainFoodSys()
    cooldish = CoolDishSys()
    hotdish = HotDishSys()

    menu = Menu()
    menu.load_menu()

    for dish in dishes:
        if menu.is_main(dish):
            cmd = MainFoodCommand(mainfood, dish)
        elif menu.is_cool(dish):
            cmd = CoolDishCommand(cooldish, dish)
        elif menu.is_hot(dish):
            cmd = HotDishCommand(hotdish, dish)
        else:
            continue
        waiter.set_order(cmd)

    waiter.notify()
