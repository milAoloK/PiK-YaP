from abc import ABC, abstractmethod


class SendStrategy(ABC):
    @abstractmethod
    def execute(self, message: str) -> None:
        pass


class ImmediateStrategy(SendStrategy):
    def execute(self, message: str) -> None:
        print(f"Immediate send: {message}")


class DelayedStrategy(SendStrategy):
    def execute(self, message: str) -> None:
        print(f"Delayed send: {message}")
