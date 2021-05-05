CLI RPN Calculator
==================

Command-line reverse polish notation (RPN) calculator using Python 3.
I have built this command-line calculator for people who are comfortable with UNIX-like CLI utilities.

Specifications
--------------

1. The calculator uses standard input and standard output
2. It implements the four standard arithmetic operators i.e. + - * /
3. The calculator handle errors and recovers gracefully
4. The calculator exits when it receives a `q`, `quit`, `exit` command

How to run code
--------------

* Install Python 3 on your PC
* Clone repository on your local PC
* Open a Terminal or Command Prompt
* In terminal, go to the cloned directory 
* Check Python 3 runs using `python` or  `python3` command
* In your cloned directory, run this command from terminal - `python3 index.py`

Example Input/Output
--------------------

This RPN calculator have been tested with following inputs and gives the expected results

    > 5 
    5
    > 8
    8
    > +
    13

---

    > 5 5 5 8 + + -
    -13.0
    > 13 +
    0.0

---

    > -3
    -3.0
    > -2
    -2.0
    > *
    6.0
    > 5
    5.0
    > +
    11.0

---

    > 5
    5
    > 9
    9
    > 1
    1
    > -
    8
    > /
    0.625
