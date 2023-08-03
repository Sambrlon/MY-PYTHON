class SMSSender():
    def send_sms(self, message):
        print("Отправляю смс на клюве голубя: ", message)

class PushSender():
    def send_push(self, message):
        print("Отправляю пуш уведомление для моей бэйбэ: ", message)

class MailSender():
    def send_mail(self, message):
        print("Кину смс по почте даже если ты не очень: ", message)

class SuperSender(SMSSender, PushSender, MailSender):
    def send_all(self, message):
        self.send_sms(message)
        self.send_push(message)
        self.send_mail(message)


sender = SuperSender()
sender.send_all("Владимирский централ ветер северный")
