import numpy as np


raredata_dn = {
    r'$\gamma\gamma':
    [
        [26.00, 'CLEOII',  'Phys. Rev. Lett. 90 (2003) 101801', 0.],
        [ 3.80, 'BESIII',  'Phys. Rev. D91 (2015) 112015', 2.92],
        [ 2.20, 'BaBar',   'Phys. Rev. D85 (2012) 091107', 0.],
        [ 0.85, 'Belle',   'Phys. Rev. D93 (2016) 051102', 0.],
    ],
    r'$e^+e^-$':
    [
        [220.000, 'CLEO',   'Phys. Rev. Lett. 60 (1988) 1614'],
        [170.000, 'Argus',  'Phys. Lett. B209 (1988) 380'],
        [130.000, 'Mark3',  'Phys. Rev. D37 (1988) 2023'],
        [ 13.000, 'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065'],
        [  8.190, 'E789',   'Phys. Rev. D61 (2000) 032005'],
        [  6.200, 'E791',   'Phys. Lett. B462 (1999) 401'],
        [  1.200, 'BaBar',  'Phys. Rev. Lett. 93 (2004) 191801'],
        [  0.079, 'Belle',  'Phys. Rev. D81 (2010) 091102R'],
    ],
    r'$\mu^+\mu^-$':
    [
        [70.0,    'Argus',  'Phys. Lett. B209 (1988) 380'],
        [44.0,    'E653',   'Phys. Lett. B345 (1995) 85'],
        [34.0,    'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065'],
        [15.6,    'E789',   'Phys. Rev. D61 (2000) 032005'],
        [ 5.2,    'E791',   'Phys. Lett. B462 (1999) 401'],
        [ 2.0,    'HERAb',  'Phys. Lett. B596 (2004) 173'],
        [ 1.3,    'BaBar',  'Phys. Rev. Lett. 93 (2004) 191801'],
        [ 0.21,   'CDF',    'Phys. Rev. D82 (2010) 091105R'],
        [ 0.14,   'Belle',  'Phys. Rev. D81 (2010) 091102R'],
        [ 0.0062, 'LHCb',   'Phys.Lett. B725 (2013) 15'],
    ],
    r'$\pi^0e^+e^-$':
    [
        [45.0, 'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065'],
        [ 4.0, 'BESIII', 'Phys. Rev. D97 (2018) 072015'],
    ],
    r'$\pi^0\mu^+\mu^-$':
    [
        [540.0, 'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065'],
        [180.0, 'E653',   'Phys. Lett. B345 (1995) 85'],
    ],
    r'$\eta e^+e^-$':
    [
        [110.0, 'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065'],
        [  3.0, 'BESIII', 'Phys. Rev. D97 (2018) 072015'],
    ],
    r'$\eta\mu^+\mu^-$':
    [
        [530.0, 'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065'],
    ],
    r'$\pi^+\pi^-e^+e^-$':
    [
        [370.0, 'E791',   'Phys. Rev. Lett. 86 (2001) 3969'],
        [  7.0, 'BESIII', 'Phys. Rev. D97 (2018) 072015'],
    ],
    r'$K_S^0 e^+e^-$':
    [
        [12.0, 'BESIII', 'Phys. Rev. D97 (2018) 072015'],
    ],
    r'$\rho^0e^+e^-$':
    [
        [450.0, 'CLEO',   'Phys. Rev. Lett. 60 (1988) 1614'],
        [124.0, 'E791',   'Phys. Rev. Lett. 86 (2001) 3969'],
        [100.0, 'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065'],
    ],
    r'$\pi^+\pi^-\mu^+\mu^-$':
    [
        [30.0, 'E791', 'Phys. Rev. Lett. 86 (2001) 3969'],
        [(0.964, 0.048, 0.051, 0.097), 'LHCb', 'Phys. Rev. Lett. 119 (2017) 181805'],
    ],
    r'$\rho^0\mu^+\mu^-$':
    [
        [810.0, 'CLEO',   'Phys. Rev. Lett. 60 (1988) 1614'],
        [490.0, 'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065'],
        [230.0, 'E653',   'Phys. Lett. B345 (1995) 85'],
        [ 22.0, 'E791',   'Phys. Rev. Lett. 86 (2001) 3969'],
    ],
    r'\omega e^+e^-':
    [
        [180.0, 'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065'],
        [  6.0, 'BESIII', 'Phys. Rev. D97 (2018) 072015'],
    ],
    r'$\omega\mu^+\mu^-$':
    [
        [830.0, 'CLEOII', 'Phys. Rev. Lett. 76 (1996) 3065'],
    ],
    r'$K^+K^-e^+e^-$':
    [
        [315.0, 'E791',   'Phys. Rev. Lett. 86 (2001) 3969'],
        [ 11.0, 'BESIII', 'Phys. Rev. D97 (2018) 072015'],
    ],
# φe+e-	59.0	E791	E.M. Aitala et al., Phys. Rev. Lett. 86 (2001) 3969
# 52.0	CLEOII	A. Freyberger et al., Phys. Rev. Lett. 76 (1996) 3065
# K+K-μ+μ-	33.0	E791	E.M. Aitala et al., Phys. Rev. Lett. 86 (2001) 3969
# 0.154±0.027±0.009±0.016	LHCb	R. Aaij et al., Phys. Rev. Lett. 119 (2017) 181805
# φμ+μ-	410.0	CLEOII	A. Freyberger et al., Phys. Rev. Lett. 76 (1996) 3065
# 31.0	E791	E.M. Aitala et al., Phys. Rev. Lett. 86 (2001) 3969
# K0e+e-	1700.0	Mark3	J. Adler et al., Phys. Rev. D40 (1989) 906
# 110.0	CLEOII	A. Freyberger et al., Phys. Rev. Lett. 76 (1996) 3065
# K0μ+μ-	670.0	CLEOII	A. Freyberger et al., Phys. Rev. Lett. 76 (1996) 3065
# 260.0	E653	K. Kodama et al., Phys. Lett. B345 (1995) 85
# K-π+e+e-	385.0	E791	E.M. Aitala et al., Phys. Rev. Lett. 86 (2001) 3969
# 41.0	BESIII	M. Ablikim et al., Phys. Rev. D97 (2018) 072015
# K-π+(e+e-)ρ/ω	4.0±0.5±0.2±0.1	BaBar	J.P. Lees et al., Phys. Rev. Lett. 122 (2018) 081802
# K*0(892)e+e-	140.0	CLEOII	A. Freyberger et al., Phys. Rev. Lett. 76 (1996) 3065
# 47.0	E791	E.M. Aitala et al., Phys. Rev. Lett. 86 (2001) 3969
# K-π+μ+μ-	360.0	E791	E.M. Aitala et al., Phys. Rev. Lett. 86 (2001) 3969
# K-π+(μ+μ-)ρ/ω	4.17±0.12±0.40	LHCb	R. Aaij et al., Phys.Lett. B757 (2016) 558
# K*0(892)μ+μ-	1180.0	CLEOII	A. Freyberger et al., Phys. Rev. Lett. 76 (1996) 3065
# 24.0	E791	E.M. Aitala et al., Phys. Rev. Lett. 86 (2001) 3969
# π+π-π0μ+μ-	810.0	E653	K. Kodama et al., Phys. Lett. B345 (1995) 85
# ρ0γ	240.0	CLEOII	D. Asner et al., Phys. Rev. D58 (1998) 092001
# 17.7±3.0±0.7	Belle	T. Nanut et al., Phys. Rev. Lett. 118 (2017) 051801
# ωγ	240.0	CLEOII	D. Asner et al., Phys. Rev. D58 (1998) 092001
# K*0(892)γ	760.0	CLEOII	D. Asner et al., Phys. Rev. D58 (1998) 092001
# 322.0±20.0±27.0	BaBar	B. Aubert et al., Phys. Rev. D78 (2008) 071101
# φγ	190.0	CLEOII	D. Asner et al., Phys. Rev. D58 (1998) 092001
# 27.3±3.0±2.6	BaBar	B. Aubert et al., Phys. Rev. D78 (2008) 071101
# μ±e∓	270.0	CLEO	P. Haas et al., Phys. Rev. Lett. 60 (1988) 1614
# 120.0	Mark3	J. Becker et al., Phys. Lett. B193 (1987) 147
# 100.0	Argus	H. Albrecht et al., Phys. Lett. B209 (1988) 380
# 19.0	CLEOII	A. Freyberger et al., Phys. Rev. Lett. 76 (1996) 3065
# 17.2	E789	D. Pripstein et al., Phys. Rev. D61 (2000) 032005
# 8.1	E791	E.M. Aitala et al., Phys. Lett. B462 (1999) 401
# 0.81	BaBar	B. Aubert et al., Phys. Rev. Lett. 93 (2004) 191801
# 0.26	Belle	M. Petric et al., Phys. Rev. D81 (2010) 091102R
# 0.016	LHCb	R. Aaij et al., Phys.Lett. B754 (2016) 167
# π0e±μ∓	86.0	CLEOII	A. Freyberger et al., Phys. Rev. Lett. 76 (1996) 3065
# 0.8	BaBar	J.P. Lees et al., Phys. Rev. D101 (2020) 112003
# ηe±μ∓	100.0	CLEOII	A. Freyberger et al., Phys. Rev. Lett. 76 (1996) 3065
# 2.3	BaBar	J.P. Lees et al., Phys. Rev. D101 (2020) 112003
# π+π-e±μ∓	15.0	E791	E.M. Aitala et al., Phys. Rev. Lett. 86 (2001) 3969
# 1.7	BaBar	J.P. Lees et al., Phys. Rev. Lett. 124 (2020) 071802
# ρ0e±μ∓	66.0	E791	E.M. Aitala et al., Phys. Rev. Lett. 86 (2001) 3969
# 49.0	CLEOII	A. Freyberger et al., Phys. Rev. Lett. 76 (1996) 3065
# 0.5	BaBar	J.P. Lees et al., Phys. Rev. D101 (2020) 112003
# ωe±μ∓	120.0	CLEOII	A. Freyberger et al., Phys. Rev. Lett. 76 (1996) 3065
# 1.7	BaBar	J.P. Lees et al., Phys. Rev. D101 (2020) 112003
# K+K-e±μ∓	180.0	E791	E.M. Aitala et al., Phys. Rev. Lett. 86 (2001) 3969
# 1.0	BaBar	J.P. Lees et al., Phys. Rev. Lett. 124 (2020) 071802
# φe±μ∓	47.0	E791	E.M. Aitala et al., Phys. Rev. Lett. 86 (2001) 3969
# 34.0	CLEOII	A. Freyberger et al., Phys. Rev. Lett. 76 (1996) 3065
# 0.51	BaBar	J.P. Lees et al., Phys. Rev. D101 (2020) 112003
# K0e±μ∓	100.0	CLEOII	A. Freyberger et al., Phys. Rev. Lett. 76 (1996) 3065
# 0.86	BaBar	J.P. Lees et al., Phys. Rev. D101 (2020) 112003
# K-π+e±μ∓	550.0	E791	E.M. Aitala et al., Phys. Rev. Lett. 86 (2001) 3969
# 1.9	BaBar	J.P. Lees et al., Phys. Rev. Lett. 124 (2020) 071802
# K*0(892)e±μ∓	100.0	CLEOII	A. Freyberger et al., Phys. Rev. Lett. 76 (1996) 3065
# 83.0	E791	E.M. Aitala et al., Phys. Rev. Lett. 86 (2001) 3969
# 1.2	BaBar	J.P. Lees et al., Phys. Rev. D101 (2020) 112003
# π∓π∓e±e±	112.0	E791	E.M. Aitala et al., Phys. Rev. Lett. 86 (2001) 3969
# 0.91	BaBar	J.P. Lees et al., Phys. Rev. Lett. 124 (2020) 071802
# π∓π∓μ±μ±	29.0	E791	E.M. Aitala et al., Phys. Rev. Lett. 86 (2001) 3969
# 1.5	BaBar	J.P. Lees et al., Phys. Rev. Lett. 124 (2020) 071802
# K∓π∓e±e±	206.0	E791	E.M. Aitala et al., Phys. Rev. Lett. 86 (2001) 3969
# 2.8	BESIII	M. Ablikim et al., Phys. Rev. D99 (2019) 112002
# 0.5	BaBar	J.P. Lees et al., Phys. Rev. Lett. 124 (2020) 071802
# K∓π∓μ±μ±	390.0	E791	E.M. Aitala et al., Phys. Rev. Lett. 86 (2001) 3969
# 0.53	BaBar	J.P. Lees et al., Phys. Rev. Lett. 124 (2020) 071802
# K∓K∓e±e±	152.0	E791	E.M. Aitala et al., Phys. Rev. Lett. 86 (2001) 3969
# 0.34	BaBar	J.P. Lees et al., Phys. Rev. Lett. 124 (2020) 071802
# K∓K∓μ±μ±	94.0	E791	E.M. Aitala et al., Phys. Rev. Lett. 86 (2001) 3969
# 0.1	BaBar	J.P. Lees et al., Phys. Rev. Lett. 124 (2020) 071802
# π∓π∓e±μ±	79.0	E791	E.M. Aitala et al., Phys. Rev. Lett. 86 (2001) 3969
# 3.1	BaBar	J.P. Lees et al., Phys. Rev. Lett. 124 (2020) 071802
# K∓π∓e±μ±	218.0	E791	E.M. Aitala et al., Phys. Rev. Lett. 86 (2001) 3969
# 2.1	BaBar	J.P. Lees et al., Phys. Rev. Lett. 124 (2020) 071802
# K∓K∓e±μ±	57.0	E791	E.M. Aitala et al., Phys. Rev. Lett. 86 (2001) 3969
# 0.58	BaBar	J.P. Lees et al., Phys. Rev. Lett. 124 (2020) 071802
# pe-	10.0	CLEO	P. Rubin et al., Phys. Rev. D79 (2009) 097101
# pe+	11.0	CLEO	P. Rubin et al., Phys. Rev. D79 (2009) 097101


print('gamma gamma: ', 3.80 * np.sqrt(2.92 / 10**3))
