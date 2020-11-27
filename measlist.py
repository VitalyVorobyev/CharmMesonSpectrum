
def mval(val, stat, syst):
    return {
        'value': val,
        'stat': stat,
        'syst': syst,
    }

def meas_item(pub, charge, incl, fState, jp, mass, width, process, yld, pdg, used):
    return {
        'pub': pub,
        'charge': charge,
        'incl': incl,
        'finalState': fState,
        'JP': jp,
        'mass': mass,
        'width': width,
        'process': process,
        'yield': yld,
        'pdg': pdg,
        'used': used,
    }

MEAS = [
    meas_item(*args) for args in [
        #   pub           q  incl      finalState        JP     mass                width                     process                         yield   PDG    used
        ['LINK 04A'     , 0, True,  r'$D^+\pi^-$',         None, mval(2407, 21, 35), mval(240, 55, 59),     r'$A\gamma$'                    ,  None, 'M178', False], # M179
        ['ABE 04D'      , 0, False, r'$D^+\pi^-$',     r'$0^+$', mval(2308, 17, 32), mval(240, 55, 59),     r'$B^-\to D^+\pi^-\pi^+$'       , 1.1e3, 'M178', True],
        ['AUBERT 09AB'  , 0, False, r'$D^+\pi^-$',     r'$0^+$', mval(2297,  8, 20), mval(273, 12, 48),     r'$B^-\to D^+\pi^-\pi^+$'       , 3.4e3, 'M178', True],  # M178
        ['LINK 04A'     , 1, True,  r'$D^0\pi^-$',         None, mval(2403, 14, 35), mval(283, 24, 34),     r'$A\gamma$'                    ,  None, 'M179', False],
        ['AAIJ 15Y'     , 1, False, r'$D^0\pi^-$',     r'$0^+$', mval(2349,  6,  4), mval(217, 13, 13),     r'$B^0\to \bar{D}^0\pi^-\pi^+$' , 9.6e3, 'M179', True],
        ['AAIJ 15X'     , 1, False, r'$D^0\pi^-$',     r'$0^+$', mval(2360, 15, 30), mval(255, 26, 51),     r'$B^0\to \bar{D}^0\pi^-K^+$'   , 2.6e3, 'M179', True],
        ['ANJOS 89C'    , 1, True,  r'$D^{*0}\pi^+$',      None, mval(2443,  7,  5), mval( 49, 19,  8),     r'$\gamma N\to D^{*0}\pi^+X^0$' ,   190, 'M120', True],  # M120
        ['BERGFELD 94B' , 1, True,  r'$D^{*0}\pi^+$',      None, mval(2425,  2,  2), mval( 26, [7, 8],  4), r'$e^+e^-\to D^{*0}\pi^+X$'     ,   146, 'M120', True],
        ['ABE 05A'      , 1, False, r'$D^+\pi^+\pi^-$',    None, mval(2421,  2,  1), mval( 21,  5,  8),     r'$\bar{B}^0\to D^+\pi^+2\pi^-$',   124, 'M120', True],
        ['ABRAMOWICZ 13', 1, True,  r'$D^{*0}\pi^-$',      None, mval(2421.9, 4.7, [1.2, 3.4]), None,       r'$e^{\pm}p\to D^{(*)0}\pi^+X$' ,   759, 'M120', True],
    ]
]

NOTES = [
    """ M179: remove 'J, P need confirmation' from header """,
    """ M120: ANJOS 89C comment: "D0 pi+" -> "D*0 pi+" """,
]
