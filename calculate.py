import pandas as pd
import sympy

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


def harmonics(exp, n, limits):
    fs = sympy.fourier_series(exp, limits=limits)

    t = limits[0]

    coeffs = [fs.a0]
    for i in range(1, n + 1):
        a = fs.an.coeff(i).subs(t, 0)
        b = fs.bn.coeff(i).subs(t, 1 / (4 * i))
        A = sympy.sqrt(a ** 2 + b ** 2)
        coeffs.append(A)

    return coeffs