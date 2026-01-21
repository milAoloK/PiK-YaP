from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> bool:
        pass


class EmailNotification(Notification):
    def send(self, message: str) -> bool:
        # имитация отправки email
        print(f"Email sent: {message}")
        return True


class SMSNotification(Notification):
    def send(self, message: str) -> bool:
        # имитация отправки sms
        print(f"SMS sent: {message}")
        return True


class NotificationFactory:
    @staticmethod
    def create(notification_type: str) -> Notification:
        if notification_type == "email":
            return EmailNotification()
        if notification_type == "sms":
            return SMSNotification()
        raise ValueError("Unknown notification type")
