"""
THIS IS WHERE YOU MAKE NEW QUESTIONS!

A question is a class with a descriptive name, which inherits from Question. 
The class must implement 

Property markdown: the string that becomes the markdown cell associated with 
    the question. 

Property inputs: a list of test-inputs which the users answer is 
    validated against.

method answer: an implementation of the correct answer. 

(optional) method special_check: if a simple useranswer(inputs) == correct_answer 
    test does not evaluate to True/False you can implement a custom check here. 
    This is for example relevant when working with pandas. 
"""

from .question import Test, Question


class GetDictValues(Question):
    
    @property 
    def markdown(self):
        s = """ Write a function that takes as it's single input 
        * Any dictionary 
        The function should return the values of the input dictionary, in a `list`.

        > *Hint:* be aware that many of the build in dictionary methods returns special
        containers that look like lists, but are in fact not. If you need to you can
        convert your result to a list using the `list()` buildin function.
        """
        return s 

    @property
    def inputs(self):
        inp = [
            ({'a':1, 'b':2, 'c':3, 'd':4}),
            ({1:'a', 2:'b', 3:'c', 4:'d'}),
            ({}),
            ({'Key':'value'})
        ]
        return inp 

    def answer(self, dictionary):
        return list(dictionary.values())


class GetDictKeys(Question):
    
    @property 
    def markdown(self):
        s = """ Write a function that takes as it's single input 
        * Any dictionary 
        The function should return the keys of the input dictionary, in a `list`.

        > *Hint:* be aware that many of the build in dictionary methods returns special
        containers that look like lists, but are in fact not. If you need to you can
        convert your result to a list using the `list()` buildin function.
        """
        return s 

    @property
    def inputs(self):
        inp = [
            ({'a':1, 'b':2, 'c':3, 'd':4}),
            ({1:'a', 2:'b', 3:'c', 4:'d'}),
            ({}),
            ({'Key':value})
        ]
        return inp 

    def answer(self, dictionary):
        return list(dictionary.keys())


class PlotCurve(Question):
    @property
    def markdown(self):
        s = """ Write a function that takes the following two inputs:
            * a list `x` of length N containing floats.
            * a list `y` of length N containing floats.

        Given the two lists, write a function that uses matplotlib to plot a curve
        with `x` on the first axis and `y` on the 2nd axis using `plt.plot()`. Add
        on top of this a set of scatter-points with the same coordinates as the line. 

        > *Hint:* Don't show the figure within the function body. To properly wrap 
        matplotlib code in a function simply `return plt` at the end of the function. I.e.
        ```
        def somePlot(x,y):
            # [Matplotlib code]            
            plt.plot(...)
            # [/Matplotlib code]
            return plt
        ```
        """
        return s 

    @property
    def inputs(self):
        inp = [
            ([1,2,3,4,5], [2,4,9,16,25]),
            ([2,4,6,8,10], [1,3,5,7,9])
        ]
        return inp

    def answer(self, x, y):
        import matplotlib.pyplot as plt 

        if not len(x) == len(y):
            return None

        plt.plot(x,y)
        plt.scatter(x,y)

        return plt


class DataFrameFromLists(Question):
    @property
    def markdown(self):
        s = """ Write a function that takes the following arguments:
        * An unknown number of lists, each containing floats representing the values of a variable.
        * A list of strings, containing the column names for a table. 

        For example, the function might be given a list of column names `key=['ID','year', 'age', 'income_index']
        and _four_ other lists: [1,1,1,2,2,2], [22,23,24,32,33,34], [2000,2001,2002,2000,2001,2002], [100,110,130,100,98,74]

        From these inputs the function should return a pandas DataFrame like 

        | 'ID' | 'year' | 'age' | 'income_index' |
        |------|--------|-------|----------------|
        |   1  | 2000   | 22    |   100          |
        |   1  | 2001   | 23    |   110          |
        |   1  | 2001   | 24    |   130          |                
        |   2  | 2000   | 32    |   100          |
        |   2  | 2001   | 33    |   98           |
        |   2  | 2001   | 44    |   74           |                

        > *Hint:* you will need to understand the `*input` notation for variable length arguments. 
        """
        return s 
    
    @property
    def inputs(self):
        inp = [
            (['a','b'],[1,2,3],[3,2,1]),
            (['ID','year', 'age', 'income_index'],
            [1,1,1,2,2,2],
            [22,23,24,32,33,34],
            [2000,2001,2002,2000,2001,2002],
            [100,110,130,100,98,74])
        ]
        return inp

    def special_check(self, inp, ans, useranswer):
        return (useranswer(*inp) == ans).all().all()

    def answer(self, keys, *values):
        import pandas as pd

        raw = {k:v for k,v in zip(keys, values)} 
        df = pd.DataFrame(raw)
        return df


