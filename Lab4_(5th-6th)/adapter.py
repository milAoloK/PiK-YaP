from notifications import Notification
from third_party import ThirdPartyMessenger


class ThirdPartyAdapter(Notification):
    def __init__(self, messenger: ThirdPartyMessenger):
        self._messenger = messenger

    def send(self, message: str) -> bool:
        status = self._messenger.push(message)
        return status == 200
