import numpy as np
from openravepy import *

if __name__ == "__main__":
    env = Environment()
    env.SetViewer("qtcoin")
    # Transforms= np.genfromtxt('test.csv',delimiter = ',')
    # T = []
    # for index in range(64):
    #     t = Transforms[index*4:index*4+4]
    #     T.append(t)
    #     print index
    T = []
    q = []
    T1 = [[0.935414, -0, -0.353553, -0.735], [0, 1, -0, -0.465], [0.353553, 0, 0.935414, 0.125], [0, 0, 0, 1]]
    q1 = [-2.96131,    -0.089453,    2,    0.50305,    0.424896,    2.23278,    -0.834637]  
    T.append(T1)
    q.append(q1)

    T2 = [[0.633316, -0, -0.773893, -0.735], [0, 1, -0, -0.465], [0.773893, 0, 0.633316, 0.125], [0, 0, 0, 1]]
    q2 = [-2.96131,    -0.089453,    2,    0.50305,    0.819608,    1.84162,    -0.651818]
    T.append(T2)
    q.append(q2)

    T3 = [[0.378467, -0, -0.925615, -0.735], [0, 1, -0, -0.465], [0.925615, 0, 0.378467, 0.125], [0, 0, 0, 1]]
    q3 = [-2.96131,    -0.089453,    2,    0.50305,    0.998582,    1.60188,    -0.624639]
    T.append(T3)
    q.append(q3)

    T4 = [[0.126004, -0, -0.99203, -0.735], [0, 1, -0, -0.465], [0.99203, 0, 0.126004, 0.125], [0, 0, 0, 1]]
    q4 = [-2.96131,    -0.089453,    2,    0.50305,    1.15306,    1.38999,    -0.636281]
    T.append(T4)
    q.append(q4)

    T5 = [[-0.126004, -0, -0.99203, -0.735], [0, 1, -0, -0.465], [0.99203, 0, -0.126004, 0.125], [0, 0, 0, 1]]
    q5 = [-2.96131,    -0.089453,    2,    0.50305,    1.31379,    1.18972,    -0.681157]
    T.append(T5)
    q.append(q5)

    T6 = [[-0.378467, -0, -0.925615, -0.735], [0, 1, -0, -0.465], [0.925615, 0, -0.378467, 0.125], [0, 0, 0, 1]]
    q6 = [-2.96131,    -0.089453,    2,    0.50305,    1.50955,    0.993353,    -0.772093]
    T.append(T6)
    q.append(q6)

    T7 = [[-0.633316, 0, -0.773893, -0.735], [0, 1, 0, -0.465], [0.773893, 0, -0.633316, 0.125], [0, 0, 0, 1]]
    q7 = [-2.96131,    -0.089453,    2,    0.50305,    1.79932,    0.798271,    -0.954803]
    T.append(T7)
    q.append(q7)

    T8 = [[-0.935414, 0, -0.353553, -0.735], [0, 1, 0, -0.465], [0.353553, 0, -0.935414, 0.125], [0, 0, 0, 1]]
    q8 = [-2.96131,    -0.089453,    2,    0.50305,    2.57204,    0.624383,    -1.55478]
    T.append(T8)
    q.append(q8)

    T9 = [[0.661438, 0.661438, -0.353553, -0.735], [-0.707107, 0.707107, 2.77556e-17, -0.465], [0.25, 0.25, 0.935414, 0.125], [0, 0, 0, 1]]
    q9 = [-2.96131,    -0.089453,    2,    0.50305,    -0.0699456,    1.59213,    -1.0125]
    T.append(T9)
    q.append(q9)

    T10 = [[0.447822, 0.447822, -0.773893, -0.735], [-0.707107, 0.707107, 8.32667e-16, -0.465], [0.547225, 0.547225, 0.633316, 0.125], [0, 0, 0, 1]]
    q10 = [-2.96131,    -0.089453,    2,    0.50305,    0.204785,    1.34472,    -0.666474]
    T.append(T10)
    q.append(q10)

    T11 = [[0.267617, 0.267617, -0.925615, -0.735], [-0.707107, 0.707107, 4.44089e-16, -0.465], [0.654508, 0.654508, 0.378467, 0.125], [0, 0, 0, 1]]
    q11 = [-2.96131,    -0.089453,    2,    0.50305,    0.325628,    1.1687,    -0.492716]
    T.append(T11)
    q.append(q11)    

    T12 = [[0.0890985, 0.0890985, -0.99203, -0.735], [-0.707107, 0.707107, 6.66134e-16, -0.465], [0.701471, 0.701471, 0.126004, 0.125], [0, 0, 0, 1]]
    q12 = [-2.96131,    -0.089453,    2,    0.50305,    0.410782,    0.999793,    -0.347043]
    T.append(T12)
    q.append(q12)

    T13 = [[-0.0890985, -0.0890985, -0.99203, -0.735], [-0.707107, 0.707107, -6.66134e-16, -0.465], [0.701471, 0.701471, -0.126004, 0.125], [0, 0, 0, 1]]
    q13 = [-2.96131,    -0.089453,    2,    0.50305,    0.472174,    0.828062,    -0.20553]
    T.append(T13)
    q.append(q13)

    T14 = [[-0.267617, -0.267617, -0.925615, -0.735], [-0.707107, 0.707107, -4.44089e-16, -0.465], [0.654508, 0.654508, -0.378467, 0.125], [0, 0, 0, 1]]
    q14 = [-2.96131,    -0.089453,    2,    0.50305,    0.506582,    0.644638,    -0.0454827]
    T.append(T14)
    q.append(q14)

    T15 = [[-0.447822, -0.447822, -0.773893, -0.735], [-0.707107, 0.707107, -8.32667e-16, -0.465], [0.547225, 0.547225, -0.633316, 0.125], [0, 0, 0, 1]]
    q15 = [-2.96131,    -0.089453,    2,    0.50305,    0.476827,    0.435067,    0.19146]
    T.append(T15)
    q.append(q15)

    T16 = [[-0.661438, -0.661438, -0.353553, -0.735], [-0.707107, 0.707107, -2.77556e-17, -0.465], [0.25, 0.25, -0.935414, 0.125], [0, 0, 0, 1]]
    q16 = [-2.96131,    -0.089453,    2,    0.50305,    -0.499003,    0.161345,    1.51249]
    T.append(T16)
    q.append(q16)

    T17 = [[0, 0.935414, -0.353553, -0.735], [-1, 0, 0, -0.465], [0, 0.353553, 0.935414, 0.125], [0, 0, 0, 1]]
    q17 = [-2.96131,    -0.089453,    2,    0.50305,    -0.549813,    0.946506,    -0.859601]
    T.append(T17)
    q.append(q17)

    T18 = [[-2.22045e-16, 0.633316, -0.773893, -0.735], [-1, -2.22045e-16, 0, -0.465], [0, 0.773893, 0.633316, 0.125], [0, 0, 0, 1]]
    q18 = [-2.96131,    -0.089453,    2,    0.50305,    -0.549813,    0.946506,    -0.336002]
    T.append(T18)
    q.append(q18)

    T19 = [[-8.88178e-16, 0.378467, -0.925615, -0.735], [-1, -8.88178e-16, 0, -0.465], [0, 0.925615, 0.378467, 0.125], [0, 0, 0, 1]]
    q19 = [-2.96131,    -0.089453,    2,    0.50305,    -0.549813,    0.946506,    -0.0383112]
    T.append(T19)
    q.append(q19)

    T20 = [[4.44089e-16, 0.126004, -0.99203, -0.735], [-1, 4.44089e-16, 0, -0.465], [0, 0.99203, 0.126004, 0.125], [0, 0, 0, 1]]
    q20 = [-2.96131,    -0.089453,    2,    0.50305,    -0.549813,    0.946506,    0.223488]
    T.append(T20)
    q.append(q20)

    T21 = [[4.44089e-16, -0.126004, -0.99203, -0.735], [-1, 4.44089e-16, 0, -0.465], [0, 0.99203, -0.126004, 0.125], [0, 0, 0, 1]]
    q21 = [-2.96131,    -0.089453,    2,    0.50305,    -0.549813,    0.946506,    0.476168]
    T.append(T21)
    q.append(q21)

    T22 = [[-8.88178e-16, -0.378467, -0.925615, -0.735], [-1, -8.88178e-16, 0, -0.465], [0, 0.925615, -0.378467, 0.125], [0, 0, 0, 1]]
    q22 = [-2.96131,    -0.089453,    2,    0.50305,    -0.549813,    0.946506,    0.737968]
    T.append(T22)
    q.append(q22)

    T23 = [[-2.22045e-16, -0.633316, -0.773893, -0.735], [-1, -2.22045e-16, 0, -0.465], [0, 0.773893, -0.633316, 0.125], [0, 0, 0, 1]]
    q23 = [-2.96131,    -0.089453,    2,    0.50305,    -0.549813,    0.946506,    1.03566]
    T.append(T23)
    q.append(q23)

    T24 = [[0, -0.935414, -0.353553, -0.735], [-1, 0, 0, -0.465], [0, 0.353553, -0.935414, 0.125], [0, 0, 0, 1]]
    q24 = [-2.96131,    -0.089453,    2,    0.50305,    -0.549813,    0.946506,    1.55926]
    T.append(T24)
    q.append(q24)

    T25 = [[-0.661438, 0.661438, -0.353553, -0.735], [-0.707107, -0.707107, -2.77556e-17, -0.465], [-0.25, 0.25, 0.935414, 0.125], [0, 0, 0, 1]]
    q25 = [-2.96131,    -0.089453,    2,    0.50305,    -1.60661,    0.558657,    -0.0402501]
    T.append(T25)
    q.append(q25)

    T26 = [[-0.447822, 0.447822, -0.773893, -0.735], [-0.707107, -0.707107, -8.32667e-16, -0.465], [-0.547225, 0.547225, 0.633316, 0.125], [0, 0, 0, 1]]
    q26 = [-2.96131,    -0.089453,    2,    0.50305,    -1.54052,    0.924182,    0.284676]
    T.append(T26)
    q.append(q26)

    T27 = [[-0.267617, 0.267617, -0.925615, -0.735], [-0.707107, -0.707107, -4.44089e-16, -0.465], [-0.654508, 0.654508, 0.378467, 0.125], [0, 0, 0, 1]]
    q27 = [-2.96131,    -0.089453,    2,    0.50305,    -1.45226,    1.12043,    0.449692]
    T.append(T27)
    q.append(q27)

    T28 = [[-0.0890985, 0.0890985, -0.99203, -0.735], [-0.707107, -0.707107, -6.66134e-16, -0.465], [-0.701471, 0.701471, 0.126004, 0.125], [0, 0, 0, 1]]
    q28 = [-2.96131,    -0.089453,    2,    0.50305,    -1.35306,    1.28058,    0.599301]
    T.append(T28)
    q.append(q28)

    T29 = [[0.0890985, -0.0890985, -0.99203, -0.735], [-0.707107, -0.707107, 6.66134e-16, -0.465], [-0.701471, 0.701471, -0.126004, 0.125], [0, 0, 0, 1]]
    q29 = [-2.96131,    -0.089453,    2,    0.50305,    -1.23869,    1.41989,    0.75334]
    T.append(T29)
    q.append(q29)

    T30 = [[0.267617, -0.267617, -0.925615, -0.735], [-0.707107, -0.707107, 4.44089e-16, -0.465], [-0.654508, 0.654508, -0.378467, 0.125], [0, 0, 0, 1]]
    q30 = [-2.96131,    -0.089453,    2,    0.50305,    -1.10058,    1.54347,    0.926655]
    T.append(T30)
    q.append(q30)

    T31 = [[0.447822, -0.447822, -0.773893, -0.735], [-0.707107, -0.707107, 8.32667e-16, -0.465], [-0.547225, 0.547225, -0.633316, 0.125], [0, 0, 0, 1]]
    q31 = [-2.96131,    -0.089453,    2,    0.50305,    -0.91997,    1.65109,    1.14274]
    T.append(T31)
    q.append(q31)

    T32 = [[0.661438, -0.661438, -0.353553, -0.735], [-0.707107, -0.707107, 2.77556e-17, -0.465], [-0.25, 0.25, -0.935414, 0.125], [0, 0, 0, 1]]
    q32 = [-2.96131,    -0.089453,    2,    0.50305,    -0.558079,    1.73186,    1.56131]
    T.append(T32)
    q.append(q32)

    T33 = [[-0.935414, 0, -0.353553, -0.735], [-0, -1, 0, -0.465], [-0.353553, 0, 0.935414, 0.125], [0, 0, 0, 1]]
    q33 = [-2.96131,    -0.089453,    2,    0.50305,    -2.7167,    0.908809,    0.834637]
    T.append(T33)
    q.append(q33)

    T34 = [[-0.633316, 0, -0.773893, -0.735], [-0, -1, 0, -0.465], [-0.773893, 0, 0.633316, 0.125], [0, 0, 0, 1]]
    q34 = [-2.96131,    -0.089453,    2,    0.50305,    -2.32198,    1.29997,    0.651818]
    T.append(T34)
    q.append(q34)

    T35 = [[-0.378467, 0, -0.925615, -0.735], [-0, -1, 0, -0.465], [-0.925615, 0, 0.378467, 0.125], [0, 0, 0, 1]]
    q35 = [-2.96131,    -0.089453,    2,    0.50305,    -2.14301,    1.53971,    0.624639]
    T.append(T35)
    q.append(q35)

    T36 = [[-0.126004, 0, -0.99203, -0.735], [-0, -1, 0, -0.465], [-0.99203, 0, 0.126004, 0.125], [0, 0, 0, 1]]
    q36 = [-2.96131,    -0.089453,    2,    0.50305,    -1.98853,    1.75161,    0.636281]
    T.append(T36)
    q.append(q36)

    T37 = [[0.126004, 0, -0.99203, -0.735], [-0, -1, 0, -0.465], [-0.99203, 0, -0.126004, 0.125], [0, 0, 0, 1]]
    q37 = [-2.96131,    -0.089453,    2,    0.50305,    -1.82781,    1.95187,    0.681157] 
    T.append(T37)
    q.append(q37)

    T38 = [[0.378467, 0, -0.925615, -0.735], [-0, -1, 0, -0.465], [-0.925615, 0, -0.378467, 0.125], [0, 0, 0, 1]]
    q38 = [-2.96131,    -0.089453,    2,    0.50305,    -1.63204,    2.14824,    0.772093]
    T.append(T38)
    q.append(q38)

    T39 = [[0.633316, 0, -0.773893, -0.735], [-0, -1, 0, -0.465], [-0.773893, 0, -0.633316, 0.125], [0, 0, 0, 1]]
    q39 = [-2.96131,    -0.089453,    2,    0.50305,    -1.34228,    2.34332,    0.954803]
    T.append(T39)
    q.append(q39)

    T40 = [[0.935414, 0, -0.353553, -0.735], [-0, -1, 0, -0.465], [-0.353553, 0, -0.935414, 0.125], [0, 0, 0, 1]]
    q40 = [-2.96131,    -0.089453,    2,    0.50305,    -0.569552,    2.51721,    1.55478]
    T.append(T40)
    q.append(q40)

    T41 = [[-0.661438, -0.661438, -0.353553, -0.735], [0.707107, -0.707107, 2.77556e-17, -0.465], [-0.25, -0.25, 0.935414, 0.125], [0, 0, 0, 1]]
    q41 = [-2.96131,    -0.089453,    2,    0.50305,    3.07165,    1.54947,    1.0125]
    T.append(T41)
    q.append(q41)

    T42 = [[-0.447822, -0.447822, -0.773893, -0.735], [0.707107, -0.707107, 8.32667e-16, -0.465], [-0.547225, -0.547225, 0.633316, 0.125], [0, 0, 0, 1]]
    q42 = [-2.96131,    -0.089453,    2,    0.50305,    -2.93681,    1.79687,    0.666474]
    T.append(T42)
    q.append(q42)

    T43 = [[-0.267617, -0.267617, -0.925615, -0.735], [0.707107, -0.707107, 4.44089e-16, -0.465], [-0.654508, -0.654508, 0.378467, 0.125], [0, 0, 0, 1]]
    q43 = [-2.96131,    -0.089453,    2,    0.50305,    -2.81596,    1.97289,    0.492716]
    T.append(T43)
    q.append(q43)

    T44 = [[-0.0890985, -0.0890985, -0.99203, -0.735], [0.707107, -0.707107, 6.66134e-16, -0.465], [-0.701471, -0.701471, 0.126004, 0.125], [0, 0, 0, 1]]
    q44 = [-2.96131,    -0.089453,    2,    0.50305,    -2.73081,    2.1418,    0.347043]
    T.append(T44)
    q.append(q44)

    T45 = [[0.0890985, 0.0890985, -0.99203, -0.735], [0.707107, -0.707107, -6.66134e-16, -0.465], [-0.701471, -0.701471, -0.126004, 0.125], [0, 0, 0, 1]]
    q45 = [-2.96131,    -0.089453,    2,    0.50305,    -2.66942,    2.31353,    0.20553]
    T.append(T45)
    q.append(q45)

    T46 = [[0.267617, 0.267617, -0.925615, -0.735], [0.707107, -0.707107, 6.66134e-16, -0.465], [-0.654508, -0.654508, -0.378467, 0.125], [0, 0, 0, 1]]
    q46 = [-2.96131,    -0.089453,    2,    0.50305,    -2.63501,    2.49695,    0.0454827]
    T.append(T46)
    q.append(q46)

    T47 = [[0.447822, 0.447822, -0.773893, -0.735], [0.707107, -0.707107, -8.32667e-16, -0.465], [-0.547225, -0.547225, -0.633316, 0.125], [0, 0, 0, 1]]
    q47 = [-2.96131,    -0.089453,    2,    0.50305,    -2.66477,    2.70653,    -0.19146]
    T.append(T47)
    q.append(q47)

    T48 = [[0.661438, 0.661438, -0.353553, -0.735], [0.707107, -0.707107, -2.77556e-17, -0.465], [-0.25, -0.25, -0.935414, 0.125], [0, 0, 0, 1]]
    q48 = [-2.96131,    -0.089453,    2,    0.50305,    2.64259,    2.98025,    -1.51249]
    T.append(T48)
    q.append(q48)

    T49 = [[0, -0.935414, -0.353553, -0.735], [1, 0, 0, -0.465], [0, -0.353553, 0.935414, 0.125], [0, 0, 0, 1]]
    q49 = [-2.96131,    -0.089453,    2,    0.50305,    2.59178,    2.19509,    0.859601]
    T.append(T49)
    q.append(q49)

    T50 = [[-2.22045e-16, -0.633316, -0.773893, -0.735], [1, -2.22045e-16, 0, -0.465], [0, -0.773893, 0.633316, 0.125], [0, 0, 0, 1]]
    q50 = [-2.96131,    -0.089453,    2,    0.50305,    2.59178,    2.19509,    0.336002]
    T.append(T50)
    q.append(q50)   

    T51 = [[-8.88178e-16, -0.378467, -0.925615, -0.735], [1, -8.88178e-16, 0, -0.465], [0, -0.925615, 0.378467, 0.125], [0, 0, 0, 1]]
    q51 = [-2.96131,    -0.089453,    2,    0.50305,    2.59178,    2.19509,    0.0383112]
    T.append(T51)
    q.append(q51)

    T52 = [[4.44089e-16, -0.126004, -0.99203, -0.735], [1, 4.44089e-16, 0, -0.465], [0, -0.99203, 0.126004, 0.125], [0, 0, 0, 1]]
    q52 = [-2.96131,    -0.089453,    2,    0.50305,    2.59178,    2.19509,    -0.223488]
    T.append(T52)
    q.append(q52)

    T53 = [[4.44089e-16, 0.126004, -0.99203, -0.735], [1, 4.44089e-16, 0, -0.465], [0, -0.99203, -0.126004, 0.125], [0, 0, 0, 1]]
    q53 = [-2.96131,    -0.089453,    2,    0.50305,    2.59178,    2.19509,    -0.476168]
    T.append(T53)
    q.append(q53)

    T54 = [[-8.88178e-16, 0.378467, -0.925615, -0.735], [1, -8.88178e-16, 0, -0.465], [0, -0.925615, -0.378467, 0.125], [0, 0, 0, 1]]
    q54 = [-2.96131,    -0.089453,    2,    0.50305,    2.59178,    2.19509,    -0.737968]
    T.append(T54)
    q.append(q54)

    T55 = [[-2.22045e-16, 0.633316, -0.773893, -0.735], [1, -2.22045e-16, 0, -0.465], [0, -0.773893, -0.633316, 0.125], [0, 0, 0, 1]]
    q55 = [-2.96131,    -0.089453,    2,    0.50305,    2.59178,    2.19509,    -1.03566]
    T.append(T55)
    q.append(q55)

    T56 = [[0, 0.935414, -0.353553, -0.735], [1, 0, 0, -0.465], [0, -0.353553, -0.935414, 0.125], [0, 0, 0, 1]]
    q56 = [-2.96131,    -0.089453,    2,    0.50305,    2.59178,    2.19509,    -1.55926]
    T.append(T56)
    q.append(q56)

    T57 = [[0.661438, -0.661438, -0.353553, -0.735], [0.707107, 0.707107, -2.77556e-17, -0.465], [0.25, -0.25, 0.935414, 0.125], [0, 0, 0, 1]]
    q57 = [-2.96131,    -0.089453,    2,    0.50305,    1.53499,    2.58294,    0.0402501]
    T.append(T57)
    q.append(q57)

    T58 = [[0.447822, -0.447822, -0.773893, -0.735], [0.707107, 0.707107, -8.32667e-16, -0.465], [0.547225, -0.547225, 0.633316, 0.125], [0, 0, 0, 1]]
    q58 = [-2.96131,    -0.089453,    2,    0.50305,    1.60107,    2.21741,    -0.284676]
    T.append(T58)
    q.append(q58)

    T59 = [[0.267617, -0.267617, -0.925615, -0.735],[0.707107, 0.707107, 2.22045e-16, -0.465], [0.654508, -0.654508, 0.378467, 0.125], [0, 0, 0, 1]]
    q59 = [-2.96131,    -0.089453,    2,    0.50305,    1.68933,    2.02116,    -0.449692]
    T.append(T59)
    q.append(q59)

    T60 = [[0.0890985, -0.0890985, -0.99203, -0.735], [0.707107, 0.707107, -6.66134e-16, -0.465], [0.701471, -0.701471, 0.126004, 0.125], [0, 0, 0, 1]]
    q60 = [-2.96131,    -0.089453,    2,    0.50305,    1.78853,    1.86102,    -0.599301]
    T.append(T60)
    q.append(q60)

    T61 = [[-0.0890985, 0.0890985, -0.99203, -0.735], [0.707107, 0.707107, 6.66134e-16, -0.465], [0.701471, -0.701471, -0.126004, 0.125], [0, 0, 0, 1]]
    q61 = [-2.96131,    -0.089453,    2,    0.50305,    1.9029,    1.7217,    -0.75334]
    T.append(T61)
    q.append(q61)

    T62 = [[-0.267617, 0.267617, -0.925615, -0.735], [0.707107, 0.707107, 4.44089e-16, -0.465], [0.654508, -0.654508, -0.378467, 0.125], [0, 0, 0, 1]]
    q62 = [-2.96131,    -0.089453,    2,    0.50305,    2.04101,    1.59812,    -0.926655]
    T.append(T62)
    q.append(q62)

    T63 = [[-0.447822, 0.447822, -0.773893, -0.735], [0.707107, 0.707107, 8.32667e-16, -0.465], [0.547225, -0.547225, -0.633316, 0.125], [0, 0, 0, 1]]
    q63 = [-2.96131,    -0.089453,    2,    0.50305,    2.22162,    1.49051,    -1.14274]
    T.append(T63)
    q.append(q63)

    T64 = [[-0.661438, 0.661438, -0.353553, -0.735], [0.707107, 0.707107, 2.77556e-17, -0.465], [0.25, -0.25, -0.935414, 0.125], [0, 0, 0, 1]]
    q64 = [-2.96131,    -0.089453,    2,    0.50305,    2.58351,    1.40973,    -1.56131]
    T.append(T64)
    q.append(q64)

    # print len(T)
    handles = []
    for t in T:
        handles.append(env.drawlinestrip(points = np.array(((0,0,0),(t[0][0],t[1][0],t[2][0]))), linewidth = 3.0, colors = np.array(((1,0,0),(1,0,0)))))
        handles.append(env.drawlinestrip(points = np.array(((0,0,0),(t[0][1],t[1][1],t[2][1]))), linewidth = 3.0, colors = np.array(((0,1,0),(0,1,0)))))
        handles.append(env.drawlinestrip(points = np.array(((0,0,0),(t[0][2],t[1][2],t[2][2]))), linewidth = 3.0, colors = np.array(((0,0,1),(0,0,1)))))

        # handles.append(env.drawlinestrip(points=np.array(((-1.25,-0.5,0),(-1.25,0.5,0),(-1.5,1,0))),
        #                            linewidth=3.0,
        #                            colors=np.array(((0,1,0),(0,0,1),(1,0,0)))))
        # handles.append(misc.DrawAxes(env,t,1))
    raw_input('finish')

