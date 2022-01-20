#! /usr/bin/env python

from colors import pycol_gen
from states import STATES, PREDICTIED, PREDICTIED_DS

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.size'] = 18

kmass = 493.677 # K+
thresholds = {
    'd0k+': [r'$D^0K^+$', STATES['S032']['massPDG'][0] + kmass],
    'd*0k+': [r'$D^{*0}K^+$', STATES['M061']['massPDG'][0] + kmass],
}

def state2line(st):
    if 'S' in st:
        return [0.7, 1.3], 'S'
    if 'P' in st:
        return [2.7, 3.3], 'P'
    if 'D' in st:
        return [4.7, 5.3], 'D'
    if 'F' in st:
        return [6.7, 7.3], 'F'
    return [8.7, 9.3], 'X'

def godfrey_plot():
    cgen = pycol_gen()
    col1, col2 = next(cgen), next(cgen)

    plt.figure(figsize=(8, 10))

    plt.plot([5, 5], [2400, 2400], '--', color=col1,
             label=r'Potential model for $c\bar{q}$')
    plt.plot([5, 5], [2400, 2400], ':', color=col2,
             label=r'Potential model for $c\bar{s}$')

    for state, [name, mass] in PREDICTIED.items():
        plt.plot(state2line(state)[0], [mass, mass], '--', color=col1)

    for state, [name, mass] in PREDICTIED_DS.items():
        x = state2line(state)[0]
        plt.plot([x[0] + 0.6, x[1] + 0.6], [mass, mass], ':', color=col2)

    x, y, yerr = [], [], []
    xs, ys, yerrs = [], [], []
    cnt = {'S': -0.4, 'P': -0.4, 'D': -0.35, 'F': -0.15}
    cnts = {'S': -0.23, 'P': -0.4, 'D': -0.23, 'F': -0.15}
    for _, data in STATES.items():
        mass, dmass = data['massPDG']
        spdf, lbl = state2line(data['assignment'])

        if 's' in data['name']:
            if '2' == data['assignment'][1]:
                cnts[lbl] = -0.15
            cnts[lbl] += 0.15
            xs.append(spdf[0] + 0.9 + cnts[lbl])
            ys.append(mass)
            yerrs.append(dmass)
        else:
            if '2' == data['assignment'][1]:
                cnt[lbl] = -0.15
            cnt[lbl] += 0.15
            x.append(spdf[0] + 0.3 + cnt[lbl])
            y.append(mass)
            yerr.append(dmass)

    plt.errorbar(x, y, yerr=yerr, fmt='o', color=col1, markersize=7,
                 label=r'Observed $c\bar{q}$')
    plt.errorbar(xs, ys, yerr=yerrs, fmt='D', color=col2, markersize=7,
                 label=r'Observed $c\bar{s}$')

    xlabels = [fr'${item}$' for item in 'SPDF']
    xticks = [1.3, 3.3, 5.3, 7.3]

    for _, thr in thresholds.items(): 
        plt.plot((0, 8.5), [thr[1], thr[1]], 'k--', alpha=0.6)
        plt.text(7, thr[1], thr[0])

    plt.legend()

    plt.xticks(xticks, xlabels)
    plt.xlim((0, 8.5))
    plt.xlabel('Angular moment')
    plt.ylabel('Mass (MeV)')
    plt.minorticks_on()
    plt.grid(which='major')
    plt.grid(which='minor', linestyle=':')
    plt.tight_layout()
    plt.savefig('plots/d-meson-spec.pdf')


if __name__ == '__main__':
    godfrey_plot()
    plt.show()
