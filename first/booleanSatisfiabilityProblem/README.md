Boolean satisfiability problem
=====================

Practice #1:

**Languages**

* Python 2.7.7 Anaconda.

It consists in reading a txt file with the format of the maxiterms:

* "1" is for the variable exists in the term.
* "0" the variable has to be negated. 
* "-1" the variable doesn't exist in the term.


 E.g:
 
 For the given data in "content.txt":
 > 1 0
 >-1 0
 
 The program's output will be something like this.
 
>| x0  | x1 | (x0 and not(x1) ) or ( not(x1) ) | Evaluation |
| - | - | - | - |
| True | True  | (True and  not(True) ) or ( not(True) ) | False |
| False | True  | (False and  not(True) ) or ( not(True) ) | False |
| True | False  | (True and  not(False) ) or ( not(False) ) | True |
| False | False  | (False and  not(False) ) or ( not(False) ) | True |


----------

Any doubts about it! Try to contact me! [Twitter](http://twitter.com/jresendiz27)