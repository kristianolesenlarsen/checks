
"""
This is where we check if an answer passes all the checks required to be
considered correct.
"""

from functools import wraps

class QuestionChecker:
    """
    Check if a question is correctly answered.

    Parameters
    ----------

    Arguments
    ---------
    testvalues: dict
        Keys are question ID's and values are a tuple of test values to run 
        the submitted answer on.
    """

    def __init__(self, questions):

        # This is temporary
        self.questions = questions
        self.complete = {k:False for k in self.questions.keys()}



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
            print(f'Your answer to problem {problem} is CORRECT. ' \
                   'Remember to hand in your results when you finish.')
        else:
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

