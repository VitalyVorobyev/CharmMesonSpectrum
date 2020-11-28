import numpy as np

def oplus(*args):
    return np.sqrt(np.sum(x**2 for x in args))

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
        #   pub               q  incl      finalState        JP      mass                     width                       process                         yield   PDG    used
        ['LINK 04A'         , 0,  True, r'$D^+\pi^-$',      'undef', mval(2407,  21,  35),    mval(240, 55, 59),       r'$A\gamma$'                    ,   None, 'M178', False], # M179
        ['ABE 04D'          , 0, False, r'$D^+\pi^-$',     r'$0^+$', mval(2308,  17,  32),    mval(240, 55, 59),       r'$B^-\to D^+\pi^-\pi^+$'       ,  1.1e3, 'M178', True],
        ['AUBERT 09AB'      , 0, False, r'$D^+\pi^-$',     r'$0^+$', mval(2297,   8,  20),    mval(273, 12, 48),       r'$B^-\to D^+\pi^-\pi^+$'       ,  3.4e3, 'M178', True],  # M178
        ['LINK 04A'         , 1,  True, r'$D^0\pi^-$',      'undef', mval(2403,  14,  35),    mval(283, 24, 34),       r'$A\gamma$'                    ,   None, 'M179', False],
        ['AAIJ 15Y'         , 1, False, r'$D^0\pi^-$',     r'$0^+$', mval(2349,   6,   4),    mval(217, 13, 13),       r'$B^0\to \bar{D}^0\pi^-\pi^+$' ,  9.6e3, 'M179', True],
        ['AAIJ 15X'         , 1, False, r'$D^0\pi^-$',     r'$0^+$', mval(2360,  15,  30),    mval(255, 26, 51),       r'$B^0\to \bar{D}^0\pi^-K^+$'   ,  2.6e3, 'M179', True],
        ['ANJOS 89C'        , 1,  True, r'$D^{*0}\pi^+$',   'undef', mval(2443,   7,   5),    mval( 49, 19,  8),       r'$\gamma N\to D^{*0}\pi^+X^0$' ,    190, 'M120', True],  # M120
        ['BERGFELD 94B'     , 1,  True, r'$D^{*0}\pi^+$',   'undef', mval(2425,   2,   2),    mval( 26, [7, 8],  4),   r'$e^+e^-\to D^{*0}\pi^+X$'     ,    146, 'M120', True],
        ['ABE 05A'          , 1, False, r'$D^+\pi^+\pi^-$', 'undef', mval(2421,   2,   1),    mval( 21,  5,  8),       r'$\bar{B}^0\to D^+\pi^+2\pi^-$',    124, 'M120', True],
        ['ABRAMOWICZ 13'    , 1,  True, r'$D^{*0}\pi^-$',   'undef', mval(2421.9, 4.7, [1.2, 3.4]), None,              r'$e^{\pm}p\to D^{(*)0}\pi^+X$' ,    759, 'M120', True],
        ['ABLIKIM 20P'      , 1, False, r'$D^+\pi^+\pi^-$', 'undef', mval(2427.2, 1.0, 1.2),  mval(23.2, 2.3, 2.3),    r'$e^+e^-\to D^+D^-\pi^+\pi^-$' ,  4.2e3, 'M120', True],
        ['AAIJ 13CC'        , 0,  True, r'$D^{*+}\pi^-$',      'un', mval(2579.5, 3.4, 5.5),  mval(177.5, 17.8, 46.0), r'$pp\to D^{*+}\pi^-X$'         ,   60e3, 'M198', True],  # M198
        ['DEL-AMO-SA... 10P', 0,  True, r'$D^{*+}\pi^-$',  r'$0^-$', mval(2539.4, 4.5, 6.8),  mval(130, 12, 13),       r'$e^+e^-\to D^{*+}\pi^-X$'     ,   34e3, 'M198', True],
        ['DEL-AMO-SA... 10P', 1,  True, r'$D^0\pi^+$',      'undef', mval(2621.3, 3.7, 4.2),  None,                    r'$e^+e^-\to D^0\pi^+X$'        ,   13e3, 'M199', True],  # M199
        ['DEL-AMO-SA... 10P', 0,  True, r'$D^+\pi^-$',      'undef', mval(2608.7, 2.4, 2.5),  mval(93, 6, 13),         r'$e^+e^-\to D^+\pi^-X$'        ,   26e3, 'M199', True],
        ['AAIJ 16AH'        , 0, False, r'$D^+\pi^-$',     r'$1^-$', mval(2681.1, 5.6, 14.0), mval(186.7, 8.5, 11.9),  r'$B^-\to D^+2\pi^-$'           ,   28e3, 'M199', True],
        ['AAIJ 13CC'        , 0,  True, r'$D^{*+}\pi^-$',       'n', mval(2649.2, 3.5, 3.5),  mval(140.2, 17.1, 18.6), r'$pp\to D^{*+}\pi^-$'          ,   51e3, 'M199', True],
        ['AAIJ 13CC'        , 0,  True, r'$D^{*+}\pi^-$',      'un', mval(2737.0, 3.5, 11.2), mval(73.2, 13.4, 25.0),  r'$pp\to D^{*+}\pi^-$'          ,  7.7e3, 'M228', True],  # M228
        ['DEL-AMO-SA... 10P', 0,  True, r'$D^{*+}\pi^-$',      'un', mval(2752.4, 1.7, 2.7),  mval(71, 6, 11),         r'$e^+e^-\to D^{*+}\pi^-X$'     , 23.5e3, 'M203', True],  # M203
        ['DEL-AMO-SA... 10P', 1,  True, r'$D^0\pi^+$',      'undef', mval(2769.7, 3.8, 1.5),  None,                    r'$e^+e^-\to D^0\pi^+X$'        ,  5.7e3, 'M203', True],
        ['DEL-AMO-SA... 10P', 0,  True, r'$D^+\pi^-$',      'undef', mval(2763.3, 2.3, 2.3),  mval(60.9, 5.1, 3.6),    r'$e^+e^-\to D^+\pi^-X$'        , 11.3e3, 'M203', True],
        ['AAIJ 13CC'        , 0,  True, r'$D^{*+}\pi^-$',       'n', mval(2761.1, 5.1, 6.5),  mval(74.4, 3.4, 37.0),   r'$pp\to D^{*+}\pi^-X$'         ,   14e3, 'M203', True],
        ['AAIJ 13CC'        , 0,  True, r'$D^+\pi^-$',      'undef', mval(2760.1, 1.1, 3.7),  mval(74.4, 3.4, 19.1),   r'$pp\to D^+\pi^-X$'            ,   56e3, 'M203', True],
        ['AAIJ 13CC'        , 1,  True, r'$D^0\pi^-$',      'undef', mval(2771.7, 1.7, 3.8),  mval(66.7, 6.6, 10.5),   r'$pp\to D^0\pi^-X$'            ,   20e3, 'M203', True],
        ['AAIJ 15Y'         , 1, False, r'$D^0\pi^-$',     r'$3^-$', mval(2798,   7,   7),    mval(105, 18,   24),     r'$B^0\to \bar{D}^0\pi^+\pi^-$' ,  9.6e3, 'M203', True],
        ['AAIJ 16AH'        , 0, False, r'$D^+\pi^-$',     r'$3^-$', mval(2775.5, 4.5, 6.5),  mval(95.3, 9.6, 34.0),   r'$B^-\to D^+\pi^-\pi^-$'       ,   28e3, 'M203', True],
        ['AAIJ 15V'         , 0, False, r'$D^+K^-$',       r'$1^-$', mval(2781, 18, oplus(11, 6)), mval(177, 32, oplus(20, 7)), r'$B^-\to D^+K^-\pi^-$',    2e3, 'M249', True],  # M249
        ['ANJOS 89C'        , 0,  True, r'$D^+\pi^-$',      'undef', mval(2459,   3,   2),    mval(20, 10, 5),         r'$\gamma N\to D^+\pi^-X$'      ,    153, 'M119', True],  # M119
        ['ALBRECHT 89B'     , 0,  True, r'$D^+\pi^-$',      'undef', mval(2455,   3,   5),    mval(15, [10,13],[10,5]),r'$e^+e^-\to D^+\pi^-X$'        ,    337, 'M119', True],
        ['AVERY 90'         , 0,  True, r'$D^+\pi^-$',      'undef', mval(2461,   3,   1),    mval(20, [10, 9],[12,9]),r'$e^+e^-\to D^+\pi^-X$'        ,    440, 'M119', True],
        ['FRABETTI 94B'     , 0,  True, r'$D^+\pi^-$',      'undef', mval(2453,   3,   2),    mval(25, 10, 5),         r'$\gamma Be\to D^+\pi^-X$'     ,    128, 'M119', True],
        ['AVERY 94C'        , 0,  True, r'$D^+\pi^-$',      'undef', mval(2465,   3,   3),    mval(28, [7,8], 6),      r'$e^+e^-\to D^+\pi^-X$'        ,    486, 'M119', True],
        ['LINK 04A'         , 0,  True, r'$D^+\pi^-$',      'undef', mval(2464.5, 1.1, 1.9),  mval(38.7, 5.3, 2.9),    r'$\gamma A$'                   ,  5.8e3, 'M119', True],
        ['ABE 04D'          , 0, False, r'$D^+\pi^-$',     r'$2^+$', mval(2461.6, 2.1, 3.3),  mval(45.6, 4.4, 6.7),    r'$B^-\to D^+\pi^-\pi^+$'       ,  1.1e3, 'M119', True],
        ['AUBERT 09AB'      , 0, False, r'$D^+\pi^-$',     r'$2^+$', mval(2460.4, 1.2, 2.2),  mval(41.8, 2.5, 2.9),    r'$B^-\to D^+\pi^-\pi^+$'       ,  3.4e3, 'M119', True],
        ['DEL-AMO-SA... 10P', 0,  True, r'$D^+\pi^-$',          'n', mval(2462.2, 0.1, 0.8),  mval(50.5, 0.6, 0.7),    r'$e^+e^-\to D^+\pi^-X$'        ,  243e3, 'M119', True],
        ['ABRAMOWICZ 13', 0,  True, r'$D^{*+}\pi^-$',   'n', mval(2462.5, 2.4, [1.1,1.3]), mval(46.6, 8.1, [3.8,5.9]), r'$e^{\pm}p\to D^{(*)+}\pi^-X$' ,  2.3e3, 'M119', True],
        ['AAIJ 13CC',         0,  True, r'$D^+\pi^-$',      'undef', mval(2460.4, 0.1, 0.1),  mval(45.6, 0.4, 1.1),    r'$pp\to D^+\pi^-X$'            ,  675e3, 'M119', True],
        ['AAIJ 13CC',         0,  True, r'$D^{*+}\pi^-$',       'n', mval(2460.4, 0.4, 1.2),  mval(43.2, 1.2, 3.0),    r'$pp\to D^{*+}\pi^-X$'         ,   82e3, 'M119', True],
        ['AAIJ 16AH'        , 0, False, r'$D^+\pi^-$',     r'$2^+$', mval(2463.7, 0.4, 0.7),  mval(47.0, 0.8, 1.0),    r'$B^-\to D^+\pi^-\pi^-$'       ,   28e3, 'M119', True],
    ]
]

NOTES = [
    """ M120, M119: ANJOS 89C comment: "D0 pi+" -> "D*0 pi+" """,
    """ M179: remove 'J, P need confirmation' from header """,
    """ M198: Why we think that the two measurements refer to the same particle? """,
    """ M199: Not obvious that AAIJ 16AH refers to the same particle as other two results """
    """ M119: ALBRECHT 89B was not able to study quantum numbers of this state """
    """ M119: AAIJ 13CC confirms only natural spin-parity, but not 2+ assignment """
    """ Signal yield for AAIJ 15Y analysis is 9.6e3. Not mentioned in PDG """
    """ M119 AVERY 90 comment: "e^+e^-\to D^{*+}\pi^-X" -> "e^+e^-\to D^+\pi^-X" """
    """ Signal yield for ABE 04D is 1.1k. Not mentioned in PDG """
]
