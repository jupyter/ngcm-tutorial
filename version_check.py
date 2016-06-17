# check Python version

import sys
assert sys.version_info.major >= 3, "You need Python 3."
print("Python version is {} -> okay".format(sys.version.splitlines()[0]))

# check IPython version

import IPython
assert IPython.version_info[0] >= 4, "You need IPython >= 4.0"
print("IPython version is {} -> okay".format(IPython.__version__))

import notebook
assert notebook.version_info >= (4,2), "You need notebook >= 4.2"
print("notebook version is {} -> okay".format(notebook.__version__))

import ipywidgets
assert 4 <= ipywidgets.version_info[0] < 5, "You need ipywidgets 4.x"
print("ipywidgets version is {} -> okay".format(ipywidgets.__version__))

import ipyparallel
assert ipyparallel.version_info[0] > 4, "You need ipyparallel >= 4"
print("ipyparallel version is {} -> okay".format(ipyparallel.__version__))

import traitlets
assert traitlets.version_info >= (4,2), "You need traitlets >= 4.2"
print("traitlets version is {} -> okay".format(traitlets.__version__))

print("You are all set for the IPython course at the NGCM Summer academy 2016.")
