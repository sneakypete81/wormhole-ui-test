from clickshot import Region, ElementConfig

from .config import config


class ConnectDialog(Region):
    def is_visible(self):
        return self.label.is_visible()

    def wait_until_visible(self, timeout=None):
        self.label.wait_until_visible(timeout)


connect_dialog = ConnectDialog("connect_dialog", config)
