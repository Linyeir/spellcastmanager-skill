def _read_short_ruletext(self, message):
        spell = message.data.get('spell')
        if spell is not None:
            self.speak_dialog('short.ruletext', {'spell': spell})
        else:
            self.speak_dialog('ruletext.fallback')