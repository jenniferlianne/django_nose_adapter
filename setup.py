try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass

from setuptools import setup

setup(
    name='DjangoNosePlugin',
    version='0.1',
    author='Jennifer Bell',
    author_email='jenniferlianne@yahoo.ca',
    description='Use plugin defined in django_nose to run tests via nose \
command line. Allows running django tests via Eclipse PyUnit.',
    license='MIT',
    install_requires=["django_nose"],
    py_modules=['django_nose_plugin'],
    entry_points={
        'nose.plugins.0.10': [
            'django_nose_plugin = django_nose_plugin:DjangoNosePlugin'
            ]
    }
)
