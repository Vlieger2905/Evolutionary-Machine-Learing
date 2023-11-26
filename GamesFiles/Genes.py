# Safe file
from numpy import *
Genes = [
[{'weights': array([[-0.43771201,  1.        ,  1.        , -1.        , -0.23614289,
        -0.09801838, -1.        ,  1.        ],
       [-0.09720928, -0.38106255, -1.        ,  0.11913578,  0.59482803,
         1.        , -1.        ,  1.        ],
       [-1.        ,  0.34724153, -0.21548493,  1.        ,  0.04729959,
         1.        ,  0.49349095,  0.52055102],
       [ 1.        , -1.        , -0.3555083 , -0.17784487,  1.        ,
        -0.97135005, -0.09612037,  1.        ],
       [-0.57771905, -1.        ,  0.80252419, -1.        ,  1.        ,
         0.49029199,  0.32003111, -0.5136996 ]]), 'biases': array([[ 1.        ,  0.10920259, -0.34089869, -1.        ,  0.14458296,
        -0.08407126,  0.42602756,  1.        ]])}, {'weights': array([[ 1.        , -1.        , -0.72648201, -1.        ,  1.        ,
         0.38208883,  1.        ,  0.09461896],
       [-0.38007928,  0.38443698, -0.34916133, -0.48628065, -1.        ,
        -1.        , -1.        , -0.61859332],
       [-0.08169479,  0.09245757, -0.0164796 ,  0.74865789, -1.        ,
         0.12613657, -0.12714689, -0.94323719],
       [ 0.08245305,  1.        , -1.        ,  0.64515981, -0.60022712,
        -0.12901592,  0.79167588,  0.22608809],
       [-1.        ,  0.39344561, -1.        , -0.17392552,  0.97948419,
        -0.78475516,  0.708847  ,  0.82958931],
       [ 0.7566461 , -1.        , -0.37052128,  1.        ,  0.90836894,
         1.        , -0.14783037,  0.56730144],
       [-0.76977847, -0.37752794, -1.        , -0.96948847, -0.68885052,
        -0.42254227,  0.5416757 ,  0.37150329],
       [ 0.92046839, -0.32084026,  0.52690105, -0.15842432, -0.11794115,
         0.0712252 ,  1.        , -0.91268381]]), 'biases': array([[ 0.97454793,  0.11267519,  0.63169932,  0.70118738, -0.88616875,
        -0.47117335,  0.40795661, -0.20709466]])}, {'weights': array([[-0.31482562, -0.6350931 , -1.        ,  0.08235987,  0.04081316],
       [ 0.05461174,  0.03255895, -0.7480989 ,  0.97369776, -0.1966442 ],
       [-0.69662023,  1.        ,  0.64146445,  0.65728935, -0.00369582],
       [ 1.        ,  0.17744028,  0.01243935, -1.        , -0.42686664],
       [ 1.        , -0.14815166,  0.71470374,  0.72179042,  1.        ],
       [ 0.65347895,  0.60088726,  0.0359741 ,  0.36253411, -0.0679913 ],
       [ 0.75868708, -0.58481273,  1.        ,  0.25626308, -1.        ],
       [-1.        , -0.49322211,  1.        , -0.46655351,  0.13655914]]), 'biases': array([[ 0.08485596,  1.        ,  0.45342097, -0.27680269,  0.56706388]])}]

,[{'weights': array([[ 1.        , -0.0753339 ,  0.73900108,  1.        , -1.        ,
        -1.        , -0.3419366 ,  0.74589419],
       [ 1.        , -0.38748246, -0.10343187, -0.40846981,  0.16526614,
        -0.57537111, -0.10325593,  1.        ],
       [ 1.        ,  1.        ,  0.14714581,  0.33355288,  0.17688566,
        -0.25210221, -0.13389537, -1.        ],
       [-0.27503422,  1.        , -1.        , -0.32400829,  1.        ,
        -0.07780301, -1.        ,  1.        ],
       [-1.        ,  1.        , -1.        ,  0.70015705, -0.54817173,
        -1.        , -1.        ,  0.92820612]]), 'biases': array([[ 0.16294237, -0.98858501,  1.        , -0.47582372,  0.82082586,
         1.        , -0.4211144 , -0.43256681]])}, {'weights': array([[ 0.55561022, -0.53143789,  0.52373352, -0.86058429,  1.        ,
        -0.29712693, -0.56757171, -0.2923089 ],
       [ 0.06346907,  0.37577384,  0.10682748,  0.34742948,  0.96230373,
        -0.72883248,  0.35598316, -0.93182138],
       [ 0.5310846 ,  1.        ,  0.78927945,  1.        ,  1.        ,
        -0.94968466, -0.48904407,  0.35914098],
       [ 0.02494563,  1.        ,  1.        , -1.        , -0.3528094 ,
         0.78431707, -0.58404898,  1.        ],
       [ 0.00253529, -1.        ,  1.        ,  0.31512623, -1.        ,
        -1.        , -1.        , -0.30561117],
       [ 0.11217008,  0.196785  ,  0.91803473,  0.20660575, -1.        ,
        -0.0950527 , -1.        ,  0.54377926],
       [-0.10958885, -0.00569316,  0.68043238,  0.74289129,  1.        ,
        -0.38672402,  0.95616391,  0.77602492],
       [ 0.25368461,  1.        ,  0.27121836,  0.35759879,  0.33539945,
        -0.17052667,  0.52174879,  0.84755177]]), 'biases': array([[-1.        ,  0.96736461, -0.49197953,  0.30226032, -0.45616502,
         0.96923605, -0.41198109,  0.59409454]])}, {'weights': array([[-0.08303453,  1.        , -1.        ,  1.        , -0.46321593],
       [ 0.54341639,  1.        ,  0.07300457,  0.7128847 , -1.        ],
       [-0.42484397,  0.1753291 , -0.36740004, -0.30022972, -0.49911466],
       [ 1.        , -0.39962006,  0.28916967,  1.        , -0.53514406],
       [ 0.240177  , -0.93348748, -1.        , -0.37816436, -0.37536631],
       [-0.16887076, -0.49775919, -1.        ,  1.        , -0.69945749],
       [ 1.        , -0.04374839, -1.        , -0.66720108, -0.79700004],
       [-0.20971168,  0.13724417,  1.        ,  1.        , -1.        ]]), 'biases': array([[-0.11721331, -0.67636906, -1.        ,  0.22940911,  0.08375994]])}]
          
,[{'weights': array([[ 0.34116961, -0.05520795, -0.22897777, -0.86020867, -0.11134593,
        -0.1471833 , -0.15639518,  1.        ],
       [ 1.        , -0.26432185,  1.        , -0.29495345, -0.97845219,
         1.        ,  0.24491868,  0.93669372],
       [-0.69465143,  1.        ,  0.78141702,  0.3492069 ,  0.17275392,
         0.80769418,  0.20455412, -0.56524274],
       [-1.        ,  1.        ,  0.3412163 ,  1.        ,  0.70915217,
        -1.        ,  0.63813394,  0.58901712],
       [-0.3124123 ,  1.        , -0.18287945,  0.58814144, -1.        ,
        -1.        , -0.21384612, -1.        ]]), 'biases': array([[-0.37047027, -1.        , -1.        , -0.28036339, -0.05584868,
        -1.        , -0.47694798, -0.49448673]])}, {'weights': array([[ 0.57580673,  0.63333318,  0.05102145,  0.21629778, -0.12248718,
         1.        , -0.30881034, -0.00938403],
       [ 0.02082878,  1.        ,  0.75262881,  1.        ,  0.171598  ,
        -1.        ,  0.04703305,  0.7509533 ],
       [ 0.94778461, -0.01708621, -0.76017101,  0.71923514,  1.        ,
         0.8552765 ,  0.2719982 ,  0.59811035],
       [-0.47535599, -0.21805929,  0.5047384 ,  0.27181792,  1.        ,
        -0.19311843, -0.16211795, -1.        ],
       [-0.39115847,  0.41051747, -1.        ,  0.17767211,  0.45210124,
        -1.        ,  0.72237722,  0.3746272 ],
       [-1.        , -0.64369295, -0.74835488,  1.        ,  0.03958112,
        -0.10021537, -0.48504385,  1.        ],
       [ 0.96960604, -0.26564435,  1.        ,  0.22448464, -0.79167397,
         1.        ,  0.67161366, -0.54629439],
       [-0.46767064,  0.99076425,  0.40826382, -0.79632063, -0.43596825,
         0.02119061,  0.35884348, -1.        ]]), 'biases': array([[ 0.92799353, -0.57667845, -0.79243748, -1.        ,  0.07169931,
         0.75552293, -0.62658519,  1.        ]])}, {'weights': array([[-0.01866219, -1.        , -0.89018863,  0.56615344, -0.21731576],
       [ 0.70437468,  0.69661494,  0.97084356, -0.96506207,  1.        ],
       [-1.        , -0.26513911, -1.        ,  0.87091898, -1.        ],
       [-0.11930298,  0.74662648,  1.        , -1.        , -0.03920835],
       [ 1.        ,  0.5280683 , -0.25711343, -1.        , -0.38255982],
       [ 1.        , -1.        , -0.06619055, -1.        , -1.        ],
       [-0.79776989,  0.14587642,  0.96488656, -1.        , -0.49097346],
       [ 1.        ,  0.657389  , -0.72581968,  0.17603533, -1.        ]]), 'biases': array([[-0.11775669,  0.29514953,  0.62886522,  0.77475413, -1.        ]])}]

,[{'weights': array([[-0.19064539,  1.        ,  0.87039579, -0.03753209, -1.        ,
         1.        ,  0.02723565,  0.19745665],
       [ 1.        ,  0.59092103,  0.46433936, -0.96603206, -0.89766166,
         0.06999017, -1.        , -0.25730987],
       [-0.75476311,  0.45926743,  1.        ,  0.46383023,  0.92260813,
         1.        , -0.71607435, -1.        ],
       [-0.14199498, -0.59827419, -0.83225566,  0.16172474,  1.        ,
         0.73054547,  1.        , -1.        ],
       [ 0.17493106,  0.00782513, -1.        ,  1.        ,  0.74337407,
         1.        , -0.89036212, -0.1917309 ]]), 'biases': array([[-1.        ,  0.81067384,  0.39270577, -0.95277289, -0.16328739,
         0.85708792, -0.17349394,  1.        ]])}, {'weights': array([[ 0.61671072, -1.        ,  0.02769742, -0.29411643, -0.26013782,
         0.31416013,  1.        , -1.        ],
       [ 0.50710226,  0.79596201, -0.77952859,  0.07658808, -0.93201375,
        -1.        ,  0.56257533, -0.44001528],
       [ 0.33807265,  0.7687132 ,  0.90602487,  1.        ,  1.        ,
        -1.        , -0.01500246,  0.83660754],
       [-0.37410553, -1.        , -0.82578099,  1.        ,  0.08109463,
         0.32898987,  1.        ,  0.30558885],
       [ 1.        , -1.        , -0.93776646,  0.53494859,  0.86048226,
        -0.38487015, -1.        ,  0.53673359],
       [ 0.39757206, -0.10581204, -1.        ,  0.12626117, -0.38923779,
        -0.24592115, -1.        , -0.24100691],
       [ 0.79723348, -0.06566428, -0.9702564 ,  0.23168639,  1.        ,
         0.73265594,  0.39237924,  0.64630594],
       [-0.60732458, -0.20104497,  0.05714845,  0.28841674, -0.31782295,
        -1.        ,  0.02304007,  0.26915478]]), 'biases': array([[-1.        , -0.17070057, -0.57462428, -0.38118674,  0.44943983,
         0.18653826,  0.1513107 , -0.21446572]])}, {'weights': array([[ 1.        , -1.        ,  0.37750862,  0.48494693,  0.38686956],
       [ 0.57943928, -0.00905401, -0.81314787,  1.        , -0.01737396],
       [ 1.        ,  0.1992132 ,  0.76106884,  0.67240951, -1.        ],
       [-1.        ,  1.        , -0.07973625,  0.11066145,  0.66955883],
       [ 0.2513743 ,  1.        , -0.19242007,  0.77010968, -0.04082543],
       [-1.        ,  0.43928242, -1.        , -0.84542359,  0.84443779],
       [-0.93330164,  0.06124158,  0.94399529, -0.04454513, -0.42518816],
       [ 1.        , -0.34059388,  1.        , -0.34079777,  0.74026198]]), 'biases': array([[ 1.        , -1.        ,  0.02685659, -1.        ,  1.        ]])}]

,[{'weights': array([[-1.        ,  0.00836329, -1.        , -1.        ,  1.        ,
        -0.19878685,  0.39524283, -0.3764071 ],
       [ 0.20719342,  0.40025203,  0.33442727, -1.        ,  0.36393043,
         0.83698524,  0.09843605, -0.31324959],
       [ 0.3054455 ,  0.44817621,  0.40707052, -0.766502  , -0.91893556,
         0.91663428,  0.54789555,  1.        ],
       [ 0.41001566,  0.11036331,  0.16769661, -0.82064701,  0.68742363,
         1.        , -0.23823595,  0.91515434],
       [ 0.20086705,  0.80318873,  1.        , -1.        ,  0.82441613,
        -0.1366956 ,  0.95158842, -1.        ]]), 'biases': array([[ 1.        , -0.68124199,  0.13799077,  0.45125316,  0.19744169,
        -1.        , -0.41784162,  0.07587647]])}, {'weights': array([[ 1.        , -0.54734593,  1.        , -0.71695227, -1.        ,
         1.        , -0.40656136, -1.        ],
       [ 0.93145048,  0.04848948,  0.60168486, -1.        , -1.        ,
        -1.        ,  0.90112314,  0.88232623],
       [-1.        , -1.        , -0.3307824 ,  0.68704592, -0.17137252,
        -1.        , -0.69193899,  1.        ],
       [-0.28775488,  0.57679417, -0.27743658,  0.2745291 , -0.94258529,
        -0.92136425, -0.11692622,  1.        ],
       [ 0.14149208,  0.72256345, -1.        , -0.04271737, -1.        ,
        -1.        , -0.26466214,  0.01067489],
       [ 0.45276981, -1.        , -0.74416034,  0.04596345,  0.65574883,
        -0.56785718,  1.        , -1.        ],
       [ 1.        , -0.45699688,  0.23958666, -0.61360361,  0.21876091,
         0.637668  , -0.13764232, -0.22447481],
       [ 1.        , -1.        , -1.        , -0.5181785 , -0.58970458,
        -1.        ,  0.31145638,  1.        ]]), 'biases': array([[ 1.        , -0.09274562,  0.41351126, -1.        ,  0.60733629,
        -0.07452043,  0.20333942,  1.        ]])}, {'weights': array([[-0.15740817, -1.        , -0.29998816, -0.17832092,  1.        ],
       [ 1.        , -0.86121873,  0.79138824,  0.40314969, -0.34428915],
       [-1.        , -0.64582648,  0.34789779, -0.75685815,  0.33387251],
       [-0.70664388,  0.17339319,  0.30013505,  0.00865417,  0.84649096],
       [-0.31467086, -0.06349244,  0.47133723,  0.52183965, -0.12809851],
       [-1.        , -0.06618811,  0.47476546,  0.84297995,  1.        ],
       [ 0.64619573, -1.        ,  0.65630574, -0.65935469,  0.48875917],
       [-0.07625514, -1.        , -0.85606102,  0.56498247,  0.07518765]]), 'biases': array([[-1.        ,  0.17429028,  0.87602151, -0.71549427,  0.57397352]])}]
]