import smtplib

class EmailSender(object):
    def __init__(self, gmail_sender_email, gmail_password):
        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.ehlo()
        self.server.starttls()
        self.gmail_sender_email = gmail_sender_email
        self.server.login(gmail_sender_email, gmail_password)

    def send_email(self, to_list, cc_list, subject_string, body_string):
        if not isinstance(to_list, list):
            raise TypeError("recipient must be a list.")
        if not isinstance(cc_list, list):
            raise TypeError("recipient must be a list.")

        header_list = []
        header_list.append(f"From: {self.gmail_sender_email}")
        header_list.append(f"To: {', '.join(to_list)}")
        if len(cc_list) > 0:
            header_list.append(f"CC: {', '.join(cc_list)}")
        header_list.append(f"Subject: {subject_string}")
        header_string = "\n".join(header_list)

        message = header_string + '\n' + body_string

        try:
            self.server.sendmail(
                self.gmail_sender_email,
                [addr.encode('ascii', 'ignore').decode('ascii') for addr in to_list],
                message.encode('utf-8')
            )
        except smtplib.SMTPRecipientsRefused:
            print(f"Invalid email address(es) {to_list}, skip")

    def __del__(self):
        self.server.close()
