# 假设一个药房，有一些大夫，一个药品划价员和一个药房管理员，它们通过一个药房管理系统组织工作流程。
# 大夫开出药方后，药品划价员确定药品是否正常，价格是否正确；通过后药房管理员进行开药处理。该系统可以如何实现？


# 首先，构造药品类
class Medicine():
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def price(self):
        return self._price

    @name.setter
    def price(self, price):
        self._price = price

    def accept(self, visitor):
        pass

# 药品中有两个子类：抗生素、感冒药


class Antibiotic(Medicine):
    def accept(self, visitor):
        visitor.visit(self)


class Coldrex(Medicine):
    def accept(self, visitor):
        visitor.visit(self)


# 工作人员(visitor)分为划价员和药房管理员
class Visitor():
    def set_name(self, name):
        self.name = name

    def visit(self, medicine):
        pass


class Charger(Visitor):
    def visit(self, medicine):
        print("CHARGE: %s lists the Medicine %s. Price:%s " %
              (self.name, medicine.name, medicine.price))


class Pharmacy(Visitor):
    def visit(self, medicine):
        print("PHARMACY:%s offers the Medicine %s. Price:%s" %
              (self.name, medicine.name, medicine.price))


# 在药品类中，有一个accept方法，其参数是个visitor；而工作人员就是从Visitor类中继承而来的，
# 也就是说，他们就是Visitor，都包含一个visit方法，其参数又恰是medicine。药品作为处理元素，
# 依次允许（Accept）Visitor对其进行操作，这就好比是一条流水线上的一个个工人，对产品进行一次次的加工。
# 整个业务流程还差一步，即药方类的构建（流水线大机器）。
class Prescription():
    def __init__(self):
        self.medicines = []

    def add_medicine(self, medicine):
        self.medicines.append(medicine)

    def rm_medicine(self, medicine):
        self.medicines.append(medicine)

    def visit(self, visitor):
        for med in self.medicines:
            med.accept(visitor)


if __name__ == "__main__":
    yinqiao = Coldrex("YinQiao", 2.0)
    penicillin = Antibiotic("Penicillin", 3.0)

    prsrp = Prescription()
    prsrp.add_medicine(yinqiao)
    prsrp.add_medicine(penicillin)

    charger = Charger()
    charger.set_name("Doc.Strange")
    pharmacy = Pharmacy()
    pharmacy.set_name("Doc.Benedict")

    prsrp.visit(charger)
    prsrp.visit(pharmacy)
