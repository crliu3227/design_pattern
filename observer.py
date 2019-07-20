# 在门面模式中，提到过火警报警器，在当时，我们关注的是通过封装减少代码重复。
# 而今天，我们将从业务流程的实现角度，来再次实现该火警报警器。
# 门面模式中存在三个传感器类的结构，分别为报警器、洒水器和拨号器，这三者都是观察烟雾传感器来进行反应。
# 因此，他们三个都是观察者，而厌恶传感器则是被观察对象。
# 根据分析，将三各类提取共性，泛化出“观察者”：


class Observer():
    def update(self, action):
        pass

    def run(self):
        pass


class AlarmSensor(Observer):
    def update(self, action):
        print("Alarm Got: %s" % action)
        self.run()

    def run(self):
        print("Alarm Ring...")


class WaterSprinker(Observer):
    def update(self, action):
        print("Sprinker Got: %s" % action)
        self.run()

    def run(self):
        print("Spray Water...")


class EmergencyDialer(Observer):
    def update(self, action):
        print("Dialer Got: %s" % action)
        self.run()

    def run(self):
        print("Dial 119...")

# 下面构造被观察者


class Observerd():
    def __init__(self):
        self.observers = []
        self.action = ""

    def add_observer(self, observer):
        self.observers.append(observer)

    def set_action(self, action):
        self.action = action

    def notify(self):
        for ob in self.observers:
            ob.update(self.action)


class SmokeSensor(Observerd):
    def is_fire(self):
        return True


if __name__ == "__main__":
    alarm_sensor = AlarmSensor()
    water_sprinker = WaterSprinker()
    emergency_dialer = EmergencyDialer()

    smoke_sensor = SmokeSensor()
    smoke_sensor.add_observer(alarm_sensor)
    smoke_sensor.add_observer(water_sprinker)
    smoke_sensor.add_observer(emergency_dialer)

    smoke_sensor.set_action("Fire")

    if smoke_sensor.is_fire():
        smoke_sensor.notify()
