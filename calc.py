import pandas as pd
import sympy

#TODO add SI. Implement from book
def op(I, I0, U0, UA0, eps):
    U = next(iter(I.free_symbols))
    Gi = I0 / U0
    gn = sympy.diff(I, U)

    df = pd.DataFrame(columns=('n', 'UAn, В', 'IAn, А', 'gAn, См', '|UAn+1 - Un|, В'))
    UAn = UA0
    n = 0
    while True:
        IAn = I.subs(U, UAn)
        gAn = gn.subs(U, UAn)

        UAp = UAn
        UAn = (UAn * gAn + I0 - IAn) / (Gi + gAn)

        df.loc[len(df)] = (n, UAp, IAn, gAn, abs(UAn - UAp))

        n = n + 1
        if abs(UAn - UAp) <= eps:
            break

    return df


#FIXME use phase
def harmonics(exp, n, limits):
    fs = sympy.fourier_series(exp, limits=limits)

    t = limits[0]

    coeffs = [fs.a0]
    for i in range(1, n + 1):
        if type(fs.an) is sympy.Dict:
            a = fs.an[i] if i in fs.an else 0
            b = fs.bn[i] if i in fs.bn else 0
        else:
            a = fs.an.coeff(i).subs(t, 0)
            b = fs.bn.coeff(i).subs(t, 1 / (4 * i))

        A = sympy.sqrt(a ** 2 + b ** 2)
        coeffs.append(A)

    return coeffs


def effective(harmonics):
    eff = 0
    for h in harmonics:
        eff += (h / sympy.sqrt(2)) ** 2

    return sympy.sqrt(eff)


def distortion_coeff(eff1, eff):
    return sympy.sqrt(1 - (eff1 / eff) ** 2)