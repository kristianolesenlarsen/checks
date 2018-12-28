
"""
THIS IS WHERE YOU SET UP NEW ASSIGNMENTS! 

Library of prefabricated assignments ready for importing
"""

from .assignment import Assignment 
from ..questionLibrary import *


# ------------------------------------------------------------------------------
# TESTASSIGNMENT 

TestAssignment = Assignment(AddTwoNumbers,
#                            ZipTwoLists,
                            SubTwoNumbers,
                            ReverseAList, 
#                            DataFrameFromLists,
#                            LinearRegressionWithSklearn,
#                            MultiplyTwoNumbers,
#                            joinStringArgs,
                            leadmd = """ # Test assignment 

                            This is a test assignment which should not be used for anything real.
                            """,
                            leadcode="from checks import TestAssignment"
                            )

