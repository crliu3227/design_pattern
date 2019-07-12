# 假设有一组火警报警系统，由三个子元件构成：一个警报器，一个喷水器，一个自动拨打电话的装置。其抽象如下：
class AlarmSensor():
    def run(self):
        print("Alarm Ring...")


class WaterSprinker():
    def run(self):
        print("Spray Water...")


class EmergencyDialer():
    def run(self):
        print("Dial 119...")


# 在业务中如果需要将三个部件启动，例如，如果有一个烟雾传感器，检测到了烟雾。在业务环境中需要做如下操作：
# if __name__ == "__main__":
#     alarm_sensor = AlarmSensor()
#     water_sprinker = WaterSprinker()
#     emergency_dialer = EmergencyDialer()
#     alarm_sensor.run()
#     water_sprinker.run()
#     emergency_dialer.run()


# 但如果在多个业务场景中需要启动三个部件，怎么办？Ctrl+C加上Ctrl+V虽然也是一个办法。。。
# 但作为码农的基本修养之一，减少重复代码是应该会被很轻易想到的方法。
# 这样，需要将其进行封装，在设计模式中，被封装成的新对象，叫做门面。门面构建如下：
class EmergencyFacade():
    def __init__(self):
        self.alarm_sensor = AlarmSensor()
        self.water_sprinker = WaterSprinker()
        self.emergency_dialer = EmergencyDialer()

    def run_all(self):
        self.alarm_sensor.run()
        self.water_sprinker.run()
        self.emergency_dialer.run()


if __name__ == "__main__":
    emergency_facade = EmergencyFacade()
    emergency_facade.run_all()
