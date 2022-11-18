from .onoff_ability import OnOffAbility


class SwitchbotPlug(OnOffAbility):
    """Switchbot Plug class"""

    def __init__(self, deviceId):
        """Constructor"""
        super().__init__(deviceId)

    def get_power(self):
        """Returns device power status"""
        status = self.get_status()
        return status["power"]
