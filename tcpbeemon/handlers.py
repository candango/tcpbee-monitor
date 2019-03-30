from firenado import service, tornadoweb
from . import services


class ConfHandler(tornadoweb.TornadoHandler):

    conf_service: services.ConfService

    @service.served_by(services.ConfService)
    def get(self):
        conf = {
            'app': self.conf_service.get_app_configuration()
        }
        self.render("configuration.html", conf=conf)


class IndexHandler(tornadoweb.TornadoHandler):

    def get(self):
        self.render("index.html")


class SessionHandler(tornadoweb.TornadoHandler):

    def get(self):
        self.render("session.html")


class SessionsHandler(tornadoweb.TornadoHandler):

    def get(self):
        self.render("sessions.html")
