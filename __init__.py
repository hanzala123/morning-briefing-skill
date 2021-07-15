from mycroft import MycroftSkill, intent_file_handler


class MorningBriefing(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('briefing.morning.intent')
    def handle_briefing_morning(self, message):
        self.speak_dialog('briefing.morning')


def create_skill():
    return MorningBriefing()

