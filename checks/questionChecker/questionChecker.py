
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
        answer: function
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

            if not special_check:
                check = lambda inp, ans: useranswer(*inp) == ans
            else:
                check = lambda inp, ans: special_check(inp, ans, useranswer)

            try:
                if not check(inp, ans):
#                if not answer(*inp) == ans:
                    print(f'Failed test with inputs: \n {inp} \n Returned: \n {useranswer(*inp)} \n\n')
                    return False
                print(f'Passed test with inputs: \n {inp} \n Returned: \n {useranswer(*inp)} \n\n')
                                
            except TypeError as e:
                if not e.args: 
                    e.args=('',)
                e.args = e.args + ('The input type your function accepts seem to differ from the expected input types',)
                raise
        return True

