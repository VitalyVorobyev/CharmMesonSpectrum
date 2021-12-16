import numpy as np


rare_dn = {
    r'$\gamma\gamma':
    [
        [26.00, 'CLEOII',  'Phys. Rev. Lett. 90 (2003) 101801', 0.],
        [3.80,  'BESIII',  'Phys. Rev. D91 (2015) 112015', 2.93],
        [2.20,  'BaBar',   'Phys. Rev. D85 (2012) 091107', 0.],
        [0.85,  'Belle',   'Phys. Rev. D93 (2016) 051102', 0.],
    ],
    r'$e^+e^-$':
    [
        [220.000, 'CLEO',   'Phys. Rev. Lett. 60 (1988) 1614'],
        [170.000, 'Argus',  'Phys. Lett. B209 (1988) 380'],
        [130.000, 'Mark3',  'Phys. Rev. D37 (1988) 2023'],
        [13.000,  'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065', 0.],
        [8.190,   'E789',   'Phys. Rev. D61 (2000) 032005'],
        [6.200,   'E791',   'Phys. Lett. B462 (1999) 401'],
        [1.200,   'BaBar',  'Phys. Rev. Lett. 93 (2004) 191801'],
        [0.079,   'Belle',  'Phys. Rev. D81 (2010) 091102R'],
    ],
    r'$\mu^+\mu^-$':
    [
        [70.0,    'Argus',  'Phys. Lett. B209 (1988) 380'],
        [44.0,    'E653',   'Phys. Lett. B345 (1995) 85'],
        [34.0,    'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065', 0.],
        [15.6,    'E789',   'Phys. Rev. D61 (2000) 032005'],
        [5.2,     'E791',   'Phys. Lett. B462 (1999) 401'],
        [2.0,     'HERAb',  'Phys. Lett. B596 (2004) 173'],
        [1.3,     'BaBar',  'Phys. Rev. Lett. 93 (2004) 191801'],
        [0.21,    'CDF',    'Phys. Rev. D82 (2010) 091105R'],
        [0.14,    'Belle',  'Phys. Rev. D81 (2010) 091102R'],
        [0.0062,  'LHCb',   'Phys.Lett. B725 (2013) 15'],
    ],
    r'$\pi^0e^+e^-$':
    [
        [45.0, 'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065', 0.],
        [4.0,  'BESIII', 'Phys. Rev. D97 (2018) 072015', 2.93],
    ],
    r'$\pi^0\mu^+\mu^-$':
    [
        [540.0, 'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065', 0.],
        [180.0, 'E653',   'Phys. Lett. B345 (1995) 85'],
    ],
    r'$\eta e^+e^-$':
    [
        [110.0, 'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065', 0.],
        [3.0,   'BESIII', 'Phys. Rev. D97 (2018) 072015', 2.93],
    ],
    r'$\eta\mu^+\mu^-$':
    [
        [530.0, 'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065', 0.],
    ],
    r'$\pi^+\pi^-e^+e^-$':
    [
        [370.0, 'E791',   'Phys. Rev. Lett. 86 (2001) 3969'],
        [7.0,   'BESIII', 'Phys. Rev. D97 (2018) 072015', 2.93],
    ],
    r'$K_S^0 e^+e^-$':
    [
        [12.0, 'BESIII', 'Phys. Rev. D97 (2018) 072015', 2.93],
    ],
    r'$\rho^0e^+e^-$':
    [
        [450.0, 'CLEO',   'Phys. Rev. Lett. 60 (1988) 1614'],
        [124.0, 'E791',   'Phys. Rev. Lett. 86 (2001) 3969'],
        [100.0, 'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065', 0.],
    ],
    r'$\pi^+\pi^-\mu^+\mu^-$':
    [
        [30.0, 'E791', 'Phys. Rev. Lett. 86 (2001) 3969'],
        [(0.964, 0.048, 0.051, 0.097), 'LHCb', 'Phys. Rev. Lett. 119 (2017) 181805'],
    ],
    r'$\rho^0\mu^+\mu^-$':
    [
        [810.0, 'CLEO',   'Phys. Rev. Lett. 60 (1988) 1614'],
        [490.0, 'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065', 0.],
        [230.0, 'E653',   'Phys. Lett. B345 (1995) 85'],
        [ 22.0, 'E791',   'Phys. Rev. Lett. 86 (2001) 3969'],
    ],
    r'\omega e^+e^-':
    [
        [180.0, 'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065', 0.],
        [  6.0, 'BESIII', 'Phys. Rev. D97 (2018) 072015', 2.93],
    ],
    r'$\omega\mu^+\mu^-$':
    [
        [830.0, 'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065', 0.],
    ],
    r'$K^+K^-e^+e^-$':
    [
        [315.0, 'E791',   'Phys. Rev. Lett. 86 (2001) 3969'],
        [ 11.0, 'BESIII', 'Phys. Rev. D97 (2018) 072015', 2.93],
    ],
    r'$\phi e^-e^+$':
    [
        [59.0, 'E791',   'Phys. Rev. Lett. 86 (2001) 3969'],
        [52.0, 'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065', 0.],
    ],
    r'$K^+K^-\mu^+\mu^-$':
    [
        [33.0, 'E791', 'Phys. Rev. Lett. 86 (2001) 3969'],
        [(0.154, 0.027, 0.009, 0.016), 'LHCb', 'Phys. Rev. Lett. 119 (2017) 181805'],
    ],
    r'$\phi\mu^+\mu^-$':
    [
        [410.0, 'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065', 0.],
        [ 31.0, 'E791',   'Phys. Rev. Lett. 86 (2001) 3969'],
    ],
    r'$K^0 e^+e^-$':
    [
        [1700.0, 'Mark3',  'Phys. Rev. D40 (1989) 906'],
        [ 110.0, 'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065', 0.],
    ],
    r'$K^0\mu^+\mu^-$':
    [
        [670.0, 'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065', 0.],
        [260.0, 'E653',   'Phys. Lett. B345 (1995) 85'],
    ]
    r'$K^-\pi^+e^+e^-$':
    [
        [385.0, 'E791',   'Phys. Rev. Lett. 86 (2001) 3969'],
        [ 41.0, 'BESIII', 'Phys. Rev. D97 (2018) 072015', 2.93],
    ],
    r'$K^-\pi^+(e^+e^-)_{\rho/\omega}$':
    [
        [(4.0, 0.5, 0.2, 0.1), 'BaBar', 'Phys. Rev. Lett. 122 (2018) 081802'],
    ],
    r'$K^{*0}(892)e^+e^-$':
    [
        [140.0, 'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065', 0.],
        [ 47.0, 'E791',   'Phys. Rev. Lett. 86 (2001) 3969'],
    ],
    r'$K^-\pi^+\mu^+\mu^-$':
    [
        [360.0, 'E791', 'Phys. Rev. Lett. 86 (2001) 3969'],
    ],
    r'$K^-\pi^+(\mu^+\mu^-)_{\rho/\omega}$':
    [
        [(4.17, 0.12, 0.40), 'LHCb', 'R. Aaij et al., Phys.Lett. B757 (2016) 558'],
    ],
    r'$K^{*0}(892)\mu^+\mu^-$':
    [
        [1180.0, 'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065', 0.],
        [  24.0, 'E791',   'Phys. Rev. Lett. 86 (2001) 3969'],
    ]
    r'$\pi^+\pi^-\pi^0\mu^+\mu^-$':
    [
        [810.0, 'E653', 'Phys. Lett. B345 (1995) 85'],
    ],
    r'$\rho^0\gamma$':
    [
        [240.0, 'CLEOII', 'Phys. Rev. D58 (1998) 092001'],
        [(17.7, 3.0, 0.7), 'Belle', 'Phys. Rev. Lett. 118 (2017) 051801'],
    ]
    r'$\omega\gamma$':
    [
        [240.0, 'CLEOII', 'Phys. Rev. D58 (1998) 092001'],
    ],
    r'$K^{*0}(892)\gamma$':
    [
        [760.0, 'CLEOII', 'Phys. Rev. D58 (1998) 092001'],
        [(322.0, 20.0, 27.0), 'BaBar', 'Phys. Rev. D78 (2008) 071101'],
    ]
    r'$\phi\gamma$':
    [
        [190.0, 'CLEOII', 'Phys. Rev. D58 (1998) 092001'],
        [(27.3, 3.0, 2.6), 'BaBar', 'Phys. Rev. D78 (2008) 071101'],
    ],
}

