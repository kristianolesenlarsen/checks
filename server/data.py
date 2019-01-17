import re 
import pickle 

class StatusData:

    def __init__(self, student_id_list, n_problems):
        self.students = student_id_list
        self.problems = n_problems 
        self.data = None 

    def initialize_data(self):
        for ku_ident in self.students:
            if not re.match(r'[A-Za-z]{3}\d{3}', ku_ident):
                raise ValueError(f'User ID {ku_ident} is invalid. KU ident must be 3 letters and 3 digits.')

        data =  {k: {n + 1: False for n in range(self.problems)} for k in self.students}
        self.data = data
        return self

    def to_file(self):
        if self.data is None:
            raise ValueError("Data is not set.")

        with open('userdata.pckl', 'wb') as f:
            pickle.dump(self.data, f)


    def from_file(self):
        with open('userdata.pckl', 'w') as f:
            data = pickle.load(f)
        self.data = data
        return self 
