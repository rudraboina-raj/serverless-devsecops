import smtplib
import logging

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from shared.core.settings import Settings

logger = logging.getLogger(__name__)


class EmailService:

    # ==========================================================
    # Employee Created Email
    # ==========================================================

    @staticmethod
    def send_employee_created_email(employee):

        logger.info("=" * 60)
        logger.info("Starting Employee Email Service")
        logger.info("=" * 60)

        receiver = employee["email"]

        logger.info(f"SMTP_SERVER : {Settings.SMTP_SERVER}")
        logger.info(f"SMTP_PORT   : {Settings.SMTP_PORT}")
        logger.info(f"SMTP_EMAIL  : {Settings.SMTP_EMAIL}")
        logger.info(f"Receiver    : {receiver}")

        message = MIMEMultipart("alternative")

        message["Subject"] = "Welcome to TechMart"
        message["From"] = Settings.SMTP_EMAIL
        message["To"] = receiver

        html = f"""
        <html>
        <body style="font-family:Arial">

            <h2>Welcome to TechMart</h2>

            <p>Hello <b>{employee['first_name']} {employee['last_name']}</b>,</p>

            <p>Your employee account has been created successfully.</p>

            <table border="1" cellpadding="8">

                <tr>
                    <td><b>Employee ID</b></td>
                    <td>{employee['employee_id']}</td>
                </tr>

                <tr>
                    <td><b>Department</b></td>
                    <td>{employee['department']}</td>
                </tr>

                <tr>
                    <td><b>Designation</b></td>
                    <td>{employee['designation']}</td>
                </tr>

            </table>

            <br>

            <p>Regards,</p>

            <b>TechMart HR Team</b>

        </body>
        </html>
        """

        message.attach(MIMEText(html, "html"))

        try:

            logger.info("Connecting to Gmail SMTP...")

            with smtplib.SMTP(
                Settings.SMTP_SERVER,
                int(Settings.SMTP_PORT),
            ) as server:

                logger.info("SMTP connection established.")

                server.starttls()

                logger.info("TLS enabled.")

                server.login(
                    Settings.SMTP_EMAIL,
                    Settings.SMTP_PASSWORD,
                )

                logger.info("SMTP login successful.")

                server.sendmail(
                    Settings.SMTP_EMAIL,
                    receiver,
                    message.as_string(),
                )

                logger.info("Employee email sent successfully.")

        except Exception:

            logger.exception("Employee email sending failed.")

            raise

        logger.info("=" * 60)
        logger.info("Employee Email Service Finished")
        logger.info("=" * 60)

    # ==========================================================
    # Payment Completed Email
    # ==========================================================

    @staticmethod
    def send_payment_completed_email(payment):

        logger.info("=" * 60)
        logger.info("Starting Payment Email Service")
        logger.info("=" * 60)

        # Change this later if payment events contain customer email.
        receiver = Settings.SMTP_EMAIL

        logger.info(f"SMTP_SERVER : {Settings.SMTP_SERVER}")
        logger.info(f"SMTP_PORT   : {Settings.SMTP_PORT}")
        logger.info(f"SMTP_EMAIL  : {Settings.SMTP_EMAIL}")
        logger.info(f"Receiver    : {receiver}")

        message = MIMEMultipart("alternative")

        message["Subject"] = f"Payment Successful - {payment['payment_id']}"
        message["From"] = Settings.SMTP_EMAIL
        message["To"] = receiver

        html = f"""
        <html>
        <body style="font-family:Arial">

            <h2>Payment Completed Successfully</h2>

            <p>A payment has been processed successfully.</p>

            <table border="1" cellpadding="8">

                <tr>
                    <td><b>Payment ID</b></td>
                    <td>{payment['payment_id']}</td>
                </tr>

                <tr>
                    <td><b>Order ID</b></td>
                    <td>{payment['order_id']}</td>
                </tr>

                <tr>
                    <td><b>Amount</b></td>
                    <td>{payment['amount']}</td>
                </tr>

                <tr>
                    <td><b>Payment Method</b></td>
                    <td>{payment['payment_method']}</td>
                </tr>

                <tr>
                    <td><b>Status</b></td>
                    <td>{payment['status']}</td>
                </tr>

            </table>

            <br>

            <p>Regards,</p>

            <b>TechMart Payment Service</b>

        </body>
        </html>
        """

        message.attach(MIMEText(html, "html"))

        try:

            logger.info("Connecting to Gmail SMTP...")

            with smtplib.SMTP(
                Settings.SMTP_SERVER,
                int(Settings.SMTP_PORT),
            ) as server:

                logger.info("SMTP connection established.")

                server.starttls()

                logger.info("TLS enabled.")

                server.login(
                    Settings.SMTP_EMAIL,
                    Settings.SMTP_PASSWORD,
                )

                logger.info("SMTP login successful.")

                server.sendmail(
                    Settings.SMTP_EMAIL,
                    receiver,
                    message.as_string(),
                )

                logger.info("Payment notification email sent successfully.")

        except Exception:

            logger.exception("Payment email sending failed.")

            raise

        logger.info("=" * 60)
        logger.info("Payment Email Service Finished")
        logger.info("=" * 60)
