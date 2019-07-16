# 假设有这么一个请假系统：员工若想要请3天以内（包括3天的假），只需要直属经理批准就可以了；
# 如果想请3-7天，不仅需要直属经理批准，部门经理需要最终批准；
# 如果请假大于7天，不光要前两个经理批准，也需要总经理最终批准。
# 类似的系统相信大家都遇到过，那么该如何实现呢？首先想到的当然是if…else…，
# 但一旦遇到需求变动，其臃肿的代码和复杂的耦合缺点都显现出来。
# 简单分析下需求，“假条”在三个经理间是单向传递关系，像一条链条一样，因而，我们可以用一条“链”把他们进行有序连接。


class Request():
    def __init__(self, request_type, request_content, number_of_days):
        self.request_type = request_type
        self.request_content = request_content
        self.number_of_days = number_of_days


class Manager():
    def __init__(self, name):
        self.name = name

    def set_successor(self, successor):
        self.successor = successor

    def handle_request(self, request):
        pass


class LineManager(Manager):
    def handle_request(self, request):
        if request.request_type == "DaysOff" and request.number_of_days <= 3:
            print('%s:%s Num:%d Accepted OVER' %
                  (self.name, request.request_content, request.number_of_days))
        else:
            print('%s:%s Num:%d Accepted CONTINUE' %
                  (self.name, request.request_content, request.number_of_days))
            if self.successor is not None:
                self.successor.handle_request(request)


class DepartmentManager(Manager):
    def handle_request(self, request):
        if request.request_type == "DaysOff" and request.number_of_days <= 7:
            print('%s:%s Num:%d Accepted OVER' %
                  (self.name, request.request_content, request.number_of_days))
        else:
            print('%s:%s Num:%d Accepted CONTINUE' %
                  (self.name, request.request_content, request.number_of_days))
            if self.successor is not None:
                self.successor.handle_request(request)


class GeneralManager(Manager):
    def handle_request(self, request):
        if request.request_type == "DaysOff":
            print('%s:%s Num:%d Accepted OVER' %
                  (self.name, request.request_content, request.number_of_days))


if __name__ == "__main__":
    line_manager = LineManager("Line Manager")
    department_manager = DepartmentManager("Department Manager")
    general_manager = GeneralManager("General Manager")

    line_manager.set_successor(department_manager)
    department_manager.set_successor(general_manager)

    req = Request("DaysOff", "Ask 5 days off", 5)

    line_manager.handle_request(req)
