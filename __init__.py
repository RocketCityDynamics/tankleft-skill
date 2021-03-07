from mycroft import MycroftSkill, intent_file_handler


class Tankleft(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('tankleft.intent')
    def handle_tankleft(self, message):
        self.speak_dialog('tankleft')


def create_skill():
    return Tankleft()

