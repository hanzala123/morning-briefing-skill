from mycroft import MycroftSkill, intent_file_handler
from mycroft.messagebus import Message
from datetime import datetime

class MorningBriefing(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
    
    def initialize(self):
        self.userTitle = self.settings.get('userTitle', "sir")
        self.settings_change_callback = self.on_settings_changed
        self.on_settings_changed()

    def on_settings_changed(self):
        self.userTitle = self.settings.get('userTitle', "sir")

    
    @intent_file_handler('good.morning.intent')
    def handle_good_morning(self, message):
        
        if 'good morning' in message.data.get('utterance'):
            if datetime.now().hour < 13:
                self.speak_dialog('good.morning', dict(title=self.userTitle))
            else:
                self.speak_dialog('not.morning', dict(title=self.userTitle))
        self.bus.emit(Message("recognizer_loop:utterance",  
                          {'utterances': self.settings.get('actions').split(';'),  
                            'lang': 'en-us'}))


def create_skill():
    return MorningBriefing()

