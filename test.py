"""Test file.

Run as::

    USER=00000000 PASS=XXXXXXXXXXXXXX python3 test.py
"""

import os

from freemobilesms import send_sms


def main():
    """Main test function.

    Sends Hello World!"""
    user = os.environ.get("USER")
    password = os.environ.get("PASS")
    send_sms(user, password, "Hello World!")
    # send_sms(user, password, "Hello World! 👋")
    # send_sms(user, password, "今日は, 世界!")


if __name__ == '__main__':
    main()
