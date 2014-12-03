from nose.plugins import Plugin

try:
    from django import setup as setup_django
except ImportError:
    setup_django = lambda: None


class DjangoNosePlugin(Plugin):
    ''' Adaptor that allows usage of django_nose package plugin from
    the nosetests command line.
    Imports and instantiates django_nose plugin after initialization
    so that the django environment does not have to be configured
    when running nosetests -p '''

    name = 'djangonose'
    enabled = False

    @property
    def plugin(self):
        if self._plugin == None:
            from django_nose.runner import NoseTestSuiteRunner
            from django_nose.plugin import DjangoSetUpPlugin
            runner = NoseTestSuiteRunner()
            self._plugin = DjangoSetUpPlugin(runner)
        return self._plugin

    def __init__(self):
        super(DjangoNosePlugin, self).__init__()
        self._plugin = None

    def configure(self, *args, **kw_args):
        super(DjangoNosePlugin, self).configure(*args, **kw_args)
        if self.enabled:
            self.plugin.configure(*args, **kw_args)

    def prepareTest(self, test):
        setup_django()  # no-op for Django < 1.7
        self.plugin.prepareTest(test)

    def finalize(self, result):
        self.plugin.finalize(result)
