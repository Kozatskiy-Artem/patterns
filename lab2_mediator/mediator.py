"""Implementation of the Mediator pattern for order page"""


class OrderPageMediator:
    """Order page mediator"""
    def __init__(self, delivery_date_selector, recipient_info_section, self_pickup_section):
        self.delivery_date_selector = delivery_date_selector
        self.recipient_info_section = recipient_info_section
        self.self_pickup_section = self_pickup_section

        self.delivery_date_selector.set_mediator(self)
        self.recipient_info_section.set_mediator(self)
        self.self_pickup_section.set_mediator(self)

    def delivery_date_selected(self, date):
        self.delivery_date_selector.update_delivery_time_slots(date)

    def recipient_info_changed(self, is_other_person: bool):
        if is_other_person:
            self.recipient_info_section.enable_name_and_phone_fields()
        else:
            self.recipient_info_section.disable_name_and_phone_fields()

    def self_pickup_selected(self, is_self_pickup: bool):
        if is_self_pickup:
            self.self_pickup_section.disable_delivery_information()
        else:
            self.self_pickup_section.enable_delivery_information()


class BaseComponent:
    def __init__(self):
        self.mediator = None

    def set_mediator(self, mediator):
        self.mediator = mediator


class DeliveryDateSelector(BaseComponent):
    def select_date(self, date):
        self.mediator.delivery_date_selected(date)

    def update_delivery_time_slots(self, date):
        """Updating the list of available time slots depending on the selected date"""
        pass


class RecipientInformationSection(BaseComponent):
    def checkbox_changed(self, is_other_person: bool):
        self.mediator.recipient_info_changed(is_other_person)

    def enable_name_and_phone_fields(self):
        """Activation of the fields for entering the recipient's name and phone number"""
        pass

    def disable_name_and_phone_fields(self):
        """Deactivation of the fields for entering the recipient's name and phone number"""
        pass


class SelfPickupSection(BaseComponent):
    def checkbox_changed(self, is_self_pickup: bool):
        self.mediator.self_pickup_selected(is_self_pickup)

    def disable_delivery_information(self):
        """Deactivation of fields for entering delivery information"""
        pass

    def enable_delivery_information(self):
        """Activation of fields for entering delivery information"""
        pass
