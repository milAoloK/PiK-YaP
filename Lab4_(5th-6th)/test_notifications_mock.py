from unittest.mock import Mock
from notifications import Notification


def test_notification_send_called():
    mock_notification = Mock(spec=Notification)

    mock_notification.send.return_value = True

    result = mock_notification.send("Hello")

    mock_notification.send.assert_called_once_with("Hello")
    assert result is True
