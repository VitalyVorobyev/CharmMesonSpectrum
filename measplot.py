#! /usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 18})

from measlist import MEAS
from states import PREDICTIED, STATES
from average import averaged_meas, oplus

SHAPES = {
    'undef': 'o',
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

def states_legend(ax, byname=True, x=0, y=0, marker='o', size=10, fontsize=14, loc='best', ncol=1):
    handles = []
    for code, info in STATES.items():
        handles.append(
            ax.plot([x], [y], linestyle='none', color=info['color'], marker=marker,
            markersize=size, label=info['name'] if byname else code)[0]
        )
    ax.add_artist(ax.legend(handles=handles, fontsize=fontsize, loc=loc, ncol=ncol))

def jp_legend(ax, x=0, y=0, color='k', size=10, fillstyle='full', fontsize=14, loc='best'):
    handles = []
    for jp, shape in SHAPES.items():
        handles.append(
            ax.plot([x], [y], linestyle='none', color=color, fillstyle=fillstyle,
                    marker=shape, markersize=size, label=jp)[0]
        )
    ax.add_artist(ax.legend(handles=handles, fontsize=fontsize, loc=loc))

def inex_legend(ax, shapes=['o', 'd'], x=0, y=0, color='k', size=10, fillstyle='full', fontsize=14, loc='best'):
    handles = []
    for lbl, m in zip(['incl', 'excl'], shapes):
        handles.append(
            ax.plot([x], [y], linestyle='none', color=color, fillstyle=fillstyle,
                    marker=m, markersize=size, label=lbl)[0]
        )
    ax.add_artist(ax.legend(handles=handles, fontsize=fontsize, loc=loc))

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

def mplot(byname=False):
    df = make_df()
    fig, ax = plt.subplots(figsize=(12, 8))
    states_legend(ax, byname=byname, size=10, fontsize=14)
    jp_legend_location = (0.695, 0.54) if byname else (0.745, 0.54)
    jp_legend(ax, fillstyle='none', size=10, fontsize=14, loc=jp_legend_location)
    for pdgid, df0 in df.groupby('pdg'):
        for jp, df1 in df0.groupby('JP'):
            ax.errorbar(
               df1.mval, df1.wval, xerr=df1.merr, yerr=df1.werr, linestyle='none', markersize=14,
               marker=SHAPES[jp], color=STATES[pdgid]['color'], fillstyle='none')
    ax.minorticks_on()
    ax.set_ylim((0, 500))
    ax.set_xlim((1950, 3550))
    ax.grid(which='major')
    ax.grid(which='minor', linestyle='--')
    ax.set_xlabel('Mass, MeV')
    ax.set_ylabel('Width, MeV')
    fig.tight_layout()

    ofname = 'mspec_byname' if byname else 'mspec_byid'
    for ext in ['png', 'svg', 'pdf']:
        plt.savefig(f'plots/{ofname}.{ext}')

def plot_potential_predictions(ax, ylo=0, yhi=500, delta=25, fsize=14):
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
    ylo, yhi, delta = 0, 500, 25

    def posgen(n=4):
        for i in range(100):
            yield yhi - delta * (i%n + 1)

    pg = posgen(7)
    next(pg)
    for pdgid, item in data.items():
        mass, width = item['mass'], item['width']
        chisq, ndf = mass[2] + width[2], mass[3] + width[3]
        col = STATES[pdgid]['color']
        ax.errorbar(
            mass[0], width[0], xerr=mass[1], yerr=width[1], markersize=8, linestyle='none',
            marker=SHAPES[STATES[pdgid]['jp']], color=col,
            label=rf'{STATES[pdgid]["name"]} (${chisq:.1f}/{ndf}$)')
        if STATES[pdgid]['assignment'] in PREDICTIED:
            key = STATES[pdgid]['assignment']
            lbl, pos = PREDICTIED[key]
            ax.plot([pos, pos], [ylo, yhi], color=col, linestyle=':')
            ax.text(pos, next(pg), fr'{lbl}({key})', color=col, fontsize=14)

    ax.minorticks_on()
    ax.set_ylim((0, 500))

    ax.set_xlim((1950, 3550))
    ax.grid(which='major')
    ax.grid(which='minor', linestyle='--')
    ax.legend(fontsize=14, ncol=1, loc='lower right')
    ax.set_xlabel('Mass, MeV')
    ax.set_ylabel('Width, MeV')
    fig.tight_layout()

    for ext in ['png', 'svg', 'pdf']:
        plt.savefig(f'plots/averaged.{ext}')


def excl_vs_incl(byname=True, fillstyle='none'):
    data = pd.DataFrame(MEAS).dropna()
    fig, ax = plt.subplots(figsize=(12, 8))
    states_legend(ax, byname=byname, size=10, fontsize=14, ncol=3)
    inex_legend_location = (0.885, 0.60)
    inex_legend(ax, fillstyle=fillstyle, size=10, fontsize=14, loc=inex_legend_location)
    for incl, df in data.groupby('incl'):
        shape = 'o' if incl else 'd'
        for pdgid, item in averaged_meas(df).items():
            mass, width = item['mass'], item['width']
            chisq, ndf = mass[2] + width[2], mass[3] + width[3]
            print(f'{pdgid} {incl:d}: {chisq:.1f}/{ndf}')
            ax.errorbar(
                mass[0], width[0], xerr=mass[1], yerr=width[1], markersize=8, color=STATES[pdgid]['color'],
                marker=shape, linestyle='none', fillstyle=fillstyle)

    ax.minorticks_on()
    ax.set_ylim((0, 400))

    ax.set_xlim((2200, 3300))
    ax.grid(which='major')
    ax.grid(which='minor', linestyle='--')
    ax.set_xlabel('Mass, MeV')
    ax.set_ylabel('Width, MeV')
    fig.tight_layout()

    for ext in ['png', 'svg', 'pdf']:
        plt.savefig(f'plots/excl_incl.{ext}')


def main():
    # mplot(byname=True)
    # average_plot()
    excl_vs_incl()
    plt.show()

if __name__ == '__main__':
    main()
