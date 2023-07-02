from collections.abc import Iterable
import seaborn as sns
import sympy
from varname import argname
from IPython.display import display, Latex


sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})


def __ref_to_units(ref, si):
    type = ref[0].upper()
    if type in ('G', 'Y'):
        return 'См' if si else 'мСм'
    elif type in ('R', 'Z'):
        return 'Ом' if si else 'кОм'
    elif type == 'I':
        return 'А' if si else 'мА'
    elif type == 'U':
        return 'В'
    elif type == 'K':
        return '' if si else '%'
    else:
        return ''


def __units_prefix_to_mul(units):
    prefix = units[0]

    if prefix == 'м':
        return 1E3
    elif prefix == 'к':
        return 1E-3
    elif prefix == '%':
        return 1E2
    else:
        return 1


def disp(exp, si=False):
    ref = argname('exp')

    units = __ref_to_units(ref, si)
    if units:
        mul = __units_prefix_to_mul(units)
        if isinstance(exp, Iterable):
            for i in range(len(exp)):
                exp[i] *= mul
        else:
            exp *= mul

        if units == '%':
            units = '\%'

    display(Latex(f'${ref} = {sympy.latex(exp)}, {units}$'))


def plot(exp, xrange, nb_of_points=None, si=False):
    ref = argname('exp')

    units = __ref_to_units(ref, si)
    if units:
        mul = __units_prefix_to_mul(units)
        exp *= mul

    adaptive = nb_of_points is None
    sympy.plot(exp, xrange, title=f'{ref}, {units}', xlabel='U, В', ylabel='', adaptive=adaptive, nb_of_points=nb_of_points)