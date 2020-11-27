def pub_item(doi, ref, year, exp):
    return {'doi': doi, 'ref': ref, 'year': year, 'exp': exp}

PUBS = {
    'LINK 04A' : pub_item(
        'https://doi.org/10.1016/j.physletb.2004.02.017',
        'Phys. Lett. B586 (2004) 11', 2004, 'FOCUS',
    ),
    'ABE 04D' : pub_item(
        'https://doi.org/10.1103/PhysRevD.69.112002',
        'Phys. Rev. D 69 (2004) 112002', 2004, 'Belle',
    ),
    'AUBERT 09AB' : pub_item(
        'https://doi.org/10.1103/PhysRevD.79.112004',
        'Phys. Rev. D 79 (2009) 112004', 2009, 'BaBar',
    ),
    'AAIJ 15Y' : pub_item(
        'https://doi.org/10.1103/PhysRevD.92.032002',
        'Phys. Rev. D 92 (2015) 032002', 2015, 'LHCb'
    ),
    'AAIJ 15X' : pub_item(
        'https://doi.org/10.1103/PhysRevD.92.012012',
        'Phys. Rev. D 92 (2015) 012012', 2015, 'LHCb'
    ),
    'ANJOS 89C': pub_item(
        'https://doi.org/10.1103/PhysRevLett.62.1717',
        'Phys. Rev. Lett 62 (1989) 1717', 1989, 'E691'
    ),
    'BERGFELD 94B': pub_item(
        'https://doi.org/10.1016/0370-2693(94)01348-9',
        'Phys. Lett. B 331 (1994) 236', 1994, 'CLEO'
    ),
    'ABE 05A': pub_item(
        'https://doi.org/10.1103/PhysRevLett.94.221805',
        'Phys. Rev. Lett. 94 (2005) 221805', 2005, 'Belle'
    ),
    'AUBERT 09Y': pub_item(
        'https://doi.org/10.1103/PhysRevLett.103.051803',
        'Phys. Rev. Lett. 103 (2009) 051803', 2009, 'BaBar'
    ),
    'ABRAMOWICZ 13': pub_item(
        'https://doi.org/10.1016/j.nuclphysb.2012.09.007',
        'Nucl. Phys. B. 866 (2013) 229', 2013, 'ZEUS'
    ),
    'ABLIKIM 20P': pub_item(
        'https://doi.org/10.1016/j.physletb.2020.135395',
        'Phys. Lett. B 804 (2020) 135395', 2020, 'BESIII'
    ),
    'DEL-AMO-SA... 10P': pub_item(
        'https://doi.org/10.1103/PhysRevD.82.111101',
        'Phys. Rev. D 82 (2010) 111101(R)', 2010, 'BaBar'
    ),
    'AAIJ 13CC': pub_item(
        'https://doi.org/10.1007/JHEP09(2013)145',
        'JHEP 09 (2013) 145', 2013, 'LHCb'
    ),
    'AAIJ 16AH': pub_item(
        'https://doi.org/10.1103/PhysRevD.94.072001',
        'Phys. Rev. D 94 (2016) 072001', 2016, 'LHCb'
    ),
}
