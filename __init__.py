from mycroft import MycroftSkill, intent_file_handler
from mycroft.messagebus import Message
from datetime import datetime
from time import sleep

class MorningBriefing(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.actions = []
        self.userTitle = ''
    
    def initialize(self):
        self.userTitle = self.settings.get('userTitle', "sir")
        self.actions = self.settings.get('actions').split(';')
        self.settings_change_callback = self.on_settings_changed
        self.on_settings_changed()

    def on_settings_changed(self):
        self.userTitle = self.settings.get('userTitle', "sir")
        self.actions = self.settings.get('actions').split(';')

    
    @intent_file_handler('good.morning.intent')
    def handle_good_morning(self, message):
        
        if 'good morning' in message.data.get('utterance'):
            if datetime.now().hour < 13:
                self.speak_dialog('good.morning', dict(title=self.userTitle))
            else:
                self.speak_dialog('not.morning', dict(title=self.userTitle))
        for action in self.actions:
            self.log.info(action)
            if 'schedule' in action:
                self.bus.emit(Message("speak",  
                                {'utterance': 'Your schedule for today is',  
                                    'lang': 'en-us'}))
            self.bus.emit(Message("recognizer_loop:utterance",  
                            {'utterances': [action],  
                                'lang': 'en-us'}))
            sleep(7)


def create_skill():
    return MorningBriefing()

