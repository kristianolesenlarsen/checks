
"""
This is where we check if an answer passes all the checks required to be
considered correct.
"""

# TODO: Test reworked connection method with Pi

from functools import wraps
from requests import post

class QuestionChecker:
    """
    Check if a question is correctly answered. Only used as superclass for 
    Assignment in assignment.py!

    Parameters
    ----------

    Arguments
    ---------
    testvalues: dict
        Keys are question ID's and values are a tuple of test values to run 
        the submitted answer on.
    """

    def submit(self, problem):
        """
        Submit an answer. Decorator for submit_answer. 

        Parameters
        ----------
        problem: int
            Problem you wish to answer with the decorated function.        
        """
        def decorator(func):

            @wraps(func)
            def with_answer_submission():
                self.submit_answer(problem = problem, useranswer = func)
            return with_answer_submission()
        return decorator


    def submit_answer(self, problem, useranswer):
        """
        Submit an answer. Does not hand in the submitted answer.

        Parameters
        ----------
        problem: int
            The problem number written (this is written in the title of 
            the problem)
        useranswer: function
            A function which solves the question with problem number `problem`.
        
        Returns
        -------
        Nothing
        """
        if self._test_answer(problem = problem, useranswer = useranswer):
            if not self.correctly_ans[problem] == True:
                self.correctly_ans[problem] = True
                self.progress(newline = True)
                
                if self.online:
                    self.conn.send_answer_to_db(problem, True)


            print(f'Your answer to problem {problem} is CORRECT. ')
        else:
            self.correctly_ans[problem] = False
            print(f'Your answer to problem {problem} is WRONG.')


    def _test_answer(self, problem, useranswer):
        """
        Run through all tests associated with the problem.
        Internal.
        """
        for test in self.questions[int(problem)]():
            inp, ans, special_check = test.inputs, test.result, test.special
            p = TestStatusPrinter(ans, useranswer, inp)

            # Some questions require a special check to properly return True/False
            if not special_check:
                check = lambda inp, ans: useranswer(*inp) == ans
            else:
                check = lambda inp, ans: special_check(inp, ans, useranswer)

            try:
                if not check(inp, ans):
                    p.tprint(success = False)
                    return False
                p.tprint(success = True)
                                
            except TypeError as e:
                if not e.args: 
                    e.args=('',)
                e.args = e.args + ('The input type your function accepts seem to differ from the expected input types',)
                raise
        return True


    def progress(self, return_values = False, newline = False):
        """ Print the number of correctly answered problems 

        Parameters
        ----------
        return_values: bool (default False)
            Should the function return the tuple (correct answers, total questions)? 
            (alternatively returns None)
        """
        total = len(self.correctly_ans)
        correct = len({k:v for k, v in self.correctly_ans.items() if v == True})

        if newline:
            print('\n')
        print(f'You have correctly answered {correct} of {total} problems in this assignment.')

        for q, s in self.correctly_ans.items():
            if s == True:
                print(f'question {q}: correct.')
            elif s == False:
                print(f'question {q}: wrong.')
            else:
                print(f'question {q}: unanswered.')               
        if newline:
            print('\n')

        if return_values:
            return correct, total



class TestStatusPrinter:
    """
    Somewhat pretty printing of submit messages
    """

    def __init__(self, answer, useranswer, inputs):
        
        self.inputs = str(inputs)
        self.answer = str(answer)
        self.useranswer = str(useranswer(*inputs))

        if '\n' in self.answer \
        or '\n' in self.useranswer:
            self.multiline = True
        else:
            self.multiline = False 

    def tprint(self, success):
        """
        Print the status of a test.
        """
        if success:
            status = "Passed"
        else: 
            status = "Failed"

        if self.multiline:
            print("----------------------------------------\n")
            print(f"{status} test with inputs {self.inputs}\n")
            print("Answer produced output:\n")
            print(self.useranswer + '\n')

            if not success:
                print("Expected output is:\n")
                print(self.answer + '\n')

        else:
            print(f"{status} test with inputs {self.inputs}, returning {self.useranswer}")

            if not success:
                print(f"Expected output is: {self.answer}")

