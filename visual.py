import seaborn as sns
import sympy
from varname import argname
from IPython.display import display, Latex


sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})


def __ref_to_units(ref):
    type = ref[0].upper()
    if type in ('G', 'Y'):
        return 'См'
    elif type in ('R', 'Z'):
        return 'Ом'
    elif type == 'I':
        return 'А'
    elif type == 'U':
        return 'В'
    else:
        return ''


def disp(exp):
    ref = argname('exp')
    display(Latex(f'${ref} = {sympy.latex(exp)}, {__ref_to_units(ref)}$'))


def plot(exp, xrange, nb_of_points=None):
    type = argname('exp')
    if type in ('G', 'g', 'Y'):
        units = 'См'
    elif type in ('R', 'r', 'Z'):
        units = 'Ом'
    elif type in ('I', 'i'):
        units = 'А'
    else:
        return

    adaptive = nb_of_points is None
    sympy.plot(exp, xrange, title=f'{type}, {units}', xlabel='U, В', ylabel='', adaptive=adaptive, nb_of_points=nb_of_points)