emu = r'e^{\pm}\mu^{\mp}'
lfv_dn = {
    fr'${emu}$':
    [
        [270.0, 'CLEO',   'Phys. Rev. Lett. 60 (1988) 1614'],
        [120.0, 'Mark3',  'Phys. Lett. B193 (1987) 147'],
        [100.0, 'Argus',  'Phys. Lett. B209 (1988) 380'],
        [19.0,  'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065', 0.],
        [17.2,  'E789',   'Phys. Rev. D61 (2000) 032005'],
        [8.1,   'E791',   'Phys. Lett. B462 (1999) 401'],
        [0.81,  'BaBar',  'Phys. Rev. Lett. 93 (2004) 191801'],
        [0.26,  'Belle',  'Phys. Rev. D81 (2010) 091102R'],
        [0.016, 'LHCb',   'Phys.Lett. B754 (2016) 167'],
    ],
    fr'$\pi^0 {emu}$':
    [
        [86.0, 'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065', 0.],
        [0.8, 'BaBar',   'Phys. Rev. D101 (2020) 112003'],
    ],
    fr'$\eta {emu}$':
    [
        [100.0, 'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065', 0.],
        [2.3,   'BaBar',  'Phys. Rev. D101 (2020) 112003'],
    ],
    fr'$\pi^+\pi^-{emu}$':
    [
        [15.0, 'E791', 'Phys. Rev. Lett. 86 (2001) 3969'],
        [1.7, 'BaBar', 'Phys. Rev. Lett. 124 (2020) 071802'],
    ],
    fr'$\rho {emu}$':
    [
        [66.0, 'E791',   'Phys. Rev. Lett. 86 (2001) 3969'],
        [49.0, 'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065', 0.],
        [0.5,  'BaBar',  'Phys. Rev. D101 (2020) 112003'],
    ],
    fr'$\omega {emu}$':
    [
        [120.0, 'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065', 0.],
        [1.7,   'BaBar',  'Phys. Rev. D101 (2020) 112003'],
    ],
    fr'$K^+K^- {emu}$':
    [
        [180.0, 'E791',  'Phys. Rev. Lett. 86 (2001) 3969'],
        [1.0,   'BaBar', 'Phys. Rev. Lett. 124 (2020) 071802'],
    ],
    fr'$\phi {emu}$':
    [
        [47.0, 'E791',   'Phys. Rev. Lett. 86 (2001) 3969'],
        [34.0, 'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065', 0.],
        [0.51, 'BaBar',  'Phys. Rev. D101 (2020) 112003'],
    ],
    fr'$K^0 {emu}$':
    [
        [100.0, 'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065', 0.],
        [0.86,  'BaBar',  'Phys. Rev. D101 (2020) 112003'],
    ],
    fr'$K^-\pi^+ {emu}$':
    [
        [550.0, 'E791',  'Phys. Rev. Lett. 86 (2001) 3969'],
        [1.9,   'BaBar', 'Phys. Rev. Lett. 124 (2020) 071802'],
    ],
    r'$K^{*0}(892) ' + fr'{emu}$':
    [
        [100.0, 'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065', 0.],
        [83.0,  'E791',   'Phys. Rev. Lett. 86 (2001) 3969'],
        [1.2,   'BaBar',  'Phys. Rev. D101 (2020) 112003'],
    ],
    r'$\pi^{\mp}\pi^{\mp}e^{\pm}e^{\pm}$':
    [
        [112.0, 'E791', 'Phys. Rev. Lett. 86 (2001) 3969'],
        [0.91, 'BaBar', 'Phys. Rev. Lett. 124 (2020) 071802'],
    ],
    r'$\pi^{\mp}\pi^{\mp}\mu^{\pm}\mu^{\pm}$':
    [
        [29.0, 'E791',  'Phys. Rev. Lett. 86 (2001) 3969'],
        [1.5,  'BaBar', 'Phys. Rev. Lett. 124 (2020) 071802'],
    ],
    r'$K^{\mp}\pi^{\mp}e^{\pm}e^{\pm}$':
    [
        [206.0, 'E791',   'Phys. Rev. Lett. 86 (2001) 3969'],
        [2.8,   'BESIII', 'Phys. Rev. D99 (2019) 112002'],
        [0.5,   'BaBar',  'Phys. Rev. Lett. 124 (2020) 071802'],
    ],
    r'$K^{\mp}\pi^{\mp}\mu^{\pm}\mu^{\pm}$':
    [
        [390.0, 'E791',  'Phys. Rev. Lett. 86 (2001) 3969'],
        [0.53,  'BaBar', 'Phys. Rev. Lett. 124 (2020) 071802'],
    ],
    r'$K^{\mp}K^{\mp}e^{\pm}e^{\pm}$':
    [
        [152.0, 'E791',  'Phys. Rev. Lett. 86 (2001) 3969'],
        [0.34,  'BaBar', 'Phys. Rev. Lett. 124 (2020) 071802'],
    ],
    r'$K^{\mp}K^{\mp}\mu^{\pm}\mu^{\pm}$':
    [
        [94.0, 'E791',  'Phys. Rev. Lett. 86 (2001) 3969'],
        [0.1,  'BaBar', 'Phys. Rev. Lett. 124 (2020) 071802'],
    ],
    r'$\pi^{\mp}\pi^{\mp}e^{\pm}\mu^{\pm}$':
    [
        [79.0, 'E791',  'Phys. Rev. Lett. 86 (2001) 3969'],
        [3.1,  'BaBar', 'Phys. Rev. Lett. 124 (2020) 071802'],
    ],
    r'$K^{\mp}\pi^{\mp}e^{\pm}\mu^{\pm}$':
    [
        [218.0, 'E791',  'Phys. Rev. Lett. 86 (2001) 3969'],
        [2.1,   'BaBar', 'Phys. Rev. Lett. 124 (2020) 071802'],
    ],
    r'$K^{\mp}K^{\mp}e^{\pm}\mu^{\pm}$':
    [
        [57.0, 'E791',  'Phys. Rev. Lett. 86 (2001) 3969'],
        [0.58, 'BaBar', 'Phys. Rev. Lett. 124 (2020) 071802'],
    ],
    r'$pe^-$':
    [
        [10.0, 'CLEOc', 'Phys. Rev. D79 (2009) 097101', 0.281],
    ],
    r'$\bar{p}e^-$':
    [
        [11.0, 'CLEOc', 'Phys. Rev. D79 (2009) 097101', 0.281],
    ]
}

