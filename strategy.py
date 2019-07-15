# 假设某司维护着一些客户资料，需要在该司有新产品上市或者举行新活动时通知客户。
# 现通知客户的方式有两种：短信通知、邮件通知。应如何设计该系统的客户通知部分？
# 为解决该问题，我们先构造客户类，包括客户常用的联系方式和基本信息，同时也包括要发送的内容。


class Customer():
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    def set_info(self, info):
        self.info = info

    def set_name(self, name):
        self.customer_name = name

    def set_brd_way(self, snd_way):
        self.snd_way = snd_way

    def snd_msg(self):
        self.snd_way.send(self.info)

# snd_way向客户发送信息的方式，该方式置为可设，即可根据业务来进行策略的选择。


class MsgSender():
    def set_code(self, code):
        self.dst_code = code

    def send(self, info):
        pass


class PhoneSender(MsgSender):
    def send(self, info):
        print("PHONE_NUMBER:%s EMAIL:%s" % (self.dst_code, info))


class EmailSender(MsgSender):
    def send(self, info):
        print("EMAIL_ADDRESS:%s EMAIL:%s" % (self.dst_code, info))


if __name__ == "__main__":
    customer_x = Customer()
    customer_x.set_name('Customer_x')
    customer_x.phone = '12345678'
    customer_x.email = '12345678@163.com'
    customer_x.set_info("Welcome!")

    phone_sender = PhoneSender()
    phone_sender.set_code(customer_x.phone)
    customer_x.set_brd_way(phone_sender)
    customer_x.snd_msg()

    email_sender = EmailSender()
    email_sender.set_code(customer_x.email)
    customer_x.set_brd_way(email_sender)
    customer_x.snd_msg()
