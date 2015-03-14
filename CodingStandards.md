# Coding Standards #

This document contains the coding standards used by the DiffDANSE group. These standards apply primarily to Python, but can be easily extended to nearly any programming language used by the group. For good python guidelines, see below and [here](http://www.python.org/dev/peps/pep-0008/).  Conventions for docstrings are [here](http://www.python.org/dev/peps/pep-0257/). In particular, follow the [PEP8](http://www.python.org/dev/peps/pep-0008/) and [PEP257](http://www.python.org/dev/peps/pep-0257/) guidelines fully except where they are contradicted below.

## General ##

  * Use [CamelCase](http://en.wikipedia.org/wiki/CamelCase) instead of under\_bars.
    * Class names should be capitalized
    * class methods and function names should start in lowercase.
    * variables should be all lower case
    * module constants should be all upper case
  * Use Unix-style line ends
  * Use four-space delimiters instead of tabs in Python or C++ code.  Many editors can be set up to do this automatically.
  * Keep your lines shorter than 80 characters, especially so in docstrings.
  * See http://www.python.org/dev/peps/pep-0008/ for further guidelines on Python style.

## Testing ##

  * New Python codes should be written together with unit tests in the packagename.tests submodule of the package.
  * Unit test cases should check the common usage of a function, i.e., if it returns a correct value or if it raises appropriate exceptions for error conditions.
  * Unit test modules should be named as "testsomename.py", where "SomeName" refers to the class or module name that is tested.
  * Unit test modules ought to be executable as "python testsomename.py".
  * Make sure all unit tests pass before committing the code.
  * Unit test module should contain the `"import unittest"` line.  DO NOT use
> `"from unittest import *"`, do not import other things on the same line.
> The `"import unittest"` string makes it possible for the [alltests.py](http://danse.us/trac/diffraction/browser/diffraction/devtools/testing/alltests.py) script
> to find all files that define unit tests.
  * You can use [preparePyUnit.py](http://danse.us/trac/diffraction/browser/diffraction/devtools/testing/preparePyUnit.py) for generation of boiler-plate unit test code.
  * Use "alltests.py" to execute all or chosen unit tests from a group of source files.  Another option is to use "python -m packagename.tests.run"
  * The unit tests package should contain a global test script that would run them all with
```
python -m packagename.tests.run
```

## Packages and Modules ##

  * All modules and `__init__.py` files should contain a doc-string that gives an overview of the contents. A developer should be able to type 'help(packagename)' from the python console and get enough information to know whether the package contains what they need.
  * Modules that contain a single class should have the same name as that class, but all in lower case.  For example, module foo.py would contain class Foo. If the module contains multiple classes, give it an informative lowercase name.
  * Package names can be upper- or lower-case.
  * Avoid name shadowing.  Name shadowing happens when package `__init__.py` defines object with the same name as a module inside the package.  For example if package foo defines variable expansion, the module foo.expansion gets overshadowed by that variable.  This happens when the `foo/__init__.py` file contains `from foo.expansion import expansion` Solution: append "mod" to the module file name (expansionmod.py) so that it differs from the name in package namespace.

## Classes ##

  * The purpose of the class should be clearly stated in the doc-string. Any other important information about the class should also be included.
  * Document each class with a list of public member variables and the purpose of each. For an example, see [mainframe.py](http://danse.us/trac/diffraction/browser/diffraction/diffraction/diffpy.pdfgui/trunk/diffpy/pdfgui/gui/mainframe.py@2885)
  * Private variables and methods should start with `'__'`. e.g. `__privateMethod`
  * Protected variables and methods should start with `'_'`. e.g. `_protectedMethod`

## Methods and Functions ##

  * End methods and functions with 'return' even if they have no return value. This makes it easier to identify code blocks and indentation errors.
  * Give detailed documentation for the method or function. The documentation should contain:
    * A one-line description followed by a blank line.
    * A more detailed description, if necessary.
    * A description of member variables that are modified by the method and how they are modified. This is necessary to avoid creating a very large and complex Behavior Specification document.
    * A list of inputs and their description, including data type, units (if applicable), acceptable ranges and default values.
    * A description of the return value, including data type, units (if applicable) and ranges.
    * A list of exceptions and the conditions under which they are thrown.

A well-documented method:
```
def min(arglist):
    """Find the minimum value in a list.

    This is where more detailed information would go if this method
    warranted it. The reason for the one-line synopsis above is so
    the doc-string can be formatted by the built-in python help
    function and by doxygen.

    arglist -- List of arguments. arglist need not be a Python list,
               but it must support iteration.

    Returns the minimum value from the list.

    Raises: AttributeError if the arglist does not support iteration.

    """
```