# 每一个公司都有自己的组织结构，越是大型的企业，其组织结构就会越复杂。
# 大多数情况下，公司喜欢用“树形”结构来组织复杂的公司人事关系和公司间的结构关系。
# 一般情况下，根结点代表公司的最高行政权利单位，分支节点表示一个个部门，而叶子结点则会用来代表每一个员工。
# 每一个结点的子树，表示该结点代表的部门所管理的单位。
# 假设一个具有HR部门，财务部门和研发部门，同时在全国有分支公司的总公司，其公司结构，
# 可以表示成如下逻辑：


class Company():
    def __init__(self, name):
        self.name = name

    def add(self, company):
        pass

    def remove(self, company):
        pass

    def display(self, depth):
        pass

    def list_duty(self):
        pass


class ConcreteCompany(Company):
    def __init__(self, name):
        super(ConcreteCompany, self).__init__(name)
        self.children_company = []

    def add(self, company):
        self.children_company.append(company)

    def remove(self, company):
        self.children_company.remove(company)

    def display(self, depth):
        print("-" * depth + self.name)
        for componment in self.children_company:
            componment.display(depth + 1)

    def list_duty(self):
        for componment in self.children_company:
            componment.list_duty()


class HRDepartment(Company):
    def __init__(self, name):
        super(HRDepartment, self).__init__(name)

    def display(self, depth):
        print("-" * depth + self.name)

    def list_duty(self):
        print('%s\t Enrolling & Transfering management.' % self.name)


class FinanceDepartment(Company):
    def __init__(self, name):
        super(FinanceDepartment, self).__init__(name)

    def display(self, depth):
        print("-" * depth + self.name)

    def list_duty(self):  # 履行职责
        print('%s\tFinance Management.' % self.name)


class RdDepartment(Company):
    def __init__(self, name):
        super(RdDepartment, self).__init__(name)

    def display(self, depth):
        print("-" * depth + self.name)

    def list_duty(self):
        print("%s\tResearch & Development." % self.name)


# 公司结构抽象仅考虑公司（ConcreteCompany）和部门（Department），公司有子公司的可能性，公司也有自己的部门，部门是最终的叶子结点。
# 假设总公司下设东边的分公司一个，东边的分公司下设东北公司和东南公司，显示公司层级，并罗列这些的公司中各部门的职责，可以构建如下业务场景：

if __name__ == "__main__":
    root = ConcreteCompany('HeadQuarter')
    root.add(HRDepartment('HQ HR'))
    root.add(FinanceDepartment('HQ Finance'))
    root.add(RdDepartment('HQ R&D'))

    east = ConcreteCompany('East Branch')
    east.add(HRDepartment('East HR'))
    east.add(FinanceDepartment('East Finance'))
    east.add(RdDepartment('East R&D'))
    root.add(east)

    northeast = ConcreteCompany('Northeast Branch')
    northeast.add(HRDepartment('Northeast HR'))
    northeast.add(FinanceDepartment('Northeast Finance'))
    northeast.add(RdDepartment('Northeast R&D'))
    east.add(northeast)

    southeast = ConcreteCompany('Southeast Branch')
    southeast.add(HRDepartment('Southeast HR'))
    southeast.add(FinanceDepartment('Southeast Finance'))
    southeast.add(RdDepartment('Southeast R&D'))
    east.add(southeast)

    root.display(1)

    root.list_duty()
