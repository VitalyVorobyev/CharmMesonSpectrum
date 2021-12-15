#! /usr/bin/env python

from acpdata import *

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.size'] = 14


def hflav_average(ds, key):
    lbls = np.array(list(ds.keys()))
    data = np.array([item[0] for item in ds.values()])
    print(data)
    vals, errs = data[:, 0], data[:, 1]
    perm = np.argsort(errs)
    lbls, vals, errs = [item[perm] for item in [lbls, vals, errs]]

    xticks = np.arange(len(lbls))
    plt.figure(figsize=(12, 6))
    plt.xticks(xticks, lbls, rotation=50)
    plt.ylabel('CP asymmetry')
    plt.xlabel('Process')
    plt.errorbar(xticks, vals, yerr=errs, linestyle='none', marker='o')
    plt.grid(which='major')
    plt.grid(which='minor', linestyle=':')
    plt.ylim((-0.05, 0.05))
    # plt.semilogy()
    plt.tight_layout()
    plt.savefig(f'plots/acp_{key}.pdf')


def hflav_precision(ds, key, lbl):
    lbls = np.array(list(ds.keys()))
    data = np.array([item[0][1] for item in ds.values()])
    perm = np.argsort(data)
    lbls, data = [item[perm] for item in [lbls, data]]
    xticks = np.arange(len(lbls))

    sctx, scty = [], []
    for idx, l in enumerate(lbls):
        scterr = sct_projection(ds[l][1])
        if scterr:
            sctx.append(idx)
            scty.append(scterr)

    plt.figure(figsize=(12, 6))
    plt.xticks(xticks, lbls, rotation=50)
    plt.ylabel('CP asymmetry precision')
    plt.plot(xticks, data, linestyle='none', marker='o', label='HFLAV 2021')
    plt.plot(sctx, scty, linestyle='none', marker='o', label=lbl)
    plt.legend(fontsize=18)
    plt.grid(which='major')
    plt.grid(which='minor', linestyle=':')
    plt.semilogy()
    plt.tight_layout()
    plt.savefig(f'plots/acp_precision_{key}.pdf')


def sct_projection(ds, lumi=1000):
    for rec in ds:
        if rec[1] == 'CLEOc':
            (_, err1, err2), lumi0 = rec[-2], rec[-1]
            return np.hypot(err1, err2) * np.sqrt(lumi0 / lumi)
    return None


if __name__ == '__main__':
    hflav_precision(acpdata_dn, 'dn', r'SCT $1~ab^{-1}$ @ 3.77 GeV')
    hflav_precision(acpdata_dp, 'dp', r'SCT $1~ab^{-1}$ @ 3.77 GeV')
    hflav_precision(acpdata_ds, 'ds', r'SCT $1~ab^{-1}$ @ 4.17 GeV')

    plt.show()
