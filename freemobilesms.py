# -*- coding: utf-8 -*-

import requests

SMSAPI_SENDMSG_URL = 'https://smsapi.free-mobile.fr/sendmsg'
"""URL of the ``sendmsg`` method."""

class MissingParameter(Exception):
    """HTTP error 400: Mandatory parameter is missing."""

class TooManySMS(Exception):
    """HTTP error 402: Too many SMSs have been sent too quickly."""

class ServiceNotEnabled(Exception):
    """HTTP error 403: SMS notification service has not been enabled for this
    user."""

class ServerError(Exception):
    """HTTP error 500: Server error."""

def send_sms(user: str, password: str, msg: str) -> None:
    """Sends a message."""
    response = requests.post(
        SMSAPI_SENDMSG_URL,
        json={
            "user": user,
            "pass": password,
            "msg": msg
        })
    error = {
        400: MissingParameter,
        402: TooManySMS,
        403: ServiceNotEnabled,
        500: ServerError
    }.get(response.status_code, None)
    if error:
        raise error
