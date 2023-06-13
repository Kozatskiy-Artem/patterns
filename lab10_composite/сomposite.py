"""Implementation of the Composite pattern"""


from abc import ABC, abstractmethod


class FormComponent(ABC):
    @abstractmethod
    def render(self):
        pass


class Input(FormComponent):
    def __init__(self, name, input_type):
        self.name = name
        self.type = input_type

    def render(self):
        return f'<input name="{self.name}" type="{self.type}">'


class Select(FormComponent):
    def __init__(self, name):
        self.name = name
        self.options = []

    def add_option(self, option):
        self.options.append(option)

    def render(self):
        options_html = ''.join(f'<option>{option}</option>' for option in self.options)
        return f'<select name="{self.name}">{options_html}</select>'


class Fieldset(FormComponent):
    def __init__(self, legend):
        self.legend = legend
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def render(self):
        components_html = ''.join(component.render() for component in self.components)
        return f'<fieldset><legend>{self.legend}</legend>{components_html}</fieldset>'


if __name__ == '__main__':
    input1 = Input('name', 'text')
    input2 = Input('email', 'email')

    select = Select('country')
    select.add_option('USA')
    select.add_option('Canada')

    fieldset = Fieldset('Personal Info')
    fieldset.add_component(input1)
    fieldset.add_component(input2)
    fieldset.add_component(select)

    form = Fieldset('Registration Form')
    form.add_component(fieldset)

    print(form.render())
