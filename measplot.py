#! /usr/bin/env python

import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 18})

# matplotlib.rc ('text', usetex=False)
# font = {'family' : "serif",
#         'weight' : 'normal',
#         'size' : 18}
# matplotlib.rc ("font", **font)

from measlist import MEAS
from states import PREDICTIED, STATES
from average import averaged_meas

def oplus(*args):
    return np.sqrt(np.sum(x**2 for x in args))

COLORS = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

SHAPES = {
    'undef': 'o',
    'unkn': 'o',
    r'$0^+$': 'v',
    r'$0^-$': '^',
    r'$1^+$': 'd',
    r'$1^-$': 's',
    r'$2^+$': 'P',
    r'$2^-$': 'X',
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
    plt.ylim((0, 500))

    plt.xlim((1950, 3550))
    plt.grid(which='major')
    plt.grid(which='minor', linestyle='--')
    plt.legend(fontsize=14, ncol=3)
    plt.xlabel('Mass, MeV')
    plt.ylabel('Width, MeV')
    plt.tight_layout()

    for ext in ['png', 'svg', 'pdf']:
        plt.savefig(f'plots/mspec.{ext}')

    plt.show()

def plot_potential_predictions(ax, ylo=0, yhi=500, delta=25, fsize=12):
    def posgen():
        cols = ['b', 'r', 'k', 'g']
        for i in range(100):
            yield (yhi - delta * (i%len(cols) + 1), cols[i % len(cols)])

    pg = posgen()
    for key, [lbl, pos] in PREDICTIED.items():
        y, col = next(pg)
        ax.plot([pos, pos], [ylo, yhi], color=col, linestyle=':')
        ax.text(pos, y, fr'{lbl}({key})', color=col, fontsize=fsize)

def average_plot():
    data = averaged_meas(pd.DataFrame(MEAS).dropna())
    fig, ax = plt.subplots(figsize=(12, 8))

    for pdgid, item in data.items():
        mass, width = item['mass'], item['width']
        chisq = (mass[2] + width[2]) / (mass[3] + width[3])
        ax.errorbar(
            mass[0], width[0], xerr=mass[1], yerr=width[1],
            markersize=8, marker=SHAPES[STATES[pdgid]['jp']], linestyle='none',
            label=f'{STATES[pdgid]["name"]} ({chisq:.2f})')
    plot_potential_predictions(ax)

    ax.minorticks_on()
    ax.set_ylim((0, 500))

    ax.set_xlim((1950, 3550))
    ax.grid(which='major')
    ax.grid(which='minor', linestyle='--')
    ax.legend(fontsize=14, ncol=1)
    ax.set_xlabel('Mass, MeV')
    ax.set_ylabel('Width, MeV')
    fig.tight_layout()

    for ext in ['png', 'svg', 'pdf']:
        plt.savefig(f'plots/averaged.{ext}')

    plt.show()

def main():
    # mplot()
    average_plot()

if __name__ == '__main__':
    main()
