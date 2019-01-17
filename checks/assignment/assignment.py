
"""
Generic assignment class which can be invoked with any number of questions.
"""
import nbformat as nbf
import os 
import re 

from .questionChecker import QuestionChecker


# Inheritance is purely for code segmentation for now (rework?)
class Assignment(QuestionChecker):
    """
    Generic assignment

    Parameters
    ----------
    *questions: Question
        A sequence of questions (from the questionLibrary) ordered by their 
        intended appearance in the final exercise set. 
    """

    def __init__(self, *questions, 
                        leadmd = None, 
                        leadcode = None
                ):

        self.leadmd = leadmd 
        self.leadcode = leadcode

        if self.leadmd is not None:
            self.leadmd = self._clean_string(leadmd)
            
        if self.leadcode is not None:
            self.leadcode = self._clean_string(leadcode)

        self.questions = {i + 1: q for i,q in enumerate(questions)}
        self.correctly_ans = {k: None for k in self.questions.keys()}

        # Semi-unused
        self.user = None                
        self.submit_after_each_question = True     


    def make_notebook(self, filename):
        """
        Build the exercise notebook.
        """
        nb = nbf.v4.new_notebook()

        # add lead code and markdown if they exist
        if self.leadmd is not None:
            nb['cells'] += [nbf.v4.new_markdown_cell(self.leadmd)]
        if self.leadcode is not None:
            nb['cells'] += [nbf.v4.new_code_cell(self.leadcode)]

        # add questions
        for num, question in self.questions.items():
            md = self._clean_string(self._make_markdown(num, question))

            nb['cells'] += [nbf.v4.new_markdown_cell(md), 
                            nbf.v4.new_code_cell(f"# [Answer to problem {num} here]")]

        print(f'Building notebook in {os.getcwd()}')
        nbf.write(nb, f'{filename}.ipynb')


    def _make_markdown(self, num, question):
        qtext = question().markdown
        s = f'# Problem {num} \n' + qtext
        
        return s


    def _clean_string(self, s):
        """ Remove whitespace in all string lines in a multiline string.
        """
        lines = s.split('\n')
        lines = [l.strip() for l in lines]
        return '\n'.join(lines).strip()


    def setup(self, ku_ident):
        # TODO: This check should also verify that the KU id is in the database
        if not re.match(r'[A-Za-z]{3}\d{3}', ku_ident):
            raise ValueError(f'User ID {ku_ident} is invalid. KU ident must be 3 letters and 3 digits.')
        self.user = ku_ident

        return self


