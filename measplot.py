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


def states_legend(ax, byname=True, x=0, y=0, marker='o', size=10, fontsize=14, loc='best', ncol=1, select=None):
    handles = []
    for code, info in STATES.items():
        if select and code not in select:
            continue
        handles.append(
            ax.plot([x], [y], linestyle='none', color=info['color'], marker=marker,
            markersize=size, label=info['name'] if byname else code)[0]
        )
    ax.add_artist(ax.legend(handles=handles, fontsize=fontsize, loc=loc, ncol=ncol))


def jp_legend(ax, x=0, y=0, color='k', size=10, fillstyle='full', fontsize=14, loc='best', select=None):
    handles = []
    for jp, shape in SHAPES.items():
        if select and jp not in select:
            continue
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

def mplot(byname=False, select=None, xlim=(1950, 3550), ylim=(0, 500), figsize=(12, 8)):
    df = make_df()
    fig, ax = plt.subplots(figsize=figsize)
    states_legend(ax, byname=byname, size=10, fontsize=14, select=select)
    jps = set()
    for pdgid, df0 in df.groupby('pdg'):
        if select and pdgid not in select:
            continue
        for jp, df1 in df0.groupby('JP'):
            jps.add(jp)
            ax.errorbar(
               df1.mval, df1.wval, xerr=df1.merr, yerr=df1.werr, linestyle='none', markersize=14,
               marker=SHAPES[jp], color=STATES[pdgid]['color'], fillstyle='none')
    
    print(jps)
    jp_legend_location = (0.695, 1 - 0.05 * len(jps)) if byname else (0.745, 1 - 0.05 * len(jps))
    jp_legend(ax, fillstyle='none', size=10, fontsize=14, loc=jp_legend_location, select=jps)

    ax.minorticks_on()
    ax.set_ylim(ylim)
    ax.set_xlim(xlim)
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

def average_plot(select=None, xlim=(1950, 3550), ylim=(0, 500), figsize=(12, 8)):
    data = averaged_meas(pd.DataFrame(MEAS).dropna())
    fig, ax = plt.subplots(figsize=figsize)
    ylo, yhi, delta = 0, ylim[-1], ylim[-1] // 10

    def posgen(n=4):
        for i in range(100):
            yield yhi - delta * (i%n + 1)

    pg = posgen(7)
    next(pg)
    for pdgid, item in data.items():
        if select and pdgid not in select:
            continue
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
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.grid(which='major')
    ax.grid(which='minor', linestyle='--')
    ax.legend(fontsize=14, ncol=1, loc='lower right')
    ax.set_xlabel('Mass, MeV')
    ax.set_ylabel('Width, MeV')
    fig.tight_layout()

    for ext in ['png', 'svg', 'pdf']:
        plt.savefig(f'plots/averaged.{ext}')


def excl_vs_incl(byname=True, fillstyle='none', select=None, xlim=(2200, 3300), ylim=(0, 400), figsize=(12, 8)):
    data = pd.DataFrame(MEAS).dropna()
    fig, ax = plt.subplots(figsize=figsize)
    states_legend(ax, byname=byname, size=10, fontsize=14, ncol=3, select=select)
    inex_legend_location = (0.885, 0.60)
    inex_legend(ax, fillstyle=fillstyle, size=10, fontsize=14, loc=inex_legend_location)
    for incl, df in data.groupby('incl'):
        shape = 'o' if incl else 'd'
        for pdgid, item in averaged_meas(df).items():
            if select and pdgid not in select:
                continue
            mass, width = item['mass'], item['width']
            chisq, ndf = mass[2] + width[2], mass[3] + width[3]
            print(f'{pdgid} {incl:d}: {chisq:.1f}/{ndf}')
            ax.errorbar(
                mass[0], width[0], xerr=mass[1], yerr=width[1], markersize=8, color=STATES[pdgid]['color'],
                marker=shape, linestyle='none', fillstyle=fillstyle)

    ax.minorticks_on()
    ax.set_ylim(ylim)
    ax.set_xlim(xlim)
    ax.grid(which='major')
    ax.grid(which='minor', linestyle='--')
    ax.set_xlabel('Mass, MeV')
    ax.set_ylabel('Width, MeV')
    fig.tight_layout()

    for ext in ['png', 'svg', 'pdf']:
        plt.savefig(f'plots/excl_incl.{ext}')


def main():
    select = ['M178', 'M179', 'M097', 'M120', 'M119', 'M150']
    xlim = (2250, 2520)
    ylim = (0, 350)
    figsize=(10, 7)
    mplot(byname=True, select=select, xlim=xlim, ylim=ylim)
    average_plot(select=select, xlim=xlim, ylim=ylim)
    excl_vs_incl(select=select, xlim=xlim, ylim=ylim)
    plt.show()

if __name__ == '__main__':
    main()
