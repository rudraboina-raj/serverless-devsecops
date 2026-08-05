from applications.notification_service.app.services.email_service import (
    EmailService,
)


class NotificationService:

    @staticmethod
    def send_employee_email(employee):

        EmailService.send_employee_created_email(employee)

    @staticmethod
    def send_payment_email(payment):

        EmailService.send_payment_completed_email(payment)