class LinearRegressionWithSklearn(Question):

    @property
    def markdown(self):
        s = """ For this question you should write a function which takes two 
    numpy arrays as inputs, uses scikit learn's LinearRegression module to 
    estimate a model of the data, and return the coefficients as a numpy array. For example 
    you should make sure your function runs on input like 
    ```
    X = np.array([1,2,3])
    y = np.array([3,2,1])
    ```
    > *Hint:* we expect the output from the .coef_ attribute of the fitted 
    model object.
    > 
    > *Hint:* Your function will be tested with 1-dimensional X input. You might want to investigate how scikit learn handles this."""
        return s

    @property
    def inputs(self):
        import numpy as np 

        inp = [
            (np.array([1,2,3]), np.array([2,3,4])),
            (np.array([4,6,8]), np.array([1,2,3])),
            (np.array([4,6,7]), np.array([3,2,1]))
        ]
        return inp

    def answer(self, X, y):
        from sklearn.linear_model import LinearRegression 
        
        m = LinearRegression()
        m = m.fit(X.reshape(-1,1), y)

        return m.coef_


class joinStringArgs(Question):
    @property 
    def markdown(self):
        s = """ Write a function that takes some arbitrary number of string inputs as arguments and joins them together, separated by commas.

        Note the string should be passed individually. Not in a list or tuple. The input might for example be 
        `'a','b'` or it could be `'hel', 'ld' 'wor', 'ld'`.  To be clear your output should be a string. I
        If for example your function receives inputs `'a', 'b', 'c'` the output should be `'abc'`.     
        """
        return s 

    @property
    def inputs(self):
        inp = [
            ('a','b','c'),
            ('z','y'),
            ('hej','hej')
        ]
        return inp 
    
    def answer(self, *s):
        return ','.join(s)


class SubTwoNumbers(Question):
    @property    
    def markdown(self):
        s = """Write a function that subtracts two numbers x,y and returns the output x - y.
        Sample input might be `x=-2`, `y=8.2' in which case the output should be `-10.2`. 
        The expected output is either float or int. 
        """
        return s 

    @property
    def inputs(self):
        inp = [(1,1),
                (3,2),
               (-2,3)]
        return inp

    def answer(self, x, y):
        return x - y


class AddTwoNumbers(Question):  
    @property    
    def markdown(self):
        s = """ Write a function that adds two numbers x,y and returns the output x + y. 
        Sample input might be `x=-1`, `y=8' in which case the expected output is `7`. 
        The expected output is either float or int.
        """
        return s 

    @property
    def inputs(self):
        inp = [(1,1),
                (2,2),
               (-2,3)]
        return inp

    def answer(self, x, y):
        return x + y


class MultiplyTwoNumbers(Question):
    @property    
    def markdown(self):
        s = """Write a function that multiplies two numbers x,y and returns 
        the output x - y. Sample input can for example be `x=2` and `y=2` in which case your function should return `4`.
        """
        return s 

    @property
    def inputs(self):
        inp = [(1,1),
                (2,2),
               (-2,3)]
        return inp

    def answer(self, x, y):
        return x * y


class ZipTwoLists(Question):

    @property 
    def markdown(self):
        s = """ Write a function that takes two lists `l1` and `l2` as inputs. The function must return a new list which
        pairs the two lists element by element. In particular given sample input `l1 = [1,2,3]` and `l2 = [4,5,6]` the function
        should return `[(1,4), (2,5), (3,6)]`.

        > *Hint:* you might want to take a look at the `zip` function. Be aware that the output of zip only becomes a list 
        if you convert it.  
        """
        return s 
    
    @property 
    def inputs(self):
        inp = [
            ([1,2,3], [4,5,6]),
            ([1,4,7,-1], [5,3,2,9]),
            ([1],[2])
        ]
        return inp 
    
    def answer(self, l1, l2):
        return list(zip(l1, l2))


class ReverseAList(Question):

    @property
    def markdown(self):
        s = """ Write a function that takes a list as input and returns the *reversed* list.
        For example given a list `l=['s', 'd', 's', 't']` the expected output is `['t', 's', 'd', 's']`
        """
        return s 

    @property
    def inputs(self):
        inp = [
            (['a','c','e'],),
            (['asd','de','e'],),
            ([4,2,1],)
        ]
        return inp

    def answer(self, l):
        return list(reversed(l))