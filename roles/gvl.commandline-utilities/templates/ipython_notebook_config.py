# Configuration file for ipython, intended for notebook server.
# Generated by GVL setup script.

c = get_config()

# Do not open local browser, just run as a server
c.NotebookApp.open_browser = False

# Require password authentication
c.NotebookApp.password = u'{{ password_python_hash }}'

# Use a known port, which should match that in nginx port forwarding.
# Do not try any other ports.
# If you are editing your config to allow multiple instances of IPython Notebook
# to run simultaneously, you may want to change these settings.
c.NotebookApp.port = {{ ipython_port }}
c.NotebookApp.port_retries = 0

# Assume that we will run at a subdirectory when port-forwarded
c.NotebookApp.base_project_url = '{{ ipython_location }}'
c.NotebookApp.base_kernel_url = '{{ ipython_location }}'
c.NotebookApp.webapp_settings = {'static_url_prefix':'{{ ipython_location }}static/'}
