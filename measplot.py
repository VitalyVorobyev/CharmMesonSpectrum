#! /usr/bin/env python

import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 18})

from measlist import MEAS

def oplus(*args):
    return np.sqrt(np.sum(x**2 for x in args))

COLORS = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

SHAPES = {
    'undef': 'o',
    r'$0^+$': 'v',
    r'$0^-$': '^',
    r'$1^+$': 'd',
    r'$1^-$': 's',
    r'$3^-$': '*',
    r'un': r'$U$',
    r'n': r'$N$',
}

def get_color():
    for col in itertools.cycle(COLORS):
        yield col

def error(mitem):
    stat = max(mitem['stat']) if isinstance(mitem['stat'], list) else mitem['stat']
    syst = max(mitem['syst']) if isinstance(mitem['syst'], list) else mitem['syst']
    return oplus(stat, syst)

def make_df():
    df = pd.DataFrame(MEAS)
    df = df[df.used & df.apply(lambda x: x.width is not None, axis=1)]
    df['merr'] = df.apply(lambda x: error(x.mass), axis=1)
    df['werr'] = df.apply(lambda x: error(x.width), axis=1)
    df['mval'] = df.apply(lambda x: x.mass['value'], axis=1)
    df['wval'] = df.apply(lambda x: x.width['value'], axis=1)
    return df


def mplot():
    df = make_df()
    colgen = get_color()
    plt.figure(figsize=(12, 8))
    for pdgid, df0 in df.groupby('pdg'):
        col = next(colgen)
        for jp, df1 in df0.groupby('JP'):
            plt.errorbar(df1.mval, df1.wval, xerr=df1.merr, yerr=df1.werr,
                     markersize=14, marker=SHAPES[jp], color=col, fillstyle='none',
                     linestyle='none', label=pdgid + ' ' + jp)
    plt.minorticks_on()
    plt.grid(which='major')
    plt.grid(which='minor', linestyle='--')
    plt.legend(fontsize=14)
    plt.xlabel('Mass, MeV')
    plt.ylabel('Width, MeV')
    plt.tight_layout()

    for ext in ['png', 'svg', 'pdf']:
        plt.savefig(f'plots/mspec.{ext}')

    plt.show()

def main():
    mplot()

if __name__ == '__main__':
    main()
