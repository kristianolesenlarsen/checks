#%%
from os.path import dirname, split

import nbf
from nbconvert.preprocessors import (ExecutePreprocessor,
                                     CellExecutionError)

#%%

def run_notebook(filepath):
    """
    Execute a notebook from disk.
    """
    with open(filepath) as f:
        nb = nbf.read(f, as_version = 4)

    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

    try:
        run_nb = ep.preprocess(nb, {'metadata': {'path': dirname(filepath)}})

    except CellExecutionError:
        msg = f'Error executing the notebook "{split(filepath)[1]}".' 
        print(msg)
        raise

    return run_nb



class NoteBookData:
    """
    Contains code-cells and markdown cells
    """
    def __init__(self, notebook):
        self.codecells = [cell for cell in nb[0]['cells'] if cell['cell_type'] == 'code']
        self.mdcells = [cell for cell in nb[0]['cells'] if cell['cell_type'] == 'markdown']

        self.codeoutputs = self._codecell_output()
        self.exec_counts = self._codecell_excec_count()
        self.codesources = self._codecell_source()

    def _codecells_exec_count(self):
        return [cell['execution_count'] for cell in self.codecells]

    def _codecells_source(self):
        return [cell['source'] for cell in self.codecells]

    def _codecells_outputs(self):
        return [cell['outputs'] for cell in self.codecells]

#%%
nb = run_notebook('../../abc123.ipynb')

nbd = NoteBookData(nb)



#%%
#%%

#%%
