from colors import kelly_gen

STATES = {
    'M061' : {
        'name': r'$D^*(2007)^0$',
        'fs': [r'$D^0\pi^0$', r'$D^0\gamma$'],
        'jp': r'$1^-$',
        'assignment': r'$1^3S_1$',
    },
    'M062' : {
        'name': r'$D^*(2010)^+$',
        'fs': [r'$D^0\pi^+$', r'$D^+\pi^0$', r'$D^+\gamma$'],
        'jp': r'$1^-$',
        'assignment': r'$1^3S_1$',
    },
    'M097' : {
        'name': r'$D_1(2420)^0$',
        'fs': [],
        'jp': r'$1^+$',
        'assignment': r'$1P_1$',
    },
    'M119' : {
        'name' : r'$D_2^*(2460)^0$',
        'fs': [],
        'jp': r'$2^+$',
        'assignment': r'$1^3P_2$',
    },
    'M120' : {
        'name' : r'$D_1(2420)^{\pm}$',
        'fs': [r'$D^{*0}\pi^+$', r'$D^+\pi^+\pi^-$'],
        'jp': 'undef',
        'assignment': r'$1P_1$',
    },
    'M150' : {
        'name' : r'$D_2^*(2460)^{\pm}$',
        'fs': [r'$D^0\pi^+$', r'$D^{*0}\pi^+$'],
        'jp': r'$2^+$',
        'assignment': r'$1^3P_2$',
    },
    'M178' : {
        'name' : r'$D_0^*(2300)^0$',
        'fs': [r'$D^+\pi^-$'],
        'jp': r'$0^+$',
        'assignment': r'$1^3P_0$',
    },
    'M179' : {
        'name' : r'$D_0^*(2300)^{\pm}$',
        'fs': [r'$D^0\pi^+$'],
        'jp': r'$0^+$',
        'assignment': r'$1^3P_0$',
    },
    'M180' : {
        'name' : r'$D_1(2430)^0$',
        'fs': [r'$D^{*+}\pi^-$'],
        'jp': r'$1^+$',
        'assignment': r'$1P_1^\prime$',
    },
    'M198' : {
        'name': r'$D(2550)^0$',
        'fs': [r'$D^{*+}\pi^-$'],
        'jp': r'$0^-$',
        'assignment': r'$2^1S_0$',
    },
    'M199' : {
        'name': r'$D_J^*(2600)$',
        'fs': [r'D\pi', r'D^*\pi'],
        'jp': r'$1^-$',
        'assignment': r'$2^3S_1$',
    },
    'M203' : {
        'name' : r'$D_3^*(2750)$',
        'fs' : [r'D\pi', r'D^*\pi'],
        'jp': r'$3^-$',
        'assignment': r'$1^3D_3$',
    },
    'M228' : {
        'name' : r'$D(2740)^0$',
        'fs' : [r'$D^{*+}\pi^-$'],
        'jp' : r'$2^-$',
        'assignment': r'$1D_2$',
    },
    'M229' : {
        'name' : r'$D(3000)^0$',
        'fs' : [r'$D^{*+}\pi^-$'],
        'jp' : r'$2^+$',
        'assignment': r'$1^3F_4$',
    },
    'M249' : {
        'name' : r'$D^*_1(2760)^0$',
        'fs' : [r'$D^+K^-$'],
        'jp' : r'$1^-$',
        'assignment': r'$1^3D_1$',
    }
}

colgen = kelly_gen()
for _, item in STATES.items():
    item['color'] = next(colgen)

PREDICTIED = {
    # Godfrey and Moats, Phys.Rev. D 93 (2016) 034035
    r'$1^1S_0$':      [r'$D$',          1877],
    r'$1^3S_1$':      [r'$D^*$',        2041],
    r'$1^3P_0$':      [r'$D_0^*$',      2399],
    r'$1P_1$':        [r'$D_1$',        2456],
    r'$1P_1^\prime$': [r'$D_1^\prime$', 2467],
    r'$1^3P_2$':      [r'$D_2^*$',      2502],
    r'$1D_2$':        [r'$D_2$',        2816],
    r'$1^3D_1$':      [r'$D_1^*$',      2817],
    r'$1^3D_3$':      [r'$D_3^*$',      2833],
    r'$1D_2^\prime$': [r'$D_2^\prime$', 2845],
    r'$1^3F_4$':      [r'$D_4^*$',      3113],
    r'$2^1S_0$':      [r'$D$',          2581],
    r'$2^3S_1$':      [r'$D^*$',        2643],
}
