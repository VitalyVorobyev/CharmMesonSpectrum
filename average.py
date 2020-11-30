#! /usr/bin/env python
""" Tools for averaging mutiple measurements """

import numpy as np
import pandas as pd

def oplus(*args):
    return np.sqrt(np.sum((np.fromiter((x**2 for x in args), dtype=np.float))))

def maxerr(err):
    return max(err) if isinstance(err, list) else err

def full_err(item):
    return oplus(maxerr(item['stat']), maxerr(item['syst']))

def average(mlist):
    if len(mlist) == 1:
        return (mlist[0]['value'], full_err(mlist[0]), 0, 1)
    vals = np.array([item['value'] for item in mlist])
    errs = np.array(list(map(full_err, mlist)))
    mval = np.average(vals, weights=1./ errs**2)
    errn = np.sum(errs**-2)**-0.5
    chisq = np.sum(((vals - mval) / errs)**2)
    # pval = stats.chisquare(f_obs=chisq, ddof=vals.size)[1]
    return (mval, errn, chisq, vals.size)

def averaged_meas(df):
    return {pdgid : {
            'mass': average(data.mass.to_numpy()),
            'width': average(data.width.to_numpy()),
        } for pdgid, data in df.groupby('pdg')}

def meas_df(mlist):
    df = pd.DataFrame(mlist).dropna()
    averaged_meas(df)

def main():
    from measlist import MEAS
    meas_df(MEAS)

if __name__ == '__main__':
    main()
