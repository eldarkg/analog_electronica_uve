import copy

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


def __latex_ref(ref):
    latex = ''
    outter = True
    for c in ref:
        if c == '_':
            if outter:
                latex += c
                latex += '{'
                outter = False
            else:
                latex += '}'
                latex += c
                latex += '{'
        else:
            latex += c

    if not outter:
        latex += '}'

    return latex


def disp(exp, si=False):
    ref = argname('exp')
    expc = copy.deepcopy(exp)

    units = __ref_to_units(ref, si)
    if units:
        mul = __units_prefix_to_mul(units)
        if isinstance(expc, Iterable):
            for i in range(len(expc)):
                expc[i] *= mul
        else:
            expc *= mul

        if units == '%':
            units = '\%'

    latex_ref = __latex_ref(ref)

    display(Latex(f'${latex_ref} = {sympy.latex(expc)}, {units}$'))


def plot(exp, xrange, nb_of_points=None, si=False):
    ref = argname('exp')
    expc = copy.deepcopy(exp)

    units = __ref_to_units(ref, si)
    if units:
        mul = __units_prefix_to_mul(units)
        expc *= mul

    latex_ref = __latex_ref(ref)

    adaptive = nb_of_points is None
    #FIXME check xrange unit. Implement time unit.
    sympy.plot(expc, xrange, title=f'${latex_ref}, {units}$', xlabel='$U, В$', ylabel='', adaptive=adaptive, nb_of_points=nb_of_points)


def plot_harmonics(harmonics, xrange, freq=1.0, nb_of_points=None, si=False):
    ref = argname('harmonics')

    units = __ref_to_units(ref, si)
    mul = __units_prefix_to_mul(units) if units else 1.0

    t = xrange[0]
    exprs = [harmonics[0] * mul]
    for i in range(1, len(harmonics)):
        #FIXME use phase
        exprs.append(harmonics[i] * mul * sympy.sin(2 * sympy.pi * i * freq * t))

    adaptive = nb_of_points is None
    sympy.plot(*exprs, xrange, title=f'${ref}, {units}$', xlabel='$t, с$', ylabel='', adaptive=adaptive, nb_of_points=nb_of_points)