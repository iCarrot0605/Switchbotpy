from SwitchbotStripLight import SwitchbotStripLight

class SwitchbotColorBulb(SwitchbotStripLight):
    """Constructor"""
    def __init__(self, deviceId):
        super().__init__(deviceId)

    def set_color_temperature(self, temperature):
        """Set color temperature"""
        body = {
            "commandType": "command",
            "command": "setColorTemperature",
        }
        body['parameter'] = temperature
        result = self.command(self.deviceId, body)
        return result.text

    def get_color_temperature(self):
        """Returns the color temperature value, range from 2700 to 6500"""
        status = self.get_status()
        return status['colorTemperature']