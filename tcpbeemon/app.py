from . import handlers
from firenado import tornadoweb


class MonitorComponent(tornadoweb.TornadoComponent):

    def get_handlers(self):
        return [
            (r'/', handlers.IndexHandler),
            (r'/conf', handlers.ConfHandler),
            (r'/session', handlers.SessionHandler),
            (r'/sessions', handlers.SessionsHandler),
        ]
