from ..core.object_base import scad_inline

class ScadInterface:
    def __init__(self):
        self.header = '\n'

    def register_customizer_var(self, name, value, options=''):
        self.header += f'{name} = {value}; //{options}\n'

    def set_global_var(self, name, value):
        self.header += f'{name} = {value};\n'

    def get_header_str(self):
        return self.header

    def register_font(self, filename):
        self.header += f'use <{filename}>\n'

    def additional_header_code(self, code):
        self.header += code + '\n'

    @staticmethod
    def get(name):
        return ScadInterface.inline(name)

    @staticmethod
    def inline(code):
        return scad_inline(code)

