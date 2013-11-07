django_nose_adapter
===================

Use the django_nose plugin, defined in the django-nose package, from the nose command line, 
so you can test django in Eclipse PyUnit.

To install the plugin, type

'''
easy_install . 
'''

in the plugin directory.  When you run nosetests -p, you should see djangonose listed.

To setup PyUnit in Eclipse, create a PyUnit run configuration and select your app's test module 
as the 'main module'.

Under 'Arguments', override the default test runner, and use Nose Test with the command line 
argument --with-djangonose.  In 'Environment Variables', set DJANGO_SETTINGS_MODULE to 'settings'.  
Also, ensure your PythonPath is appropriate for your project.

The first time the configuration is run, you may get an Eclipse build error, but mysteriously, 
it works after that.  

Note that you can also use django_nose's REUSE_DB environment setting to speed up your django tests.

Validate installation by running from the command line:
'''
DJANGO_SETTINGS_MODULE='settings' PYTHONPATH='yourpath' nosetests yourapp.tests --with-djangonose
''' 