# 假设有一个网上咖啡选购平台，客户可以在该平台上下订单订购咖啡，平台会根据用户位置进行线下配送。
# 假设其咖啡对象构造如下：


class Coffee():
    def __init__(self, name):
        self.name = name
        # 在实际业务中，咖啡价格应该是由配置表进行配置，或者调用接口获取等方式得到，
        # 此处为说明享元模式，将咖啡价格定为名称长度，只是一种简化
        self.price = len(name)

    def show(self):
        print("Coffee Name:%s Price:%s" % (self.name, self.price))

# 其对应的顾客类如下：


# class Customer():
#     def __init__(self, name):
#         self.name = name

#     def order(self, coffee_name):
#         print("%s ordered a cup of coffee:%s" % (self.name, coffee_name))
#         return Coffee(coffee_name)


# 按照一般的处理流程，用户在网上预订咖啡，其代表用户的Customer类中生成一个Coffee类，直到交易流程结束,整个流程是没有问题的。
# 如果，随着网站用户越来越多，单位时间内购买咖啡的用户也越来越多，并发量越来越大，对系统资源的消耗也会越来越大，
# 极端情况下，会造成宕机等严重后果。此时，高效利用资源，就显得非常重要了。
# 简单分析下业务流程，高并发下用户数量增加，而该模型下，每个用户点一杯咖啡，就会产生一个咖啡实例，
# 如果一种咖啡在该时间内被很多用户点过，那么就会产生很多同样咖啡的实例。避免重复实例的出现，是节约系统资源的一个突破口。
# 类似于单例模式，我们这里在咖啡实例化前，增加一个控制实例化的类：咖啡工厂。
class CoffeeFactory():
    def __init__(self):
        self.coffee_dict = {}

    def get_coffee(self, name):
        if name not in self.coffee_dict.keys():
            self.coffee_dict[name] = Coffee(name)
        return self.coffee_dict[name]

    def get_coffee_count(self):
        return len(self.coffee_dict)

# 重写Customer


class Customer():
    def __init__(self, name, coffee_factory):
        self.name = name
        self.coffee_factory = coffee_factory

    def order(self, coffee_name):
        print("%s ordered a cup of coffee:%s" % (self.name, coffee_name))
        return self.coffee_factory.get_coffee(coffee_name)


# 假设业务中短时间内有多人订了咖啡，业务模拟如下：
if __name__ == "__main__":
    coffee_factory = CoffeeFactory()

    customer1 = Customer("customer1", coffee_factory)
    customer2 = Customer("customer2", coffee_factory)
    customer3 = Customer("customer3", coffee_factory)

    c1 = customer1.order("cappuccino")
    c2 = customer2.order("mocha")
    c3 = customer3.order("cappuccino")

    c1.show()
    c2.show()
    c3.show()

    print("Num of Coffee Instance:%s" % coffee_factory.get_coffee_count())
