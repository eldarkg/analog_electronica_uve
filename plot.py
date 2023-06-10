import seaborn as sns
import sympy
from varname import argname


sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})


def plot(exp, xlim, ylim):
    type = argname('exp')
    if type in ('G', 'g', 'Y'):
        units = 'S'
    elif type in ('R', 'r', 'Z'):
        units = r'$\Omega$'
    elif type in ('I', 'i'):
        units = 'A'
    else:
        return

    print(f'{type}(U):')
    display(exp)

    sympy.plot(exp, title=f'{type}, {units}', xlabel='U, V', ylabel='', xlim=xlim, ylim=ylim)