from unittest.mock import Mock
from sender import NotificationSender
from strategy import SendStrategy


def test_strategy_execution_called():
    mock_strategy = Mock(spec=SendStrategy)
    sender = NotificationSender(mock_strategy)

    sender.send("Hello Strategy")

    mock_strategy.execute.assert_called_once_with("Hello Strategy")