from firenado import service
import firenado.conf
import logging

logger = logging.getLogger(__name__)


class SessionService(service.FirenadoService):

    def get_sessions(self):
        """

        :return:
        """
        return []


class ConfService(service.FirenadoService):

    def get_app_configuration(self):
        """ Return the application section configuration ready to be displayed
        in the template.
        :return:
        """
        conf = {}
        if firenado.conf.app['socket'] is None:
            conf['Addresses'] = firenado.conf.app['addresses']
            conf['Port'] = firenado.conf.app['port']
        else:
            conf['Socket'] = firenado.conf.app['socket']
        return conf
