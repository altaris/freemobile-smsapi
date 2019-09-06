# freemobile-smsapi

![Python 3](https://badgen.net/badge/Python/3/blue)
[![MIT License](https://badgen.net/badge/license/MIT/blue)](https://choosealicense.com/licenses/mit/)

Python wrapper for the SMS API provided by [FreeMobile](http://mobile.free.fr/).

Before using this, you must activate the SMS notification service
(_Notifications par SMS_) on your [FreeMobile
account](https://mobile.free.fr/moncompte/).

Then, simply invoke `send_sms`:
```python
from freemobilesms import send_sms

send_sms(user, password, "Hello World!")
```

This method can raise the following exceptions:
* `MissingParameter` (HTTP error 400): Mandatory parameter is missing;
* `TooManySMS` (HTTP error 402): Too many SMSs have been sent too quickly;
* `ServiceNotEnabled` (HTTP error 403): SMS notification service has not been
  enabled for user;
* `ServerError` (HTTP error 500): Server error.

# TODOs

- [ ] Unicode support.
- [ ] What is the maximal message size?
