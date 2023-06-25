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
    if exp.free_symbols:
        params = f'({exp.free_symbols})'
    else:
        params = ''
    display(Latex(f'${ref}{params} = {sympy.latex(exp)}, {__ref_to_units(ref)}$'))


def plot(exp, xrange):
    type = argname('exp')
    if type in ('G', 'g', 'Y'):
        units = 'См'
    elif type in ('R', 'r', 'Z'):
        units = 'Ом'
    elif type in ('I', 'i'):
        units = 'А'
    else:
        return

    #sympy.plot(exp, xrange, ylabel=f'{type}, {units}', xlabel='U, В')
    sympy.plot(exp, xrange, title=f'{type}, {units}', xlabel='U, В', ylabel='')