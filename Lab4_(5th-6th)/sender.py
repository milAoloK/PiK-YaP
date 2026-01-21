from strategy import SendStrategy


class NotificationSender:
    def __init__(self, strategy: SendStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SendStrategy):
        self._strategy = strategy

    def send(self, message: str):
        self._strategy.execute(message)
