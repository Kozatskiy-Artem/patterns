from abc import ABC


class EntityUpdater(ABC):
    def update_entity(self, entity):
        self.validate_data(entity)
        self.prepare_request(entity)
        self.send_request(entity)
        self.handle_response(entity)

    def validate_data(self, entity):
    # Виконання валідації вихідних даних

    def prepare_request(self, entity):
    # Формування запиту на збереження інформації

    def send_request(self, entity):
    # Відправлення запиту

    def handle_response(self, entity):
    # Обробка отриманої відповіді

    def pre_update_hook(self, entity):
    # Хук, який можна перевизначити в підкласах для внесення змін перед оновленням сутності

    def post_update_hook(self, entity):
    # Хук, який можна перевизначити в підкласах для внесення змін після оновлення сутності


class ProductUpdater(EntityUpdater):
    def validate_data(self, product):
    # Виконання валідації даних товару

    def prepare_request(self, product):
    # Формування запиту на оновлення товару

    def send_request(self, product):
    # Відправлення запиту на оновлення товару

    def handle_response(self, product):
    # Обробка відповіді на оновлення товару

    def pre_update_hook(self, product):

    # Внесення змін перед оновленням товару

    def post_update_hook(self, product):
    # Внесення змін після оновлення товару


class UserUpdater(EntityUpdater):
    def validate_data(self, user):
    # Виконання валідації даних користувача

    def prepare_request(self, user):
    # Формування запиту на оновлення користувача

    def send_request(self, user):
    # Відправлення запиту на оновлення користувача

    def handle_response(self, user):
    # Обробка відповіді на оновлення користувача

    def pre_update_hook(self, user):
    # Внесення змін перед оновленням користувача

    def post_update_hook(self, user):
    # Внесення змін після оновлення користувача


class OrderUpdater(EntityUpdater):
    def validate_data(self, order):
    # Виконання валідації даних замовлення

    def prepare_request(self, order):
    # Формування запиту на оновлення замовлення

   def send_request(self, order):
    # Відправлення запиту на оновлення замовлення

    def handle_response(self, order):
    # Обробка відповіді на оновлення замовлення

    def pre_update_hook(self, order):
    # Внесення змін перед оновленням замовлення

    def post_update_hook(self, order):
    # Внесення змін після оновлення замовлення
