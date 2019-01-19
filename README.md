
The ultimate goal of checks is to provide a tool to generate notebook-based assignments which support automatic evaluation of students answers without requiring code-execution outside of the students own machine. Secondary goals is that it should be easy to use both for teachers and students, so 

* Creating new assignments should be easy. So should adding new questions to the library. 
* Students must be able to complete their assignment, transparently track their progress and hand in their results all within the notebook. 

## Using checks as a student
Begin by installing the `checks` package from github, this should work by running 
```
pip install git+https://github.com/Kristianuruplarsen/checks
```
In the notebook containing the exercises then import the relevant assignment from checks
```python
from checks import PreCourseAssignment
``` 
Now to use the checker wrap the answers in the `@PreCourseAssignment.submit` decorator. The full code to answer question 1 would thus be
```python
@PreCourseAssignment.submit(problem = 1)
def myanswer(x,y):
        return x + y
```
which should give some text output informing you that the question was answered correctly. 

### Submitting to the server 
For now the server that registers users is a simple flask script which can be run on a Paspberry Pi (or any other local pc). I imagine bringing the Pi to a class and asking students to hand in during the session. Assuming the Pi is setup in your local network, move the scripts in the folder *server* onto it. Run both of them. 

As when used locally we begin by importing the assignment, but to work with the server we need to supply some additional information: 
```python
from checks import PreCourseAssignment
A = PreCourseAssignment.setup(ident = 'asd123', server_ip = '1.2.3.4:5')
```
Just like when offline we can now submit answers to the server by running 
```python 
@A.submit(1)
def add(x,y):
    return x + y
```
which pushes the students status to the server. On the server a little dash app can be set up to auto update a barchart showing the progress of each student. 


## Building an assignment
To build an assignment it must first be constructed. As of now this is done in assignmentsLibrary.py, where there is 
already one assignment constructed:

```python
TestAssignment = Assignment(AddTwoNumbers,
                            SubTwoNumbers, 
                            LinearRegressionWithSklearn,
                            MultiplyTwoNumbers,
                            joinStringArgs,
                            leadmd = """ # Test assignment 

                            This is a test assignment which should not be used for anything real.
                            """,
                            leadcode="from checks import TestAssignment"
                            )
```

The `TestAssignment` is then an instance of Assignment with 4 questions, a piece of markdown at the top of the document and a line of code which imports `TestAssignment` since this instance also contains the problem checker for the problem set. To build the corresponding problem set simply run 

```python
from checks import TestAssignment
TestAssignment.make_notebook('filename')
```

## Things to set up before use
- make an assignment and make sure everybody updates the package
- manually add the student ID's and number of problems to the plotstatus.py file (temp)
- remove any existing pickle file


# TODO:
- make it possible to submit to some kind of online service that allows teachers to easily see the progress of their students. 
        One way to do this is to generate a secret key which is revealed to students as they complete the questions

- make it possible to read problem input output from a file in `question.py`. This will make it possible to completely hide 
  the answer from students (low priority).
## DONE: 
- Add pre-question cell to notebook with instructions.

