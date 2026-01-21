import pytest
from pytest_bdd import scenario, given, when, then
from notifications import NotificationFactory


@scenario(
    "features/notification.feature",
    "Send email notification"
)
def test_send_email():
    pass


@pytest.fixture
def context():
    return {}


@given("a notification factory")
def given_factory(context):
    context["factory"] = NotificationFactory()


@when('I create an "email" notification')
def when_create_notification(context):
    factory = context["factory"]
    context["notification"] = factory.create("email")


@then("the notification should be sent successfully")
def then_send_notification(context):
    notification = context["notification"]
    assert notification.send("Hello BDD") is True