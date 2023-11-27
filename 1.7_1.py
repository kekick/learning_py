from string import ascii_lowercase, digits

# здесь объявляйте классы TextInput и PasswordInput
class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits
    @classmethod
    def check_name(cls, name):
        if 3 > len(name) or len(name) > 50 or not all(map(lambda x: x in cls.CHARS_CORRECT, name)):
            raise ValueError("некорректное поле name")

    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size

    def get_html(self):
        html_str = f"<p class='login'>{self.name}: <input type='text' size={self.size} />"
        return html_str

class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    @classmethod
    def check_name(cls, name):
        if len(name) < 3 or len(name) > 50 or not all(map(lambda x: x in cls.CHARS_CORRECT, name)):
            raise ValueError("некорректное поле name")

    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size

    def get_html(self):
        html_str = f"<p class='password'>{self.name}: <input type='text' size={self.size} />"
        return html_str

class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Лf"), PasswordInput("Пароль"))
html = login.render_template()