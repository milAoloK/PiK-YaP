Feature: Notification sending

  Scenario: Send email notification
    Given a notification factory
    When I create an "email" notification
    Then the notification should be sent successfully
