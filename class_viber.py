class Viber:
    MESSAGES = []

    @classmethod
    def add_message(cls, msg):
        cls.MESSAGES.append(msg)

    @classmethod
    def remove_message(cls, msg):
        cls.MESSAGES.remove(msg)

    @classmethod
    def set_like(cls, msg):
        if msg.fl_like:
            msg.fl_like = False
        else:
            msg.fl_like = True

    @classmethod
    def show_last_message(cls, count):
        print(len(cls.MESSAGES))
        if count <= len(cls.MESSAGES):
            for i in range(-1, -count-1, -1):
                print(cls.MESSAGES[i].message, end=' ')
            print()

    @classmethod
    def total_messages(cls):
        return len(cls.MESSAGES)


class Message:

    def __init__(self, text):
        self.message = text
        self.fl_like = False


msg_1 = Message("Hello")
msg_2 = Message("Hello")

Viber.add_message(msg_1)
Viber.add_message(msg_2)

Viber.show_last_message(2)

print(Viber.MESSAGES[0].fl_like)