rare_dp = {
    r'\pi^+e^+e^-':
    [
        [110.0, 'E687',  'Phys. Lett. B398 (1997) 239'],
        [52.0,  'E791',  'Phys. Lett. B462 (1999) 401'],
        [5.9,   'CLEOc',  'Phys. Rev. D82 (2010) 092007', 1.42],
        [1.6,   'LHCb',  'JHEP 06 (2021) 044'],
        [1.1,   'BaBar', 'Phys. Rev. D84 (2011) 072006'],
    ],
    r'$\pi^+\pi^0e^+e^-$':
    [
        [14.0, 'BESIII', 'Phys. Rev. D97 (2018) 072015', 2.93],
    ],
    r'$\pi^+\mu^+\mu^-$':
    [
        [220.0, 'E653',  'Phys. Lett. B345 (1995) 85'],
        [89.0,  'E687',  'Phys. Lett. B398 (1997) 239'],
        [15.0,  'E791',  'Phys. Lett. B462 (1999) 401'],
        [8.8,   'Focus', 'Phys. Lett. B572 (2003) 21'],
        [6.5,   'BaBar', 'Phys. Rev. D84 (2011) 072006'],
        [3.9,   'D0',    'Phys. Rev. Lett. 100 (2008) 101801'],
        [0.067, 'LHCb',  'JHEP 06 (2021) 044'],
    ],
    r'$\rho^+\mu^+\mu^-$':
    [
        [560.0, 'E653', 'Phys. Lett. B345 (1995) 85'],
    ],
    r'$K^+e^+e^-$':
    [
        [200.0, 'E687',  'Phys. Lett. B398 (1997) 239'],
        [3.0,   'CLEOc',  'Phys. Rev. D82 (2010) 092007', 1.42],
        [1.0,   'BaBar', 'Phys. Rev. D84 (2011) 072006'],
        [0.85,  'LHCb',  'JHEP 06 (2021) 044'],
    ],
    r'$K^+\mu^+\mu^-$':
    [
        [97.0,  'E687',  'Phys. Lett. B398 (1997) 239'],
        [44.0,  'E791',  'Phys. Lett. B462 (1999) 401'],
        [9.2,   'Focus', 'Phys. Lett. B572 (2003) 21'],
        [4.3,   'BaBar', 'Phys. Rev. D84 (2011) 072006'],
        [0.054, 'LHCb',  'JHEP 06 (2021) 044'],
    ],
    r'$K^+\pi^0e^+e^-':
    [
        [15.0, 'BESIII', 'Phys. Rev. D97 (2018) 072015', 2.93],
    ],
    r'$K_S^0\pi^+e^+e^-$':
    [
        [26.0, 'BESIII', 'Phys. Rev. D97 (2018) 072015', 2.93],
    ],
    r'$K_S^0K^+e^+e^-$':
    [
        [11.0, 'BESIII', 'Phys. Rev. D97 (2018) 072015', 2.93],
    ]
}

