import activity_browser as ab

from .plugin.layouts.tabs import LeftTab, RightTab
from .metadata import infos

class Plugin(ab.Plugin):

    def __init__(self):
        ab.Plugin.__init__(self, infos)

    def load(self):
        self.rightTab = RightTab(self)
        self.leftTab = LeftTab(self)
        self.tabs = [self.rightTab, self.leftTab]

    def close(self):
        return

    def remove(self):
        return

    def delete(self):
        return