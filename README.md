# ngcm-tutorial

Materials for the IPython/Jupyter workshop at the NGCM Summer Academy, at
Southampton University, Boldrewood campus.

Teaching blocks from 9:30-11am, 11:30am-1pm, 2:30-3:30pm and 4-5:30pm. There
will be coffee breaks at 11 am and 3:30 pm and a 1 hour lunch break from 1-2
pm.

### Installation:

Anaconda
pandoc
latex
git
github account


http://ngcm.soton.ac.uk/summer-academy/ipython.html

Lecture key; 1, 2, 4 are 1:30h, 3 is 1h. 5 is really a little demo at the end
of lecture 4.

IPython

3-day course
24, 25 and 26 June 2015
At Southampton University, Boldrewood campus, 175/1025

### Course content

Python provides tools for interactive and parallel computing that are widely used in scientific computing. We will show some uses of IPython for scientific applications, focusing on exciting recent developments, web-based notebook with code, graphics, and rich HTML.

In this advance tutorial we will mostly focus on the notebook format and capability of the IPython web notebook.

Day 1: Core IPython

Notebook Basics
IPython - beyond plain python
Markdown Cells
Rich Display System
Introduction to Interactive Javascript Widgets
Customizing IPython - a condensed version

Day 1 End Demo:         rpy2, pyjulia


Day 2: Interactivity and the Jupyter project

The architecture of interactive widgets
Developing custom widgets
Notebooks as documents: sharing and converting them
Beyond Python: the Jupyter architecture with Julia and R
The Jupyter Hub: multiuser Jupyter environments

Day 2 End Demo: other kernels (R, Julia, etc)

Day 3: Parallel computing with IPython

Overview of the IPython.parallel model
Controller and engines
Basics of remote execution
Direct vs task execution
Integration with MPI codes
Handling dependencies between tasks
Performance considerations

Day 3 wrap-up: Architecture
   1. Single cell
   2. Thebe
   3. JupyterHub
   4. try.jupyter.org
   5. ipymd
   6. embedding
   7. nbformat

### Software Requirements

Python 3.x
IPython stable (version 3.1) installed with the notebook. It should be available through the usual distribution channel, such Anaconda.
Your favorite text editor.
If you have trouble installing Anaconda, this blog entry may help.
To install the packages required for this course and the Pandas course using Anaconda, create a suitable environment using

```bash
conda create -n ngcm python=3 numpy scipy ipython ipython-notebook pandas matplotlib pyzmq tornado requests
```

Then, to use this environment, enter

```bash
source activate ngcm
```

### Checking your installation

You can download and run this ipython-version-check.py script, and execute it using "python ipython-version-check.py" to check you have fulfilled the installation requirements.

### Required knowledge

Basic Python,
some vague notion of html would be great.
The trainer

Fernando Perez

Demonstrators: Max Albert, Josh Greenhalgh

Infrastructure

Etherpad IPython
Slack channel "ipython"
