This is a bit of fun with Terraform and Python to create a random animal with two random adjectives or adverbs. After the file is created it is then read and emailed to a Gmail account. Configure a .env file and set the following environment variables that are used for email credentials:

FROM_EMAIL="name of the user email you are sending from."

TO_EMAIL="name of the user email you are sending to."

PASSWORD="your FROM_EMAIL user's password for the email account."

Set these as environment variables in a .zshenv file or your preferred method of persisting environment variables.

Run everything at your desired time each day as a cronjob. Example:

0 15 * * * cd /Users/jameswurbel/SMTP_Dream_Date && python3 del_tfstate.py

0 16 * * * cd /Users/jameswurbel/SMTP_Dream_Date && bash animal_create.sh

1 16 * * * cd /Users/jameswurbel/SMTP_Dream_Date && python3 dream_date.py

