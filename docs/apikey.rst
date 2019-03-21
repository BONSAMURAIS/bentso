ENTSO-E API key
---------------

You will need a `apply for an ENTSO-E API key <https://entsoe.zendesk.com/hc/en-us/articles/115000153663-Restful-API-first-steps-general-info->`__ before you can use bentso. There are two ways to provide this key to bentso:

* You can specify the environment variable ``ENTSOE_API_TOKEN``. This is the preferred method. `Environment variables on Windows <https://docs.python.org/3/using/windows.html#excursus-setting-environment-variables>`__.
* You can create a file in the same directory that you are using called ``entsoe_api_token.txt``. This file should have one line, which is the API token.

The environment variable will take precedence if both options are used.

Environment variables: Virtualenv
---------------------------------

Use virtualenvwrapper, and `set the variables in the postactivate and predeactivate scripts <https://stackoverflow.com/a/11134336/164864>`__.

Environment variables: Conda
----------------------------

In conda you need to `create new directories to set environment variables <https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#macos-and-linux>`__.
