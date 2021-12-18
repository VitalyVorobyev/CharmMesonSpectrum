from colors import kelly_gen
import numpy as np

STATES = {
    'S032': {
        'name': r'$D^0$',
        'jp': r'$0^-$',
        'assignment': r'$1^1S_1$',
        'massPDG': (1864.84, 0.05),
        'ctauPDG': (410.1, 1.5),  # fs
    },
    'S031': {
        'name': r'$D^+$',
        'jp': r'$0^-$',
        'assignment': r'$1^1S_1$',
        'massPDG': (1869.66, 0.05),
        'ctauPDG': (1040, 7),  # fs
    },
    'S034': {
        'name': r'$D_s^+$',
        'jp': r'$0^-$',
        'assignment': r'$1^1S_1$',
        'massPDG': (1968.85, 0.05),
        'ctauPDG': (504, 4),  # fs
    },
    'M061': {
        'name': r'$D^{*0}$',
        'fs': [r'$D^0\pi^0$', r'$D^0\gamma$'],
        'jp': r'$1^-$',
        'assignment': r'$1^3S_1$',
        'massPDG': (2006.85, 0.05),
        'widthPDG': 2.1,  # MeV
    },
    'M062': {
        'name': r'$D^{*+}$',
        'fs': [r'$D^0\pi^+$', r'$D^+\pi^0$', r'$D^+\gamma$'],
        'jp': r'$1^-$',
        'assignment': r'$1^3S_1$',
        'massPDG': (2010.26, 0.05),
        'widthPDG': (0.0834, 0.0018),  # MeV
    },
    'S074': {
        'name': r'$D_s^{*+}$',
        'fs': [r'$D_s^+\pi^+$', r'$D_s^+\pi^0$', r'$D_s^+e^+e^-$'],
        'jp': r'$1^-$',
        'assignment': r'$1^3S_1$',
        'massPDG': (2112.2, 0.4),
        'widthPDG': 1.9,  # MeV
    },
    'M252': {
        'name': r'$D_0^*(2300)$',
        'fs': [r'$D^+\pi^-$', r'$D^0\pi^+$'],
        'jp': r'$0^+$',
        'massPDG': (2343, 10),
        'widthPDG': (229, 16),
        'assignment': r'$1^3P_0$',
    },
    'M172': {
        'name': r'$D_{s0}^*(2317)^+$',
        'fs': [r'$D_s^+\pi^0$'],
        'jp': r'$0^+$',
        'massPDG': (2317.8, 0.5),
        'widthPDG': 3.8,
        'assignment': r'$1^3P_0$',
    },
    'M253': {
        'name': r'$D_1(2420)^0$',
        'fs': [r'$D^{*0}\pi^+', r'$D^{*0}\pi^0'],
        'jp': r'$1^+$',
        'assignment': r'$1P_1$',
        'massPDG': (2422.1, 0.6),
        'widthPDG': (31.3, 1.9),  # MeV
    },
    'M173': {
        'name': r'$D_{s1}(2460)^+$',
        'fs': [r'$D^{*0}\pi^+', r'$D^{*0}\pi^0'],
        'jp': r'$1^+$',
        'assignment': r'$1P_1$',
        'massPDG': (2459.5, 0.6),
        'widthPDG': 3.5,  # MeV
    },
    'M180': {
        'name': r'$D_1(2430)^0$',
        'fs': [r'$D^{*+}\pi^-$'],
        'jp': r'$1^+$',
        'assignment': r'$1P_1^\prime$',
        'massPDG': (2412, 9),
        'widthPDG': (314, 29),  # MeV
    },
    'M121': {
        'name': r'$D_{s1}(2536)^+$',
        'fs': [r'$D^*K$', r'$D^+\pi^-K^+$'],
        'jp': r'$1^+$',
        'assignment': r'$1P_1^\prime$',
        'massPDG': (2535.11, 0.06),
        'widthPDG': (0.92, 0.05),  # MeV
    },
    'M254': {
        'name': r'$D_2^*(2460)$',
        'fs': [r'$D^0\pi^+$', r'$D^{*0}\pi^+$', r'$D^+\pi^-$', r'$D^{*+}\pi^-$'],
        'jp': r'$2^+$',
        'assignment': r'$1^3P_2$',
        'massPDG': (2461.1, 0.8),
        'widthPDG': (47.3, 0.8),  # MeV
    },
    'M148': {
        'name': r'$D_{s2}^*(2573)^+$',
        'fs': [r'$D^0K^+$'],
        'jp': r'$2^+$',
        'assignment': r'$1^3P_2$',
        'massPDG': (2569.1, 0.8),
        'widthPDG': (16.9, 0.7),  # MeV
    },
    'M198': {
        'name': r'$D_0(2550)^0$',
        'fs': [r'$D^{*+}\pi^-$'],
        'jp': r'$0^-$',
        'assignment': r'$2^1S_0$',
        'massPDG': (2549, 19),
        'widthPDG': (165, 24),  # MeV
    },
    'M256': {
        'name': r'$D_{s0}(2590)^+$',
        'fs': [r'$D^+K^+\pi^-$'],
        'jp': r'$0^-$',
        'assignment': r'$2^1S_0$',
        'massPDG': (2591, np.hypot(6, 7)),
        'widthPDG': (89, np.hypot(16, 12)),  # MeV
    },
    'M199': {
        'name': r'$D_1^*(2600)$',
        'fs': [r'D\pi', r'D^*\pi'],
        'jp': r'$1^-$',
        'assignment': r'$2^3S_1$',
        'massPDG': (2627, 10),
        'widthPDG': (141, 23),  # MeV
    },
    'M182': {
        'name': r'$D_{s1}^*(2700)$',
        'fs': [r'$D^{(*)}K$'],
        'jp': r'$1^-$',
        'assignment': r'$2^3S_1$',
        'massPDG': (2714, 5),
        'widthPDG': (122, 10),  # MeV
    },
    'M249': {
        'name': r'$D^*_1(2760)^0$',
        'fs': [r'$D^+K^-$'],
        'jp': r'$1^-$',
        'assignment': r'$1^3D_1$',
        'massPDG': (2781, 22),
        'widthPDG': (177, 40),  # MeV
    },
    'M196': {
        'name': r'$D^*_{s1}(2860)^+$',
        'fs': [r'$D^+K^-$'],
        'jp': r'$1^-$',
        'assignment': r'$1^3D_1$',
        'massPDG': (2859, 27),
        'widthPDG': (159, 80),  # MeV
    },
    'M203': {
        'name': r'$D_3^*(2750)$',
        'fs': [r'D\pi', r'D^*\pi'],
        'jp': r'$3^-$',
        'assignment': r'$1^3D_3$',
        'massPDG': (2763.1, 3.2),
        'widthPDG': (66, 5),  # MeV
    },
    'M226': {
        'name': r'$D_{s3}^*(2860)^+$',
        'fs': [r'D^+K^-', r'D^{*+}K^-'],
        'jp': r'$3^-$',
        'assignment': r'$1^3D_3$',
        'massPDG': (2860, 7),
        'widthPDG': (53, 10),  # MeV
    },
    'M228': {
        'name': r'$D(2740)^0$',
        'fs': [r'$D^{*+}\pi^-$'],
        'jp': r'$2^-$',
        'assignment': r'$1D_2$',
        'massPDG': (2747, 6),
        'widthPDG': (88, 6),  # MeV
    },
    'M229': {
        'name': r'$D(3000)^0$',
        'fs': [r'$D^{*+}\pi^-$'],
        'jp': r'$2^+$',
        'assignment': r'$1^3F_4$',
        'massPDG': (3214, 60),
        'widthPDG': (186, 80),  # MeV
    },
    'M197': {
        'name': r'$D_{sJ}(3000)^0$',
        'fs': [r'$D^{*0}K^+$', r'$D^{*+}K_S^0$'],
        'assignment': r'$2P_1^{(\prime)}$',
        'massPDG': (3044, 31),
        'widthPDG': (239, 60),  # MeV
    },
}

