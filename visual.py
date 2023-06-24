import seaborn as sns
import sympy
from varname import argname
from IPython.display import display, Latex


sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})


def disp(exp):
    type = argname('exp')
    display(Latex(f'${type}({exp.free_symbols}) =$'), exp)


def plot(exp, xlim, ylim):
    type = argname('exp')
    if type in ('G', 'g', 'Y'):
        units = 'См'
    elif type in ('R', 'r', 'Z'):
        units = 'Ом'
    elif type in ('I', 'i'):
        units = 'А'
    else:
        return

    display(Latex(f'${type}({exp.free_symbols}) =$'), exp)

    sympy.plot(exp, title=f'{type}, {units}', xlabel='U, В', ylabel='', xlim=xlim, ylim=ylim)