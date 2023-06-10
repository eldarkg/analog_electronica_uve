import seaborn as sns
from sympy.plotting import plot


sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})


def plot_g(exp, xlim, ylim):
    print('G(U):')
    display(exp)
    plot(exp, title='G, S', xlabel='U, V', ylabel='', xlim=xlim, ylim=ylim)


def plot_r(exp, xlim, ylim):
    print('R(U):')
    display(exp)
    plot(exp, title=r'R, $\Omega$', xlabel='U, V', ylabel='', xlim=xlim, ylim=ylim)


def plot_i(exp, xlim, ylim):
    print('I(U):')
    display(exp)
    plot(exp, title='I, A', xlabel='U, V', ylabel='', xlim=xlim, ylim=ylim)