colgen = kelly_gen()
for _, item in STATES.items():
    item['color'] = next(colgen)

PREDICTIED = {
    # Godfrey and Moats, Phys.Rev. D 93 (2016) 034035
# 1S
    r'$1^1S_0$':      [r'$D$',          1877],
    r'$1^3S_1$':      [r'$D^*$',        2041],
# 1P
    r'$1^3P_0$':      [r'$D_0^*$',      2399],
    r'$1P_1$':        [r'$D_1$',        2456],
    r'$1P_1^\prime$': [r'$D_1^\prime$', 2467],
    r'$1^3P_2$':      [r'$D_2^*$',      2502],
# 1D
    r'$1^3D_1$':      [r'$D_1^*$',      2817],
    r'$1D_2$':        [r'$D_2$',        2816],
    r'$1D_2^\prime$': [r'$D_2^\prime$', 2845],
    r'$1^3D_3$':      [r'$D_3^*$',      2833],
# 1F
    r'$1^3F_2$':        [r'$D_2^*$',          3132],
    r'$1^3F_3$':        [r'$D_3$',            3108],
    r'$1^3F_3^\prime$': [r'$D_3^{*^\prime}$', 3143],
    r'$1^3F_4$':        [r'$D_4^*$',          3113],
# 2S
    r'$2^1S_0$':      [r'$D$',          2581],
    r'$2^3S_1$':      [r'$D^*$',        2643],
# 2P
    r'$2^3P_0$':      [r'$D_0^*$',      2931],
    r'$2P_1$':        [r'$D_1$',        2924],
    r'$2P_1^\prime$': [r'$D_1^\prime$', 2961],
    r'$2^3P_2$':      [r'$D_2^*$',      2957],
# 2S
    r'$3^1S_0$':      [r'$D$',          3068],
    r'$3^3S_1$':      [r'$D^*$',        3110],
}

