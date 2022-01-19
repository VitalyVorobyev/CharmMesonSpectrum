#! /usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.size'] = 16

# PhysRevD.97.072004
# 3.93 1/fb @ sqrts = 3773 MeV
besbrs = [
    [r'$D^+\to \pi^+\pi^0$', (10108, 267), (49.0, 0.3), (1.259, 0.033, 0.023), (1.24, 0.06)],
    [r'$D^+\to K^+\pi^0$', (1834, 168), (48.2, 0.4), (0.232, 0.021, 0.006), (0.189, 0.025)],
    [r'$D^+\to \pi^+\eta$', (11636, 215), (47.0, 0.3), (3.790, 0.070, 0.068), (3.66, 0.22)],
    [r'$D^+\to K^+\eta$', (439, 72), (44.6, 0.3), (0.151, 0.025, 0.014), (0.112, 0.018)],
    [r'$D^+\to \pi^+η^\prime$', (3088, 83), (21.5, 0.2), (5.12, 0.14, 0.024), (4.84, 0.31)],
    [r'$D^+\to K^+\eta^\prime$', (87, 25), (18.8, 0.2), (0.164, 0.051, 0.024), (0.183, 0.023)],
    [r'$D^+\to K_S^0\pi^+$', (93883, 352), (51.4, 0.2), (15.91, 0.06, 0.30), (15.3, 0.6)],
    [r'$D^+\to K_S^0K^+$', (17704, 151), (48.5, 0.1), (3.183, 0.029, 0.060), (2.95, 0.15)],
    [r'$D^0\to \pi^+\pi^-$', (21107, 249), (66.0, 0.3), (1.508, 0.018, 0.022), (1.421, 0.025)],
    [r'$D^0\to K^+K^-$', (56359, 272), (62.8, 0.3), (4.233, 0.021, 0.064), (4.01, 0.07)],
    [r'$D^0\to K^{\mp}\pi^{\pm}$', (534135, 759), (64.7, 0.1), (38.98, 0.06, 0.51), (39.4, 0.4)],
    [r'$D^0\to K_S^0\pi^0$', (66552, 302), (37.1, 0.2), (12.39, 0.06, 0.27), (12.0, 0.4)],
    [r'$D^0\to K_S^0\eta$', (9485, 126), (32.0, 0.1), (5.13, 0.07, 0.12), (4.85, 0.30)],
    [r'$D^0\to K_S^0\eta^\prime$', (2978, 61), (12.7, 0.1), (9.49, 0.20, 0.36), (9.5, 0.5)],
]


def values_plot():
    data = np.array([x[3] for x in besbrs]) * 1.e-3
    perm = np.argsort(data[:, 0])[::-1]
    lbls = [besbrs[perm[i]][0] for i in range(perm.size)]
    data = data[perm]

    xticks = np.arange(len(lbls))
    plt.figure(figsize=(8, 6))
    vals = data[:, 0]
    errs = np.sqrt(np.sum(data[:, 1:]**2, axis=1))
    plt.xticks(xticks, lbls, rotation=50)
    plt.ylabel('Absolute branching')
    plt.xlabel('Process')
    plt.errorbar(xticks, vals, yerr=errs, linestyle='none', marker='o')
    plt.grid(which='major')
    plt.grid(which='minor', linestyle=':')
    plt.semilogy()
    plt.tight_layout()
    plt.savefig('plots/charm-branch-val.pdf')


def errors_plot():
    data = np.array([x[3] for x in besbrs]) * 1.e-3
    perm = np.argsort(data[:, 0])[::-1]
    lbls = [besbrs[perm[i]][0] for i in range(perm.size)]
    data = data[perm]
    errs = np.sqrt(np.sum(data[:, 1:]**2, axis=1))

    coef = np.sqrt(3.93 / 10**3)

    xticks = np.arange(len(lbls))
    plt.figure(figsize=(8, 6))
    plt.xticks(xticks, lbls, rotation=50)
    plt.ylabel('Absolute branching precision')
    plt.xlabel('Process')
    plt.plot(xticks, errs, linestyle='none', marker='o',
             label='BESIII @ 3.93 1/fb')
    plt.plot(xticks, errs * coef, linestyle='none', marker='o',
             label='SCT @ 1 1/ab')
    plt.grid(which='major')
    plt.grid(which='minor', linestyle=':')
    plt.legend(fontsize=18)
    plt.semilogy()
    plt.tight_layout()
    plt.savefig('plots/charm-branch-err.pdf')


if __name__ == '__main__':
    values_plot()
    errors_plot()
    plt.show()

