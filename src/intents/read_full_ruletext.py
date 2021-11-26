def _read_full_ruletext(self, message):
        spell = message.data.get('spell')
        if spell is not None:
            self.speak_dialog('long.ruletext', {'spell': spell})
        else:
            self.speak_dialog('ruletext.fallback')