lfv_dp = {
    r'$\pi^+e^{\pm}\mu^{\mp}$':
    [
        [34.0, 'E791', 'Phys. Lett. B462 (1999) 401'],
    ],
    r'$\pi^+e^+\mu^-$':
    [
        [110.0, 'E687',  'Phys. Lett. B398 (1997) 239'],
        [2.9,   'BaBar', 'Phys. Rev. D84 (2011) 072006'],
        [0.21,  'LHCb',  'JHEP 06 (2021) 044'],
    ],
    r'$\pi^+\mu^+e^-$':
    [
        [130.0, 'E687', 'Phys. Lett. B398 (1997) 239'],
        [3.6,   'BaBar', 'Phys. Rev. D84 (2011) 072006'],
        [0.22,  'LHCb',	'JHEP 06 (2021) 044'],
    ],
    r'$K^+e^{\pm}\mu^{mp}$':
    [
        [68.0, 'E791', 'Phys. Lett. B462 (1999) 401'],
    ],
    r'$K^+e^+\mu^-$':
    [
        [130.0, 'E687',  'Phys. Lett. B398 (1997) 239'],
        [1.2,   'BaBar', 'Phys. Rev. D84 (2011) 072006'],
        [0.075, 'LHCb',  'JHEP 06 (2021) 044'],
    ],
    r'$K^+\mu^+e^-$':
    [
        [120.0, 'E687', 'Phys. Lett. B398 (1997) 239'],
        [2.8, 'BaBar', 'Phys. Rev. D84 (2011) 072006'],
        [0.1, 'LHCb',  'JHEP 06 (2021) 044'],
    ],
    r'$\pi^-e^+e^+$':
    [
        [110.0, 'E687',  'Phys. Lett. B398 (1997) 239'],
        [96.0,  'E791',  'Phys. Lett. B462 (1999) 401'],
        [1.9,   'BaBar', 'Phys. Rev. D84 (2011) 072006'],
        [1.1,   'CLEOc', 'Phys. Rev. D82 (2010) 092007', 1.42],
        [0.53,  'LHCb',  'JHEP 06 (2021) 044'],
    ],
    r'$\pi^-\mu^+\mu^+$':
    [
        [87.0, 'E687',  'Phys. Lett. B398 (1997) 239'],
        [17.0, 'E791',  'Phys. Lett. B462 (1999) 401'],
        [4.8,  'Focus', 'Phys. Lett. B572 (2003) 21'],
        [2.0,  'BaBar', 'Phys. Rev. D84 (2011) 072006'],
        [0.014, 'LHCb', 'JHEP 06 (2021) 044'],
    ],
    r'$\pi^-e^+\mu^+$':
    [
        [110.0, 'E687', 'Phys. Lett. B398 (1997) 239'],
        [50.0,  'E791', 'Phys. Lett. B462 (1999) 401'],
        [0.13,  'LHCb', 'JHEP 06 (2021) 044'],
    ],
    r'$\rho^-\mu^+\mu^+':
    [
        [560.0, 'E653', 'Phys. Lett. B345 (1995) 85'],
    ],
    r'$K^-e^+e^+$':
    [
        [120.0, 'E687', 'Phys. Lett. B398 (1997) 239'],
        [3.5,   'CLEOc'	'Phys. Rev. D82 (2010) 092007', 1.42],
        [0.9,   'BaBar'	'Phys. Rev. D84 (2011) 072006'],
    ],
K-μ+μ+	320.0	E653	K. Kodama et al., Phys. Lett. B345 (1995) 85
120.0	E687	P.L. Frabetti et al., Phys. Lett. B398 (1997) 239
13.0	Focus	J.M. Link et al., Phys. Lett. B572 (2003) 21
10.0	BaBar	J.P. Lees et al., Phys. Rev. D84 (2011) 072006
K-e+μ+	130.0	E687	P.L. Frabetti et al., Phys. Lett. B398 (1997) 239
K-π0e+e+	8.5	BESIII	M. Ablikim et al., Phys. Rev. D99 (2019) 112002
KSπ-e+e+	3.3	BESIII	M. Ablikim et al., Phys. Rev. D99 (2019) 112002
K*-(892)μ+μ+	850.0	E653	K. Kodama et al., Phys. Lett. B345 (1995) 85

print('gamma gamma: ', 3.80 * np.sqrt(2.92 / 10**3))
