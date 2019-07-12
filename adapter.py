# 假设某公司A与某公司B需要合作, A公司和B公司接口分别如下：
class StaffInA():
    def __init__(self, id, name="", phone=""):
        self._id = id
        self._name = name
        self._phone = phone

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone


class StaffInB():
    def __init__(self, id, name="", telephone=""):
        self._id = id
        self._name = name
        self._telephone = telephone

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    def telephone(self, telephone):
        self._telephone = telephone


# 此时A公司要访问B公司数据但接口不一样（A为phone，B为telephone）
# 若直接调用，但会对现在业务流程造成不确定的风险。为减少耦合，规避风险，我们需要一个帮手，就像是转换电器电压的适配器一样，
# 这个帮手就是协议和接口转换的适配器。
class AdapterB():
    def __init__(self, staff_in_B):
        self.adapter = staff_in_B

    @property
    def name(self):
        return self.adapter.name

    @name.setter
    def name(self, name):
        self.adapter.name = name

    @property
    def phone(self):
        return self.adapter.telephone

    @phone.setter
    def phone(self, phone):
        self.adapter.telephone = phone


# 适配器将B公司人员接口封装，而对外接口形式与A公司人员接口一致，达到用A公司人员接口访问B公司人员信息的效果。
if __name__ == "__main__":
    staff_A = StaffInA("123456")
    staff_A.name = "LCR"
    staff_A.phone = "87654321"
    print("Staff name: %s\tStaff phone: %s" % (staff_A.name, staff_A.phone))

    staff_B = AdapterB(StaffInB("234567"))
    staff_B.name = "XXD"
    staff_B.phone = "98765432"
    print("Staff name: %s\tStaff phone: %s" % (staff_B.name, staff_B.phone))
