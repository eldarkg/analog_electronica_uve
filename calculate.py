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
