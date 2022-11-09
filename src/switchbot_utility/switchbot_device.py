import json

import requests

from .switchbot import Switchbot


class SwitchbotDevice(Switchbot):
    """Switchbot device class"""

    _body = {"commandType": "command", "parameter": "default"}
    _baseurl = "https://api.switch-bot.com/v1.1/devices/"

    def __init__(self, deviceId):
        """Constructor"""
        self.deviceId = deviceId

    def get_status(self):
        """Get device information"""
        header = self.gen_sign()
        response = requests.get(
            self._baseurl + self.deviceId + "/status",
            headers=header,
        )
        status = json.loads(response.text)
        return status["body"]

    def command(self, deviceId, body):
        """Send command"""
        header = self.gen_sign()
        return requests.post(
            self._baseurl + deviceId + "/commands",
            headers=header,
            data=json.dumps(body),
        )
