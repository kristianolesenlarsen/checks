
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
                self.submit_answer(problem = problem, answer = func)
            return with_answer_submission()
        return decorator

    def submit_answer(self, problem, answer):
        """
        Submit an answer. Does not hand in the submitted answer.

        Parameters
        ----------
        problem: int
            The problem number written (this is written in the title of 
            the problem)
        answer: function
            A function which solves the question with problem number `problem`.
        
        Returns
        -------
        Nothing
        """
        if self._test_answer(problem = problem, answer = answer):
            print(f'Your answer to problem {problem} is CORRECT. ' \
                   'Remember to hand in your results when you finish.')
        else:
            print(f'Your answer to problem {problem} is WRONG.')


    def _test_answer(self, problem, answer):
        """
        Run through all tests associated with the problem.
        Internal.
        """
        for test in self.questions[int(problem)]():
            inp, ans = test.inputs, test.result
            try:
                if not answer(*inp) == ans:
                    print(f'Failed test with inputs {inp}, returned {answer(*inp)}')
                    return False
                print(f'Passed test with inputs {inp}, returned {answer(*inp)}')                
            except TypeError as e:
                if not e.args: 
                    e.args=('',)
                e.args = e.args + ('The input type your function accepts seem to differ from the expected input types',)
                raise
        return True

