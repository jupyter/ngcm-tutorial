# IPython/Jupyter Workshop at the NGCM Summer Academy

Materials for the IPython/Jupyter workshop at the Next-Generation Computational
Modeling Summer Academy:

-   3-day course
-   24, 25 and 26 June 2015
-   At Southampton University, Boldrewood campus, 175/1025

Course URL: http://ngcm.soton.ac.uk/summer-academy/ipython.html

Teaching blocks from 9:30-11am, 11:30am-1pm, 2:30-3:30pm and 4-5:30pm. There
will be coffee breaks at 11 am and 3:30 pm and a 1 hour lunch break from 1-2
pm.

## Course content

Python provides tools for interactive and parallel computing that are
widely used in scientific computing. We will show some uses of IPython
for scientific applications, focusing on exciting recent developments,
web-based notebook with code, graphics, and rich HTML.

In this advance tutorial we will mostly focus on the notebook format and
capability of the IPython web notebook.

Day 1: Core IPython

-   Notebook Basics
-   IPython - beyond plain python
-   Markdown Cells
-   Rich Display System
-   Introduction to Interactive Javascript Widgets
-   Customizing IPython - a condensed version

Day 2: Interactivity and the Jupyter project

-   The architecture of interactive widgets
-   Developing custom widgets
-   Notebooks as documents: sharing and converting them
-   Beyond Python: the Jupyter architecture with Julia and R
-   The Jupyter Hub: multiuser Jupyter environments

Day 3: Parallel computing with IPython

-   Overview of the IPython.parallel model
-   Controller and engines
-   Basics of remote execution
-   Direct vs task execution
-   Integration with MPI codes
-   Handling dependencies between tasks
-   Performance considerations


## Software Requirements

-   Python 3.x
-   IPython stable (version 3.1) installed with the notebook. It should
    be available through the usual distribution channel, such
    [Anaconda](http://continuum.io/downloads).
-   Your favorite text editor.
-   If you have trouble installing Anaconda, [this blog
    entry](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html)
    may help.

To install the packages required for this course and the Pandas course
using Anaconda, create a suitable environment using

```bash
conda create -n ngcm python=3 numpy scipy ipython ipython-notebook ipython-qtconsole pandas matplotlib pyzmq tornado requests scikit-image sympy
```

Then, to use this environment, enter

```python
source activate ngcm
```

## Checking your installation

You can download and run this
[ipython-version-check.py](http://www.southampton.ac.uk/~fangohr/teaching/summeracademy/2015/ipython-version-check.py)
script, and execute it using "python ipython-version-check.py" to check
you have fulfilled the installation requirements.


## Required knowledge

-   Basic Python,
-   some vague notion of html would be great.


## The trainers

-   [Ian Hawke](http://cmg.soton.ac.uk/people/ih3/)
-   [MinRK](http://github.com/minrk)

Demonstrators: [Max Albert](http://cmg.soton.ac.uk/people/mha2e09/),
[Josh Greenhalgh (NGCM)](http://cmg.soton.ac.uk/people/jdg1g14/)


## Infrastructure

-   [Etherpad IPython](https://etherpad.mozilla.org/YWve9erzYX)
-   [Slack channel "ipython"](https://ngcmsummeracademy2015.slack.com/messages/ipython/)
