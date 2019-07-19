# 有一个手机仓储管理系统，使用者有三方：销售、仓库管理员、采购。需求是：
# 销售一旦达成订单，销售人员会通过系统的销售子系统部分通知仓储子系统，仓储子系统会将可出仓手机数量减少，同时通知采购管理子系统当前销售订单；
# 仓储子系统的库存到达阈值以下，会通知销售子系统和采购子系统，并督促采购子系统采购；
# 采购完成后，采购人员会把采购信息填入采购子系统，采购子系统会通知销售子系统采购完成，并通知仓库子系统增加库存。

# 从需求描述来看，每个子系统都和其它子系统有所交流，在设计系统时，如果直接在一个子系统中集成对另两个子系统的操作，
# 一是耦合太大，二是不易扩展。为解决这类问题，我们需要引入一个新的角色-中介者-来将“网状结构”精简为“星形结构”。


class Colleague():
    def __init__(self, mediator):
        self.mediator = mediator


class PurchaseColleague(Colleague):
    def buy_stuff(self, num):
        print("PURCHASE:Bought %s" % num)
        self.mediator.execute("buy", num)

    def get_notice(self, content):
        print("PURCHASE:Get Notice--%s" % content)


class WarehouseColleague(Colleague):
    def __init__(self, mediator):
        super(WarehouseColleague, self).__init__(mediator)
        self.total = 0
        self.low_threshold = 100

    def set_threshold(self, low_threshold):
        self.low_threshold = low_threshold

    def is_enough(self):
        if self.total < self.low_threshold:
            print("WAREHOUSE:Warning...Stock is low... ")
            self.mediator.execute("warning", self.total)
            return False
        return True

    def inc(self, num):
        self.total += num
        print("WAREHOUSE:Increase %s" % num)
        self.mediator.execute("increase", num)
        self.is_enough()

    def dec(self, num):
        if num > self.total:
            print("WAREHOUSE:Error...Stock is not enough")
        else:
            self.total -= num
            print("WAREHOUSE:Decrease %s" % num)
            self.mediator.execute("decrease", num)
        self.is_enough()


class SalesColleague(Colleague):
    def sell_stuff(self, num):
        print("SALES:Sell %s" % num)
        self.mediator.execute("sell", num)

    def get_notice(self, content):
        print("SALES:Get Notice--%s" % content)


# 当各个类在初始时都会指定一个中介者，而各个类在有变动时，也会通知中介者，由中介者协调各个类的操作。
# 中介者实现如下：
class ABCMediator():
    def __init__(self):
        self.purchase = ""
        self.sales = ""
        self.warehouse = ""

    def set_purchase(self, purchase):
        self.purchase = purchase

    def set_sales(self, sales):
        self.sales = sales

    def set_warehouse(self, warehouse):
        self.warehouse = warehouse

    def execute(self, content, num):
        pass


class StockMediator(ABCMediator):
    def execute(self, content, num):
        print("MEDIATOR:Get Info--%s" % content)
        if content == "buy":
            self.warehouse.inc(num)
            self.sales.get_notice("Bought %s" % num)
        elif content == "increase":
            self.sales.get_notice("Inc %s" % num)
            self.purchase.get_notice("Inc %s" % num)
        elif content == "decrease":
            self.sales.get_notice("Dec %s" % num)
            self.purchase.get_notice("Dec %s" % num)
        elif content == "warning":
            self.sales.get_notice("Stock is low.%s Left." % num)
            self.purchase.get_notice(
                "Stock is low. Please Buy More!!! %s Left" % num)
        elif content == "sell":
            self.warehouse.dec(num)
            self.purchase.get_notice("Sold %s" % num)
        else:
            pass


# 中介者模式中的execute是最重要的方法，它根据同事类传递的信息，直接协调各个同事的工作。
# 在场景类中，设置仓储阈值为200，先采购300，再卖出120，实现如下：
if __name__ == "__main__":
    mobile_mediator = StockMediator()

    mobile_purchase = PurchaseColleague(mobile_mediator)
    mobile_warehouse = WarehouseColleague(mobile_mediator)
    mobile_sales = SalesColleague(mobile_mediator)

    mobile_mediator.set_purchase(mobile_purchase)
    mobile_mediator.set_warehouse(mobile_warehouse)
    mobile_mediator.set_sales(mobile_sales)

    mobile_warehouse.set_threshold(200)
    mobile_purchase.buy_stuff(300)
    mobile_sales.sell_stuff(120)
