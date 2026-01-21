import pytest
from notifications import NotificationFactory, EmailNotification, SMSNotification


def test_factory_creates_email_notification():
    notification = NotificationFactory.create("email")
    assert isinstance(notification, EmailNotification)


def test_factory_creates_sms_notification():
    notification = NotificationFactory.create("sms")
    assert isinstance(notification, SMSNotification)


def test_factory_raises_error_for_unknown_type():
    with pytest.raises(ValueError):
        NotificationFactory.create("push")
