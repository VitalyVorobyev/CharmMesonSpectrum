from average import oplus

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
        ['TOMARADZE 15', 0, True, r'$D^0\pi^0$', r'$1^-$', mval(1864.83+142.007,0.015,oplus(0.014, 0.05)), mval(0, 0, 0), r'$e^+e^-\to D^0\pi^0X$'     ,   10e3, 'M061', True],  # M061
        ['LEES 13X',  1, True, r'$D^0\pi^+$', r'$1^-$', mval(1864.83+145.4259,4e-4,oplus(1.7e-3, 0.05)), mval(83.3e-3,1.2e-3,1.4e-3), r'$e^+e^-\to D^0\pi^+X$',312.8e3, 'M062', True],  # M062

        ['LINK 04A'     , 1,  True, r'$D^0\pi^-$',      'undef', mval(2403,  14,  35),    mval(283, 24, 34),       r'$A\gamma$'                    ,   None, 'M179', False],  # M179
        ['AAIJ 15Y'     , 1, False, r'$D^0\pi^-$',     r'$0^+$', mval(2349,   6,   4),    mval(217, 13, 13),       r'$B^0\to \bar{D}^0\pi^-\pi^+$' ,  9.6e3, 'M179', True],
        ['AAIJ 15X'     , 1, False, r'$D^0\pi^-$',     r'$0^+$', mval(2360,  15,  30),    mval(255, 26, 51),       r'$B^0\to \bar{D}^0\pi^-K^+$'   ,  2.6e3, 'M179', True],

        ['LINK 04A'     , 0,  True, r'$D^+\pi^-$',      'undef', mval(2407,  21,  35),    mval(240, 55, 59),       r'$A\gamma$'                    ,   None, 'M178', False], # M178
        ['ABE 04D'      , 0, False, r'$D^+\pi^-$',     r'$0^+$', mval(2308,  17,  32),    mval(276, 21, 63),       r'$B^-\to D^+\pi^-\pi^+$'       ,  1.1e3, 'M178', True],
        ['AUBERT 09AB'  , 0, False, r'$D^+\pi^-$',     r'$0^+$', mval(2297,   8,  20),    mval(273, 12, 48),       r'$B^-\to D^+\pi^-\pi^+$'       ,  3.4e3, 'M178', True],

        ['ABE 04D'      , 0, False, r'$D^{*+}\pi^-$',  r'$1^+$', mval(2427, 26, 25),      mval(384,[75,107],74),   r'$B^+\to D^{*+}\pi^-\pi^+$'    ,    560, 'M180', True],  # M180
        ['AAIJ 2020D'   , 0, False, r'$D^{*+}\pi^-$',  r'$1^+$', mval(2411,  3,  9),      mval(309, 9, 28),        r'$B^+\to D^{*+}\pi^-\pi^+$'    ,   79e3, 'M180', True],
        
        ['ANJOS 89C'    , 0,  True, r'$D^{*+}\pi^-$',   'undef', mval(2428,   8,   5),    mval(58, 14, 10),        r'$\gamma N\to D^{*+}\pi^-X$'   ,    171, 'M097', True],  # M097 (width is not used in PDG)
        ['ALBRECHT 89H' , 0,  True, r'$D^{*+}\pi^-$',      'un', mval(2414,   2,   5),    mval(13, 6, [5,10]),     r'$e^+e^-\to D^{*+}\pi^-X$'     ,    171, 'M097', True],
        ['AVERY 90'     , 0,  True, r'$D^{*+}\pi^-$',      'un', mval(2428,   3,   2),    mval(23, [6,8], [3,10]), r'$e^+e^-\to D^{*+}\pi^-X$'     ,    279, 'M097', True],
        ['FRABETTI 94B' , 0,  True, r'$D^{*+}\pi^-$',      'un', mval(2422,   2,   2),    mval(15, 8, 4),          r'$\gamma Be\to D^{*+}\pi^-X$'  ,     51, 'M097', True],
        ['AVERY 94C'    , 0,  True, r'$D^{*+}\pi^-$',      'un', mval(2421, [2,1], 2),    mval(20, [5,6], 3),      r'$e^+e^-\to D^{*+}\pi^-X$'     ,    286, 'M097', True],
        ['ABE 04D'      , 0, False, r'$D^{*+}\pi^-$',  r'$1^+$', mval(2421.4, 1.5, 0.9),  mval(23.7, 2.7, 4.0),    r'$B^+\to D^{*+}\pi^-\pi^+$'    ,    560, 'M097', True],
        ['ABE 05A'      , 0, False, r'$D^0\pi^+\pi^-$', 'undef', mval(2426,   3,   1),    mval(24,   7,   8),      r'$B^-\to D^0\pi^+2\pi^-$'      ,    151, 'M097', True],
        ['DEL-AMO 10P'  , 0,  True, r'$D^{*+}\pi^-$',      'un', mval(2420.1, 0.1, 0.8),  mval(31.4, 0.5, 1.3),    r'$e^+e^-\to D^{*+}\pi^-X$'     ,  103e3, 'M097', True],
        ['ABRAMOWICZ 13', 0,  True, r'$D^{*+}\pi^-$',   'un', mval(2423.1,1.5,[1.0,0.4]), mval(38.8,5.0,[5.4,1.9]),r'$e^{\pm}p\to D^{(*)+}\pi^+X$' ,  2.7e3, 'M097', True],
        ['AAIJ 13CC'    , 0,  True, r'$D^{*+}\pi^-$',      'un', mval(2419.6, 0.1, 0.7),  mval(35.2, 0.4, 0.9),    r'$pp\to D^{*+}\pi^-X$'         ,  210e3, 'M097', True],
        ['AAIJ 2020D'   , 0, False, r'$D^{*+}\pi^-$',  r'$1^+$', mval(2424.8, 0.1, 0.7),  mval(33.6, 0.3, 2.7),    r'$B^+\to D^{*+}\pi^-\pi^+$'    ,   79e3, 'M097', True],

        ['ANJOS 89C'    , 1,  True, r'$D^{*0}\pi^+$',   'undef', mval(2443,   7,   5),    mval( 49, 19,  8),       r'$\gamma N\to D^{*0}\pi^+X^0$' ,    190, 'M120', True],  # M120
        ['BERGFELD 94B' , 1,  True, r'$D^{*0}\pi^+$',   'undef', mval(2425,   2,   2),    mval( 26, [7, 8],  4),   r'$e^+e^-\to D^{*0}\pi^+X$'     ,    146, 'M120', True],
        ['ABE 05A'      , 1, False, r'$D^+\pi^+\pi^-$', 'undef', mval(2421,   2,   1),    mval( 21,  5,  8),       r'$\bar{B}^0\to D^+\pi^+2\pi^-$',    124, 'M120', True],
        ['ABRAMOWICZ 13', 1,  True, r'$D^{*0}\pi^-$',   'undef', mval(2421.9, 4.7, [1.2, 3.4]), None,              r'$e^{\pm}p\to D^{(*)0}\pi^+X$' ,    759, 'M120', True],
        ['ABLIKIM 20P'  , 1, False, r'$D^+\pi^+\pi^-$', 'undef', mval(2427.2, 1.0, 1.2),  mval(23.2, 2.3, 2.3),    r'$e^+e^-\to D^+D^-\pi^+\pi^-$' ,  4.2e3, 'M120', True],

        ['ANJOS 89C'    , 0,  True, r'$D^+\pi^-$',      'undef', mval(2459,   3,   2),    mval(20, 10, 5),         r'$\gamma N\to D^+\pi^-X$'      ,    153, 'M119', True],  # M119
        ['ALBRECHT 89B' , 0,  True, r'$D^+\pi^-$',      'undef', mval(2455,   3,   5),    mval(15, [10,13],[10,5]),r'$e^+e^-\to D^+\pi^-X$'        ,    337, 'M119', True],
        ['AVERY 90'     , 0,  True, r'$D^+\pi^-$',      'undef', mval(2461,   3,   1),    mval(20, [10, 9],[12,9]),r'$e^+e^-\to D^+\pi^-X$'        ,    440, 'M119', True],
        ['FRABETTI 94B' , 0,  True, r'$D^+\pi^-$',      'undef', mval(2453,   3,   2),    mval(25, 10, 5),         r'$\gamma Be\to D^+\pi^-X$'     ,    128, 'M119', True],
        ['AVERY 94C'    , 0,  True, r'$D^+\pi^-$',      'undef', mval(2465,   3,   3),    mval(28, [7,8], 6),      r'$e^+e^-\to D^+\pi^-X$'        ,    486, 'M119', True],
        ['LINK 04A'     , 0,  True, r'$D^+\pi^-$',      'undef', mval(2464.5, 1.1, 1.9),  mval(38.7, 5.3, 2.9),    r'$\gamma A$'                   ,  5.8e3, 'M119', True],
        ['ABE 04D'      , 0, False, r'$D^+\pi^-$',     r'$2^+$', mval(2461.6, 2.1, 3.3),  mval(45.6, 4.4, 6.7),    r'$B^-\to D^+\pi^-\pi^+$'       ,  1.1e3, 'M119', True],
        ['AUBERT 09AB'  , 0, False, r'$D^+\pi^-$',     r'$2^+$', mval(2460.4, 1.2, 2.2),  mval(41.8, 2.5, 2.9),    r'$B^-\to D^+\pi^-\pi^+$'       ,  3.4e3, 'M119', True],
        ['DEL-AMO 10P'  , 0,  True, r'$D^+\pi^-$',          'n', mval(2462.2, 0.1, 0.8),  mval(50.5, 0.6, 0.7),    r'$e^+e^-\to D^+\pi^-X$'        ,  243e3, 'M119', True],
        ['ABRAMOWICZ 13', 0,  True, r'$D^{*+}\pi^-$',   'n', mval(2462.5,2.4,[1.1,1.3]),  mval(46.6,8.1,[3.8,5.9]),r'$e^{\pm}p\to D^{(*)+}\pi^-X$' ,  2.3e3, 'M119', True],
        ['AAIJ 13CC'    , 0,  True, r'$D^+\pi^-$',      'undef', mval(2460.4, 0.1, 0.1),  mval(45.6, 0.4, 1.1),    r'$pp\to D^+\pi^-X$'            ,  675e3, 'M119', True],
        ['AAIJ 13CC'    , 0,  True, r'$D^{*+}\pi^-$',       'n', mval(2460.4, 0.4, 1.2),  mval(43.2, 1.2, 3.0),    r'$pp\to D^{*+}\pi^-X$'         ,   82e3, 'M119', True],
        ['AAIJ 16AH'    , 0, False, r'$D^+\pi^-$',     r'$2^+$', mval(2463.7, 0.4, 0.7),  mval(47.0, 0.8, 1.0),    r'$B^-\to D^+\pi^-\pi^-$'       ,   28e3, 'M119', True],

        ['ALBRECHT 89F' , 1,  True, r'$D^0\pi^+$',      'undef', mval(2469,   4,   6),    None,                    r'$e^+e^-\to D^+\pi^-X$'        ,    262, 'M150', True],  # M150
        ['FRABETTI 94B' , 1,  True, r'$D^0\pi^+$',      'undef', mval(2453,   3,   2),    mval(23,     9,  5),     r'$\gamma Be\to D^0\pi^-X$'     ,    185, 'M150', True],
        ['BERGFELD 94B' , 1,  True, r'$D^0\pi^+$',      'undef', mval(2463,   3,   3),    mval(27, [8,11], 5),     r'$e^+e^-\to D^0\pi^+X$'        ,    312, 'M150', True],
        ['LINK 04A'     , 1,  True, r'$D^0\pi^+$',      'undef', mval(2467.6, 1.5, 0.8),  mval(34.1,  6.5, 4.2),   r'$\gamma A$'                   ,  3.5e3, 'M150', True],
        ['KUZMIN 07'    , 1, False, r'$D^0\pi^+$',     r'$2^+$', mval(2465.7,1.8,[4.8,1.4]), mval(49.7, 3.8, 6.4), r'$\bar{B}^0\to D^0\pi^+\pi^-$' ,  2.9e3, 'M150', True],
        ['DEL-AMO 10P'  , 1,  True, r'$D^0\pi^+$',      'undef', mval(2465.4, 0.2, 1.1),  None,                    r'$e^+e^-\to D^0\pi^+X$'        ,  111e3, 'M150', True],
        ['AAIJ 13CC'    , 1,  True, r'$D^0\pi^+$',      'undef', mval(2463.1, 0.2, 0.6),  mval(48.6, 1.3, 1.9),    r'$pp\to D^0\pi^+X$'            ,  342e3, 'M150', True],
        ['AAIJ 15Y'     , 1, False, r'$D^0\pi^-$',     r'$2^+$', mval(2468.6, 0.6, 0.3),  mval(47.3, 1.5, 0.7),    r'$B^0\to \bar{D}^0\pi^+\pi^-$' ,  9.6e3, 'M150', True],
        ['AAIJ 15X'     , 1, False, r'$D^0\pi^-$',     r'$2^+$', mval(2465.6, 1.8, 1.3),  mval(46.0, 3.4, 3.2),    r'$B^0\to \bar{D}^0\pi^-K^+$'   ,  2.6e3, 'M150', True],

        ['AAIJ 13CC'    , 0,  True, r'$D^{*+}\pi^-$',      'un', mval(2579.5, 3.4, 5.5),  mval(177.5, 17.8, 46.0), r'$pp\to D^{*+}\pi^-X$'         ,   60e3, 'M198', True],  # M198
        ['DEL-AMO 10P'  , 0,  True, r'$D^{*+}\pi^-$',  r'$0^-$', mval(2539.4, 4.5, 6.8),  mval(130, 12, 13),       r'$e^+e^-\to D^{*+}\pi^-X$'     ,   34e3, 'M198', True],
        ['AAIJ 2020D'   , 0, False, r'$D^{*+}\pi^-$',  r'$0^-$', mval(2518,   2,   7),    mval(199,  5, 17),       r'$B^+\to D^{*+}\pi^-\pi^+$'    ,   79e3, 'M198', True],
        
        ['DEL-AMO 10P'  , 1,  True, r'$D^0\pi^+$',      'undef', mval(2621.3, 3.7, 4.2),  None,                    r'$e^+e^-\to D^0\pi^+X$'        ,   13e3, 'M199', True],  # M199
        ['DEL-AMO 10P'  , 0,  True, r'$D^+\pi^-$',      'undef', mval(2608.7, 2.4, 2.5),  mval(93, 6, 13),         r'$e^+e^-\to D^+\pi^-X$'        ,   26e3, 'M199', True],
        ['AAIJ 16AH'    , 0, False, r'$D^+\pi^-$',     r'$1^-$', mval(2681.1, 5.6, 14.0), mval(186.7, 8.5, 11.9),  r'$B^-\to D^+2\pi^-$'           ,   28e3, 'M199', True],
        ['AAIJ 13CC'    , 0,  True, r'$D^{*+}\pi^-$',       'n', mval(2649.2, 3.5, 3.5),  mval(140.2, 17.1, 18.6), r'$pp\to D^{*+}\pi^-$'          ,   51e3, 'M199', True],
        ['AAIJ 2020D'   , 0, False, r'$D^{*+}\pi^-$',  r'$1^-$', mval(2641.9, 1.8, 4.5),  mval(149,    4,   20),   r'$B^+\to D^{*+}\pi^-\pi^+$'    ,   79e3, 'M199', True],
        
        ['AAIJ 13CC'    , 0,  True, r'$D^{*+}\pi^-$',      'un', mval(2737.0, 3.5, 11.2), mval(73.2, 13.4, 25.0),  r'$pp\to D^{*+}\pi^-$'          ,  7.7e3, 'M228', True],  # M228
        ['AAIJ 2020D'   , 0, False, r'$D^{*+}\pi^-$',  r'$2^-$', mval(2751,   3,    7 ),  mval(102,   6,   26),    r'$B^+\to D^{*+}\pi^-\pi^+$'    ,   79e3, 'M228', True],
    
        ['DEL-AMO 10P'  , 0,  True, r'$D^{*+}\pi^-$',      'un', mval(2752.4, 1.7, 2.7),  mval(71, 6, 11),         r'$e^+e^-\to D^{*+}\pi^-X$'     , 23.5e3, 'M203', True],  # M203
        ['DEL-AMO 10P'  , 1,  True, r'$D^0\pi^+$',      'undef', mval(2769.7, 3.8, 1.5),  None,                    r'$e^+e^-\to D^0\pi^+X$'        ,  5.7e3, 'M203', True],
        ['DEL-AMO 10P'  , 0,  True, r'$D^+\pi^-$',      'undef', mval(2763.3, 2.3, 2.3),  mval(60.9, 5.1, 3.6),    r'$e^+e^-\to D^+\pi^-X$'        , 11.3e3, 'M203', True],
        ['AAIJ 13CC'    , 0,  True, r'$D^{*+}\pi^-$',       'n', mval(2761.1, 5.1, 6.5),  mval(74.4, 3.4, 37.0),   r'$pp\to D^{*+}\pi^-X$'         ,   14e3, 'M203', True],
        ['AAIJ 13CC'    , 0,  True, r'$D^+\pi^-$',      'undef', mval(2760.1, 1.1, 3.7),  mval(74.4, 3.4, 19.1),   r'$pp\to D^+\pi^-X$'            ,   56e3, 'M203', True],
        ['AAIJ 13CC'    , 1,  True, r'$D^0\pi^-$',      'undef', mval(2771.7, 1.7, 3.8),  mval(66.7, 6.6, 10.5),   r'$pp\to D^0\pi^-X$'            ,   20e3, 'M203', True],
        ['AAIJ 15Y'     , 1, False, r'$D^0\pi^-$',     r'$3^-$', mval(2798,   7,   7),    mval(105, 18,   24),     r'$B^0\to \bar{D}^0\pi^+\pi^-$' ,  9.6e3, 'M203', True],
        ['AAIJ 16AH'    , 0, False, r'$D^+\pi^-$',     r'$3^-$', mval(2775.5, 4.5, 6.5),  mval(95.3, 9.6, 34.0),   r'$B^-\to D^+\pi^-\pi^-$'       ,   28e3, 'M203', True],
        ['AAIJ 2020D'   , 0, False, r'$D^{*+}\pi^-$',  r'$3^-$', mval(2753,   4,   6),    mval(66,  10,   14),     r'$B^+\to D^{*+}\pi^-\pi^+$'    ,   79e3, 'M203', True],

        ['AAIJ 15V'     , 0, False, r'$D^+K^-$',       r'$1^-$', mval(2781, 18, oplus(11, 6)), mval(177, 32, oplus(20, 7)), r'$B^-\to D^+K^-\pi^-$',    2e3, 'M249', True],  # M249

        ['AAIJ 16AH'    , 0, False, r'$D^+\pi^-$',     r'$2^+$', mval(3214, 29, 49),      mval(186, 38, 72),       r'$B^-\to D^+\pi^-\pi^-$'       ,   28e3, 'M229', True],  # M229
        ['AAIJ 13CC'    , 0,  True, r'$D^+\pi^-$',      'undef', mval(3008.1, 4.0, 0.0),  mval(110.5, 11.5, 0.0),  r'$pp\to D^+\pi^-X$'            , 17.6e3, 'M229', True],  # not used in PDG
        ['AAIJ 13CC'    , 0,  True, r'$D^{*+}\pi^-$',      'un', mval(2971.8, 8.7, 0.0),  mval(188.1, 44.8, 0.0),  r'$pp\to D^{*+}\pi^-X$'         ,  9.5e3, 'M229', True],  # not used in PDG
    ]
]

NOTES = [
    """ ALBRECHT 89F signal yield is 112 + 150 + 262. Not mentioned in PDG """,
    """ ABE 04D: signal yield for the B^+ -> D^{*+}\pi^-\pi^+ mode is 560 """,
    """ ANJOS 89C: not clear why M097 width is not used while M120 width is used """,
    """ M120, M119: ANJOS 89C comment: "D0 pi+" -> "D*0 pi+" """,
    """ M179: remove 'J, P need confirmation' from header """,
    """ M198: Why we think that the two measurements refer to the same particle? """,
    """ M199: Not obvious that AAIJ 16AH refers to the same particle as other two results """,
    """ M119: ALBRECHT 89B was not able to study quantum numbers of this state """,
    """ M119: AAIJ 13CC confirms only natural spin-parity, but not 2+ assignment """,
    """ Signal yield for AAIJ 15Y analysis is 9.6e3. Not mentioned in PDG """,
    """ M119 AVERY 90 comment: "e^+e^- -> D^{*+}\pi^-X" -> "e^+e^- -> D^+\pi^-X" """,
    """ Signal yield for ABE 04D is 1.1k. Not mentioned in PDG """,
    """ M229. AAIJ 16AH and AAIJ 13CC probably report different states """,
]
