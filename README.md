# Motivational Mailer

Motivational Mailer is a small Python application that sends a random motivational quote via email.
It is designed to be lightweight, easy to configure, and ideal for running as a scheduled task
(e.g. via cron on Linux or a Raspberry Pi).

The application reads quotes from a local JSON file, selects one quote at random, and sends it
using an SMTP mail server.

---

## How It Works

1. The application is started via `main.py`
2. A logger is initialized to record runtime information and errors
3. A JSON file containing motivational quotes is loaded
4. One quote is selected randomly
5. The quote is passed to the email client
6. The email client sends the quote via SMTP

The application exits immediately after sending the email, making it well suited for cron jobs.

---

## Configuration

Copy the example configuration files and adjust them to your needs:

```bash
cp config_example.py config.py
cp quotes_example.json quotes.json
```
- config.py contains SMTP settings, email addresses, and logging configuration
- quotes.json contains the motivational quotes used by the application

Example crontab entry to send a motivational quote every Monday at 8:00 AM:<br>
```bash
0 8 * * 1 /usr/bin/python3 /home/pi/motivational_mailer/main.py
```