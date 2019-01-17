
"""
THIS IS WHERE YOU SET UP NEW ASSIGNMENTS! 

Library of prefabricated assignments ready for importing
"""

from ..assignment import Assignment 
from ..questionLibrary import *


# ------------------------------------------------------------------------------
# TESTASSIGNMENT 

TestAssignment = Assignment(AddTwoNumbers,
                            PlotCurve,
                            GetDictKeys,
                            GetDictValues,
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




# ------------------------------------------------------------------------------
# TESTASSIGNMENT 

PreCourseAssignment = Assignment(
                            AddTwoNumbers,
                            GetDictKeys,
                            GetDictValues,
                            ReverseAList,
                            regexGetDigits,
                            DataFrameFromLists,
                            LinearRegressionWithSklearn,
                            PlotCurve,
                            leadmd = """ # Pre Course Assignment for TSDS 

                            This assignment consist of 8 questions and must be handed in
                            before the beginning of the TSDS lectures. The reason we give 
                            you an assignment so early in the course is to ensure you have
                            all installed python, and are confident using it to the level 
                            you are taught in the summer course SDS. If you haven't already
                            installed the anaconda python distribution on your system,
                            a simple google search should get you there.


                            ### Practical info
                            * Handin no later than XXXX 
                            * Feel free to colaborate, but upload one notebook per student.

                            ### Code validation
                            These questions have a build-in validator that will tell you 
                            if your answers are correct. To use it you need to install a package
                            called `checks` from here: 
                            [https://github.com/Kristianuruplarsen/checks](https://github.com/Kristianuruplarsen/checks)

                            > **Note:** The `checks` package is in very early development so dont worry if 
                            you can't get it to work. We will accept submissions if they dont use the automated checking.

                            To install the package simply run the following in your terminal:
                            ```
                            pip install git+https://github.com/Kristianuruplarsen/checks
                            ```
                            After doing this you should be able to simply run
                            ```
                            from checks import PreCourseAssignment
                            ```
                            after which you can decorate your answers in the following way to 
                            get instant validation of your answers: 
                            ```
                            PreCourseAssignment.submit(problem = 1)
                            def add(x,y):
                            # ... Code here
                            ```
                            For a more thorough introduction to the `checks` package refer to the git repo.
                            """,
                            leadcode = "from checks import PreCourseAssignment"
                            )
