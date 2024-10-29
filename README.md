# SendEmails

## Sending emails to TML students

```python
pip install -r requirements.txt
cp .env.example .env
```

Then edit .env file: 
- `GMAIL_PASSWORD` will be provided by Joon; 
- `GSHEET_JSON` should indicate the path to the json file that Joon sends you; 
- `TEST_EMAIL`: when `DEBUG=True`, the code will send emails to `TEST_EMAIL`. You wanna put your personal email address here.

Inside `main_email_tml_students.py`, edit the following
- `TEMPLATE_TYPE`: See `util/email_templates.py` for more info. Feel free to add more templates.
- `FILTER_CONDITION`: This is google sheet column name for deciding whom to send the email to
- `FILTER_CONDITION_VALUE`: We send emails only to people with `FILTER_CONDITION` matching `FILTER_CONDITION_VALUE`.
- `EMAIL_KEY`: There may be multiple columns for emails. Choose which type of email to use.
- `DEBUG`: When True, it will send email to `TEST_EMAIL`. When False, it will send emails to respective email addresses in the column `EMAIL_KEY`.

To send emails, run:

```python
python main_email_tml_students.py
```

Enjoy!