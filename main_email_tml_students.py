import logging
import os
import sys
from dotenv import load_dotenv
from util.gsheet import GSheetWithHeader
from util.email import EmailSender
from util.email_templates import TEMPLATES

load_dotenv()

TEMPLATE_TYPE = "Exercise0_grade"
FILTER_CONDITION = "Submit Ex0?"
FILTER_CONDITION_VALUE = "TRUE"
EMAIL_KEY = "Email"
DEBUG = True


def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', stream=sys.stdout)
    
    gsheet_reader = GSheetWithHeader(key_file=os.getenv('GSHEET_JSON'), doc_name=os.getenv('GSHEET_TITLE'), sheet_name=os.getenv('GSHEET_SHEET'))
    data_list = gsheet_reader.get_data_list()
    email_sender = EmailSender(gmail_sender_email=os.getenv('GMAIL_SENDER_EMAIL'),
                               gmail_password=os.getenv('GMAIL_PASSWORD'))

    total_rows = len(data_list)
    processed_rows = 0
    skipped_rows = 0

    for idx, row in enumerate(data_list):
        if row[FILTER_CONDITION] != FILTER_CONDITION_VALUE:
            logging.info(f"Skipped row {idx + 1}: Filter condition not met")
            skipped_rows += 1
            continue
        
        email_body = TEMPLATES[TEMPLATE_TYPE]["body"].format(**row)
        email_subject = TEMPLATES[TEMPLATE_TYPE]["subject"]
        logging.info(f"Processing row {idx + 1}: Sending email to {row[EMAIL_KEY]}")
        logging.info(f"Subject: {email_subject}")
        logging.info(email_body)
        
        email_sender.send_email(to_list=[os.getenv('TEST_EMAIL')] if DEBUG else [row[EMAIL_KEY]],
                                cc_list=[os.getenv('TEST_EMAIL')] if DEBUG else os.getenv('CC_EMAIL_LIST', '').split(','),
                                subject_string=email_subject,
                                body_string=email_body)
        processed_rows += 1
        logging.info(f"Finished processing row {idx + 1}")

    logging.info(f"Completed. Processed {processed_rows} rows, skipped {skipped_rows} rows, out of {total_rows} total rows.")


if __name__ == "__main__":
    main()
