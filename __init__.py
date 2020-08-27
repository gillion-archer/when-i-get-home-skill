from mycroft import MycroftSkill, intent_file_handler


class WhenIGetHome(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('home.get.i.when.intent')
    def handle_home_get_i_when(self, message):
        self.speak_dialog('home.get.i.when')


def create_skill():
    return WhenIGetHome()

