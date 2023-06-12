import seaborn as sns
import sympy
from varname import argname


sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})


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

    print(f'{type}(U) =')
    display(exp)

    sympy.plot(exp, title=f'{type}, {units}', xlabel='U, В', ylabel='', xlim=xlim, ylim=ylim)