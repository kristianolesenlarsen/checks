
"""
Base functionality for the question library. 
"""
from collections import namedtuple
import pickle

class Test:
    """
    Container for a specific test input-output
    """
    def __init__(self, inputs, result, special_check):
        self.inputs = inputs 
        self.result = result
        self.special = special_check



def inputfromfile(filepath):
    pass

def resultfromfile(filepath):
    pass



class Question:
    """
    Iter functionality for a question, iters over all test-inputs.
    """
    def __init__(self):
        pass 

    def __iter__(self):
        self.i = 0
        return self
    
    def __next__(self):
        if self.i < len(self.inputs):
            inp = self.inputs[self.i]
            ans = self.answer(*inp)
            try:
                special = self.special_check
            except AttributeError:
                special = False
            self.i += 1
            return Test(inp, ans, special)
        else:
            raise StopIteration

    def tofile(self, filepath):
        """
        Save a question to file, so it can be read again later.
        """
        Q = namedtuple('question', 'markdown inputs result')
        try:
            q = Q(self.md, self.inputs, self.result)

            # TODO: Implement saving q in some way

        except TypeError:
            raise

