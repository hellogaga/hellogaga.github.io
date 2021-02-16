---
title: "Python PEP8 Style"
last_modified_at: 2020-10-12T16:20:02-05:00

categories:
  - Blog
tags:
  - Python
  - Code Style
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"

---

# What is PEP 8
According to [Jasmine Finer](https://realpython.com/python-pep8/):
>PEP8 is a document that provides guidelines and best practices on how to write Python code. It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan. The primary focus of PEP 8 is to improve the readability and consistency of Python code.

# How to check if your code follows PEP 8. 
A very useful tool is `pycodestyle`, which can be installed with `pip`. This package is previously known as `pep8`.
```python
pip install pycodestyle
```
The usage of the package is also very simple. `.` in the following will simple check all the files in the current folder. If the current folder contains the installed dependencies, it will take quite some time. You can also specify a specific document and check its consistency with PEP8 style
```
pycodestyle .
pycodestyle example.py
```
# Common Rules by PEP 8
A list of common rules can be found [here](https://www.flake8rules.com/). You can find both good and bad practices. For example, E111 is *Indentation is not a multiple of four*. That implies that the indentation did not follow the convention. The document might followed indentation of two spaces, which are convention in some companies. 

# How to fix codes. 
Now we introduce another very useful package `autopep8`. It can be installed by `pip install autopep8`. Please note that this package is dependent on `pycodestyle`. So make sure your have installed `pycodestyple`.  The use of this package is also very simple, please refer the [document](https://pypi.org/project/autopep8/) for detailed information. A simple example is given below:
``` python
autopep8 -i example.py
```
The `-i` stands for in place. Thus the original document will be replaced with new one. If you are not comfortable with this. You can simply run `autopep8 example.py`. This will prompt results in the console. 

