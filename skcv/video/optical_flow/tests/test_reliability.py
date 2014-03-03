import numpy as np
from numpy.testing import assert_equal, assert_almost_equal
from skcv.video.optical_flow.reliability import *


def test_forward_backward_reliability():
    N = 99
    M = 99

    fflow = np.zeros((N, M, 2))
    bflow = np.zeros((N, M, 2))

    fflow[N / 3:2 * N / 3, M / 3:2 * M / 3, 0] = 1
    fflow[N / 3:2 * N / 3, M / 3:2 * M / 3, 1] = 1

    bflow[1 + N / 3:2 * N / 3, 1 + M / 3:2 * M / 3, 0] = -1
    bflow[1 + N / 3:2 * N / 3, 1 + M / 3:2 * M / 3, 1] = -1

    frel = occlusion_reliability(fflow, bflow)
    brel = occlusion_reliability(bflow, fflow)

    low_rel = (np.array([33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
                         50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 65,
                         65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65,
                         65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65]),
               np.array([65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65,
                         65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 33, 34,
                         35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
                         52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65]))

    assert_equal(np.where(frel < 1), low_rel)

    low_rel = (np.array([33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33,
                         33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 34,
                         35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
                         52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65]),
               np.array([33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
                         50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 33,
                         33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33,
                         33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33]))

    assert_equal(np.where(brel < 1), low_rel)


def test_variation_reliability():
    N = 99
    M = 99

    fflow = np.zeros((N, M, 2))

    fflow[N / 3:2 * N / 3, M / 3:2 * M / 3, 0] = 1
    fflow[N / 3:2 * N / 3, M / 3:2 * M / 3, 1] = 1

    rel = variation_reliability(fflow)

    low_rel = (np.array([33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33,
                         33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 34,
                         34, 35, 35, 36, 36, 37, 37, 38, 38, 39, 39, 40, 40, 41, 41, 42, 42,
                         43, 43, 44, 44, 45, 45, 46, 46, 47, 47, 48, 48, 49, 49, 50, 50, 51,
                         51, 52, 52, 53, 53, 54, 54, 55, 55, 56, 56, 57, 57, 58, 58, 59, 59,
                         60, 60, 61, 61, 62, 62, 63, 63, 64, 64, 65, 65, 65, 65, 65, 65, 65,
                         65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65,
                         65, 65, 65, 65, 65, 65, 65, 65, 65]),
               np.array([33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
                         50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 33,
                         65, 33, 65, 33, 65, 33, 65, 33, 65, 33, 65, 33, 65, 33, 65, 33, 65,
                         33, 65, 33, 65, 33, 65, 33, 65, 33, 65, 33, 65, 33, 65, 33, 65, 33,
                         65, 33, 65, 33, 65, 33, 65, 33, 65, 33, 65, 33, 65, 33, 65, 33, 65,
                         33, 65, 33, 65, 33, 65, 33, 65, 33, 65, 33, 34, 35, 36, 37, 38, 39,
                         40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
                         57, 58, 59, 60, 61, 62, 63, 64, 65]))

    assert_equal(np.where(rel < 1), low_rel)


def test_structure_reliability():
    N = 100
    M = 100

    img = np.zeros((N, M, 3))

    img[N / 2, M / 2, :] = [100, 100, 100]

    rel = structure_reliability(img)

    assert_almost_equal(np.max(rel), 1)
    assert_equal(np.argmax(rel), 4848)


def test_reliability():
    N = 9
    M = 9

    img = np.zeros((N, M, 3))

    fflow = np.zeros((N, M, 2))
    bflow = np.zeros((N, M, 2))

    fflow[N / 3:2 * N / 3, M / 3:2 * M / 3, 0] = 1
    fflow[N / 3:2 * N / 3, M / 3:2 * M / 3, 1] = 1

    bflow[1 + N / 3:2 * N / 3, 1 + M / 3:2 * M / 3, 0] = -1
    bflow[1 + N / 3:2 * N / 3, 1 + M / 3:2 * M / 3, 1] = -1

    img[N / 3:2 * N / 3, M / 3:2 * M / 3, :] = 100

    rel = flow_reliability(img, forward_flow=fflow, backward_flow=bflow,
                           use_structure=True)

    expected_rel = np.array([[3.18997461e-03, 2.27885585e-02, 5.77428933e-02,
                              6.76206854e-02, 5.99810903e-02, 6.76206854e-02,
                              5.77428933e-02, 2.27885585e-02, 3.18997461e-03],
                             [2.27885585e-02, 1.83698319e-01, 4.55458765e-01,
                              5.45682429e-01, 5.21522853e-01, 5.45682429e-01,
                              4.55458765e-01, 1.83698319e-01, 2.27885585e-02],
                             [5.77428933e-02, 4.55458765e-01, 8.82046385e-01,
                              9.59261552e-01, 9.61780019e-01, 9.59261552e-01,
                              8.82046385e-01, 4.55458765e-01, 5.77428933e-02],
                             [6.76206854e-02, 5.45682429e-01, 9.59261552e-01,
                              1.81694479e-20, 1.34794095e-10, 1.81694479e-20,
                              9.59261552e-01, 5.45682429e-01, 6.76206854e-02],
                             [5.99810903e-02, 5.21522853e-01, 9.61780019e-01,
                              1.34794095e-10, 9.98152559e-01, 1.34794095e-10,
                              9.61780019e-01, 5.21522853e-01, 5.99810903e-02],
                             [6.76206854e-02, 5.45682429e-01, 9.59261552e-01,
                              1.81694479e-20, 1.34794095e-10, 1.81694479e-20,
                              9.59261552e-01, 5.45682429e-01, 6.76206854e-02],
                             [5.77428933e-02, 4.55458765e-01, 8.82046385e-01,
                              9.59261552e-01, 9.61780019e-01, 9.59261552e-01,
                              8.82046385e-01, 4.55458765e-01, 5.77428933e-02],
                             [2.27885585e-02, 1.83698319e-01, 4.55458765e-01,
                              5.45682429e-01, 5.21522853e-01, 5.45682429e-01,
                              4.55458765e-01, 1.83698319e-01, 2.27885585e-02],
                             [3.18997461e-03, 2.27885585e-02, 5.77428933e-02,
                              6.76206854e-02, 5.99810903e-02, 6.76206854e-02,
                              5.77428933e-02, 2.27885585e-02, 3.18997461e-03]])

    assert_almost_equal(rel, expected_rel)

    rel = flow_reliability(img, forward_flow=fflow, backward_flow=bflow,
                           use_structure=False)

    low_rel = (np.array([3, 3, 3, 4, 4, 5, 5, 5]),
               np.array([3, 4, 5, 3, 5, 3, 4, 5]))

    assert_equal(np.where(rel < 1), low_rel)