PREDICTIED_DS = {
    # Godfrey and Moats, Phys.Rev. D 93 (2016) 034035
# 1S
    r'$1^1S_0$':      [r'$D_s$',           1979],
    r'$1^3S_1$':      [r'$D_s^*$',         2129],
# 1P
    r'$1^3P_0$':      [r'$D_{s0}^*$',      2484],
    r'$1P_1$':        [r'$D_{s1}$',        2549],
    r'$1P_1^\prime$': [r'$D_{s1}^\prime$', 2556],
    r'$1^3P_2$':      [r'$D_{s2}^*$',      2592],
# 1D
    r'$1D_2$':        [r'$D_{S2}$',        2900],
    r'$1^3D_1$':      [r'$D_{s1}^*$',      2899],
    r'$1^3D_3$':      [r'$D_{s3}^*$',      2917],
    r'$1D_2^\prime$': [r'$D_{s2}^\prime$', 2926],
# 1F
    r'$1^3F_2$':        [r'$D_{s2}^*$',          3208],
    r'$1^3F_3$':        [r'$D_{s3}$',            3186],
    r'$1^3F_3^\prime$': [r'$D_{s3}^{*^\prime}$', 3218],
    r'$1^3F_4$':        [r'$D_{s4}^*$',          3190],
# 2S
    r'$2^1S_0$':      [r'$D_s$',           2673],
    r'$2^3S_1$':      [r'$D_s^*$',         2732],
# 2P
    r'$2^3P_0$':      [r'$D_{s0}^*$',      3005],
    r'$2P_1$':        [r'$D_{s1}$',        3018],
    r'$2P_1^\prime$': [r'$D_{s1}^\prime$', 3038],
    r'$2^3P_2$':      [r'$D_{s2}^*$',      3048],
# 3S
    r'$3^1S_0$':      [r'$D_s$',           3154],
    r'$3^3S_1$':      [r'$D_s^*$',         3193],
}
