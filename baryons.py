STATES = {
    'lamc': {
        'name': r'$\Lambda_c^+$',
        'jp': r'$1/2^+$',
        'assignment': '1/2+(1S)',
        'massPDG': (2286.46, 0.14),
        'ctauPDG': (202.4, 3.1),  # fs
    },
    'lamc2595': {
        'name': r'$\Lambda_c(2595)^+$',
        'jp': r'$1/2^+$',
        'assignment': '1/2-(1P)',
        'massPDG': (2592.25, 0.28),
        'widthPDG': (2.6, 0.6),  # MeV
    },
    'lamc2625': {
        'name': r'$\Lambda_c(2625)^+$',
        'jp': r'$3/2^-$',
        'assignment': '3/2-(1P)',
        'massPDG': (2628.11, 0.19),
        'widthPDG': 0.97,  # MeV @ CL=90%
    },
    'lamc2765': {
        'name': r'$\Lambda_c(2765)^+$',
        'assignment': '1/2+(2S)',
        'massPDG': (2766.6, 2.4),
        'widthPDG': (50, 10),
    },
    'lamc2860': {
        'name': r'$\Lambda_c(2860)^+$',
        'jp': r'$3/2^+$',
        'massPDG': (2856.1, 6.0),
        'widthPDG': (68, 22),  # MeV
    },
    'lamc2880': {
        'name': r'$\Lambda_c(2880)^+$',
        'jp': r'$5/2^+$',
        'assignment': '5/2+(1D)',
        'massPDG': (2881.63, 0.24),
        'widthPDG': (5.6, 0.8),  # MeV
    },
    'lamc2940': {
        'name': r'$\Lambda_c(2940)^+$',
        'jp': r'$3/2^-$',
        'assignment': ['1/2-(2P)', '3/2-(2P)'],
        'massPDG': (2939.6, 1.5),
        'widthPDG': (20, 6),  # MeV
    },
    'xic+': {
        'name': r'$\Xi_c^+$',
        'jp': r'$1/2^+$',
        'assignment': '1/2+(1S)',
        'massPDG': (2467.71, 0.23),
        'ctauPDG': (456., 5.),  # fs
    },
    'xic0': {
        'name': r'$\Xi_c^0$',
        'jp': r'$1/2^+$',
        'assignment': '1/2+(1S)',
        'massPDG': (2470.44, 0.28),
        'ctauPDG': (153., 6.),  # fs
    },
    'xic`+': {
        'name': r'$\Xi_c^{\prime+}$',
        'jp': r'$1/2^+$',
        'massPDG': (2578.2, 0.5),
    },
    'xic`0': {
        'name': r'$\Xi_c^{\prime0}$',
        'jp': r'$1/2^+$',
        'massPDG': (2578.7, 0.5),
    },
    'xic2645+': {
        'name': r'$\Xi_c(2645)^+$',
        'jp': r'$3/2^+$',
        'massPDG': (2645.10, 0.30),
        'widthPDG': (2.14, 0.19)
    },
    'xic26450': {
        'name': r'$\Xi_c(2645)^0$',
        'jp': r'$3/2^+$',
        'massPDG': (2646.16, 0.25),
        'widthPDG': (2.35, 0.22)
    },
    'xic2790+': {
        'name': r'$\Xi_c(2790)^+$',
        'jp': r'$1/2^-$',
        'assignment': '1/2-(1P)',
        'massPDG': (2791.9, 0.5),
        'widthPDG': (8.9, 1.0)
    },
    'xic27900': {
        'name': r'$\Xi_c(2790)^0$',
        'jp': r'$1/2^-$',
        'assignment': '1/2-(1P)',
        'massPDG': (2793.9, 0.5),
        'widthPDG': (10.0, 1.1)
    },
    'xic2815+': {
        'name': r'$\Xi_c(2815)^+$',
        'jp': r'$3/2^-$',
        'assignment': '3/2-(1P)',
        'massPDG': (2816.51, 0.25),
        'widthPDG': (2.43, 0.26)
    },
    'xic28150': {
        'name': r'$\Xi_c(2815)^0$',
        'jp': r'$3/2^-$',
        'assignment': '3/2-(1P)',
        'massPDG': (2819.79, 0.30),
        'widthPDG': (2.54, 0.25)
    },
    'xic29230': {
        'name': r'$\Xi_c(2923)^0$',
        'massPDG': (2923.04, 0.35),
        'widthPDG': (7.1, 2.0)
    },
    'xic2930+': {
        'name': r'$\Xi_c(2930)^+$',
        'massPDG': (2942, 5),
        'widthPDG': (15, 9)
    },
    'xic29300': {
        'name': r'$\Xi_c(2930)^0$',
        'massPDG': (2938.55, 0.30),
        'widthPDG': (10.2, 1.4)
    },
    'xic2970+': {
        'name': r'$\Xi_c(2970)^+$',
        'assignment': '1/2+(2S)',
        'massPDG': (2964.3, 1.5),
        'widthPDG': (20.9, 3.5)
    },
    'xic29700': {
        'name': r'$\Xi_c(2970)^0$',
        'assignment': '1/2+(2S)',
        'massPDG': (2967.1, 1.7),
    },
    'xic3055+': {
        'name': r'$\Xi_c(3055)^+$',
        'assignment': '3/2+(1D)',
        'massPDG': (3055.9, 0.4),
        'widthPDG': (7.8, 1.9)
    },
    'xic3080+': {
        'name': r'$\Xi_c(3080)^+$',
        'assignment': '5/2+(1D)',
        'massPDG': (3077.2, 0.4),
        'widthPDG': (3.6, 1.1)
    },
    'xic30800': {
        'name': r'$\Xi_c(3080)^0$',
        'assignment': '5/2+(1D)',
        'massPDG': (3079.9, 1.4),
        'widthPDG': (5.6, 2.2)
    },
    'xic3123+': {
        'name': r'$\Xi_c(3123)^+$',
        'assignment': ['1/2-(2P)', '3/2-(2P)'],
        'massPDG': (3122.9, 1.3),
        'widthPDG': (4, 4)
    },
    'omegac': {
        'name': r'$\Omega_c^0$',
        'jp': r'$1/2^+$',
        'massPDG': (2695.2, 1.7),
        'widthPDG': (2.68, 0.26)
    },
    'omegac2770': {
        'name': r'$\Omega_c(2770)^0$',
        'jp': r'$3/2^+$',
        'massPDG': (2765.9, 2.0),
        'widthPDG': (70.7, 0.9)
    },
    'omegac3000': {
        'name': r'$\Omega_c(3000)^0$',
        'massPDG': (3000.41, 0.22),
        'widthPDG': (4.5, 0.7)
    },
    'omegac3050': {
        'name': r'$\Omega_c(3050)^0$',
        'massPDG': (3050.20, 0.13),
        'widthPDG': 1.2
    },
    'omegac3065': {
        'name': r'$\Omega_c(3065)^0$',
        'massPDG': (3065.46, 0.28),
        'widthPDG': (3.5, 0.4)
    },
    'omegac3090': {
        'name': r'$\Omega_c(3090)^0$',
        'massPDG': (3090.0, 0.5),
        'widthPDG': (8.7, 1.3)
    },
    'omegac3120': {
        'name': r'$\Omega_c(3120)^0$',
        'massPDG': (3119.1, 1.0),
        'widthPDG': 2.6
    },
    'sigmac2455++': {
        'name': r'$\Sigma_c^{++}$',
        'jp': r'$1/2^+$',
        # 'assignment': '1/2+(1S)',
        'massPDG': (2453.97, 0.14),
        'ctauPDG': (1.83, 0.18),
    },
    'sigmac2455+': {
        'name': r'$\Sigma_c^{+}$',
        'jp': r'$1/2^+$',
        # 'assignment': '1/2+(1S)',
        'massPDG': (2452.9, 0.4),
        'ctauPDG': 4.6,
    },
    'sigmac24550': {
        'name': r'$\Sigma_c^{0}$',
        'jp': r'$1/2^+$',
        # 'assignment': '1/2+(1S)',
        'massPDG': (2453.75, 0.14),
        'ctauPDG': (1.83, 0.19),
    },
    'sigmac2520++': {
        'name': r'$\Sigma_c(2520)^{++}$',
        'jp': r'$3/2^+$',
        # 'assignment': '1/2+(1S)',
        'massPDG': (2518.41, 0.21),
        'widthPDG': (14.78, 0.40),
    },
    'sigmac2520+': {
        'name': r'$\Sigma_c(2520)^{+}$',
        'jp': r'$3/2^+$',
        # 'assignment': '1/2+(1S)',
        'massPDG': (2517.5, 2.3),
        'widthPDG': 17,
    },
    'sigmac25200': {
        'name': r'$\Sigma_c(2520)^{0}$',
        'jp': r'$3/2^+$',
        # 'assignment': '1/2+(1S)',
        'massPDG': (2518.48, 0.20),
        'widthPDG': (15.3, 0.5),
    },

    'sigmac2800++': {
        'name': r'$\Sigma_c(2800)^{++}$',
        # 'jp': r'$3/2^+$',
        # 'assignment': '1/2+(1S)',
        'massPDG': (2801, 6),
        'widthPDG': (75, 22),
    },
    'sigmac2800+': {
        'name': r'$\Sigma_c(2800)^{+}$',
        # 'jp': r'$3/2^+$',
        # 'assignment': '1/2+(1S)',
        'massPDG': (2792, 14),
        'widthPDG': (62, 60),
    },
    'sigmac28000': {
        'name': r'$\Sigma_c(2800)^{0}$',
        # 'jp': r'$3/2^+$',
        # 'assignment': '1/2+(1S)',
        'massPDG': (2806, 7),
        'widthPDG': (72, 22),
    },
}

PREDICTIED = {
    'lamc': {
        '1/2+(1S)': 2286,
        '1/2+(2S)': 2766,
        '1/2+(3S)': 3112,
        '1/2-(1P)': 2591,
        '3/2-(1P)': 2629,
        '1/2-(2P)': 2989,
        '3/2-(2P)': 3000,
        '3/2+(1D)': 2857,
        '5/2+(1D)': 2879,
        '3/2+(2D)': 3188,
        '5/2+(2D)': 3198,
    },
    'xic': {
        '1/2+(1S)': 2467,
        '1/2+(2S)': 2959,
        '1/2-(1P)': 2779,
        '3/2-(1P)': 2814,
        '1/2-(2P)': 3195,
        '3/2-(2P)': 3204,
        '3/2+(1D)': 3055,
        '5/2+(1D)': 3076,
    }
}
