"""Implementation of the Memento pattern for user profile settings"""


class Settings:
    def __init__(self):
        self.notifications = {}

    def enable_notification(self, notification_type):
        self.notifications[notification_type] = True

    def disable_notification(self, notification_type):
        self.notifications[notification_type] = False

    def create_memento(self):
        return SettingsMemento(self.notifications)

    def restore_from_memento(self, memento):
        self.notifications = memento.get_state()


class SettingsMemento:
    def __init__(self, state):
        self.state = state

    def get_state(self):
        return self.state


class SettingsCareTaker:
    def __init__(self):
        self.mementos = []

    def add_memento(self, memento):
        self.mementos.append(memento)

    def get_memento(self, index):
        return self.mementos[index]


class SettingsPage:
    def __init__(self, settings):
        self.settings = settings
        self.care_taker = SettingsCareTaker()
        self.current_memento_index = -1

    def enable_notification(self, notification_type):
        self.settings.enable_notification(notification_type)

    def disable_notification(self, notification_type):
        self.settings.disable_notification(notification_type)

    def apply_settings(self):
        memento = self.settings.create_memento()
        self.care_taker.add_memento(memento)
        self.current_memento_index += 1

    def undo_settings(self):
        if self.current_memento_index > 0:
            self.current_memento_index -= 1
            memento = self.care_taker.get_memento(self.current_memento_index)
            self.settings.restore_from_memento(memento)
