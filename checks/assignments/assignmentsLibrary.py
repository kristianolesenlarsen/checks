
"""
THIS IS WHERE YOU SET UP NEW ASSIGNMENTS! 

Library of prefabricated assignments ready for importing
"""

from .assignment import Assignment 
from ..questionChecker import QuestionChecker
from ..questionLibrary import *


TestAssignment = Assignment(AddTwoNumbers,
                            SubTwoNumbers, 
                            DataFrameFromLists,
                            LinearRegressionWithSklearn,
                            MultiplyTwoNumbers,
                            joinStringArgs,
                            leadmd = """ # Test assignment 

                            This is a test assignment which should not be used for anything real.
                            """,
                            leadcode="from checks import TestAssignment"
                            )

