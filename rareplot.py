#! /usr/bin/env python

from rarecharmdata import rare_dn, rare_dp, rare_ds
from rarecharmdata import lfv_dn, lfv_dp, lfv_ds
from colors import pycol_gen

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.size'] = 16


def rare_plot(ds, modes, fname):
    modesidx = {item: idx for idx, item in enumerate(modes)}
    data = {}
    ctau = set(['BESIII', 'CLEOc'])
    sctl = r'SCT @ 1 ab${}^{-1}$'
    for mode, recs in ds.items():
        labeled = {item[1]: item for item in recs}
        if ctau & labeled.keys():
            data[mode] = {}
            key = 'BESIII' if 'BESIII' in labeled else 'CLEOc'
            uplim = labeled[key][0]
            lumi = labeled[key][-1]
            # print(labeled[key])
            data[mode][sctl] = uplim * np.sqrt(lumi / 10**3)
            data[mode][recs[-1][1]] = recs[-1][0]

    plt.figure(figsize=(7 * len(data) / 8, 6))
    cgen = pycol_gen()
    cmap = {key: next(cgen) for key in
            ['BESIII', sctl, 'CLEOc', 'Belle', 'BaBar', 'LHCb']}
    lbls = set()
    for mode, vals in data.items():
        for label, uplim in vals.items():
            if label in lbls:
                plt.scatter(modesidx[mode], [uplim * 10**-6], c=cmap[label])
            else:
                lbls.add(label)
                plt.scatter(modesidx[mode], [uplim * 10**-6], c=cmap[label], label=label)

    xticks = np.arange(len(modes))
    plt.xticks(xticks, modes, rotation=40)
    plt.ylabel('Branching upper limit')
    plt.grid(which='major')
    plt.grid(which='minor', linestyle=':')
    plt.ylim(1e-8, 2e-4)
    plt.semilogy()

    plt.legend()
    plt.tight_layout()
    plt.savefig(f'plots/{fname}.pdf')
    plt.show()

def strip_val(v):
    return v[0] if isinstance(v, tuple) else v

def preprocess_data():
    ctau = set(['BESIII', 'CLEOc'])

    def aux(ds, key, rdata, rmodes):
        for mode, data in ds.items():
            if ctau & set([item[1] for item in data]):
                newmode = fr'${key} \to $' + mode
                rdata[newmode] = data
                rmodes.append([newmode, strip_val(data[-1][0])])

    rare_data = dict()
    rare_modes = []
    aux(rare_dn, 'D^0', rare_data, rare_modes)
    aux(rare_dp, 'D^+', rare_data, rare_modes)
    aux(rare_ds, 'D_s^+', rare_data, rare_modes)

    lfv_data = dict()
    lfv_modes = []
    aux(lfv_dn, 'D^0', lfv_data, lfv_modes)
    aux(lfv_dp, 'D^+', lfv_data, lfv_modes)
    aux(lfv_ds, 'D_s^+', lfv_data, lfv_modes)

    rare_modes = [item[0] for item in sorted(rare_modes, key=lambda x: x[1])]
    lfv_modes = [item[0] for item in sorted(lfv_modes, key=lambda x: x[1])]

    return (rare_data, rare_modes), (lfv_data, lfv_modes)

if __name__ == '__main__':
    (rare_data, rare_modes), (lfv_data, lfv_modes) = preprocess_data()
    rare_plot(rare_data, rare_modes, 'rare_limits')
    rare_plot(lfv_data, lfv_modes, 'lfv_limits')
