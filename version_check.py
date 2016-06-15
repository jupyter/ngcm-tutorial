# check Python version

import sys
assert sys.version_info.major >= 3, "You need Python 3."
print("Python version is {} -> okay".format(sys.version_info[0:30]))

# check IPython version

import IPython
assert IPython.version_info[0] >= 4, "You need IPython >= 4.0"
print("IPython version is {} -> okay".format(IPython.version_info))

import notebook
assert notebook.version_info[0] >= 4, "You need notebook >= 4.0"
print("notebook version is {} -> okay".format(notebook.version_info))

import ipywidgets
assert ipywidgets.version_info[0] >= 4, "You need ipywidgets >= 4.0"
print("ipywidgets version is {} -> okay".format(ipywidgets.version_info))

print("You are all set for the IPython course at the NGCM Summer academy 2016.")
