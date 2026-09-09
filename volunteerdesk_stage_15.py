# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: VolunteerDesk
class CommandDispatcher:
    def __init__(self):
        self._commands = {
            'shift': self._shift,
            'signup': self._signup,
            'hours': self._hours,
            'note': self._note,
            'help': self._help,
            'quit': self._quit,
        }

    def register(self, name, handler):
        self._commands[name] = handler

    def dispatch(self, text):
        text = text.strip().lower()
        for key, handler in self._commands.items():
            if text.startswith(key):
                return handler(text)
        return None

    def _shift(self, text):
        return f'Available shifts: {self._shifts()}'

    def _signup(self, text):
        return 'Sign up for a shift: shift_id, volunteer_name'

    def _hours(self, text):
        return 'Log hours: shift_id, hours, volunteer_name'

    def _note(self, text):
        return 'Leave a thank-you note: shift_id, message'

    def _help(self, text):
        return 'Commands: shift, signup, hours, note, help, quit'

    def _quit(self, text):
        return 'Goodbye!'

    def _shifts(self):
        return 'MORNING, AFTERNOON, EVENING'
