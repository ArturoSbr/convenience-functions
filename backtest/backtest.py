# Imports
import numpy as np


# Function that calculates goods and bads per threshold
def backtest(y_true, proba, thr, ascending_proba=True):

    # Cast to np array
    thr_array = np.asarray(thr)

    # Declare masks
    if ascending_proba:
        acc_m = proba[:, None] < thr
    else:
        acc_m = proba[:, None] > thr
    rej_m = ~acc_m

    # Accepted population
    acc_n = acc_m.sum(axis=0)
    acc_n1 = (y_true[:, None] * acc_m).sum(axis=0)
    acc_n0 = acc_n - acc_n1
    acc_r1 = acc_n1 / acc_n
    acc_r0 = acc_n0 / acc_n

    # Rejected population
    rej_n = rej_m.sum(axis=0)
    rej_n1 = (y_true[:, None] * rej_m).sum(axis=0)
    rej_n0 = rej_n - rej_n1
    rej_r1 = rej_n1 / rej_n
    rej_r0 = rej_n0 / rej_n

    # Return metrics
    return {
        'thr': thr,
        'acc_n': acc_n,
        'acc_n0': acc_n0,
        'acc_n1': acc_n1,
        'acc_rate0': acc_r0,
        'acc_rate1': acc_r1,
        'rej_n': rej_n,
        'rej_n0': rej_n0,
        'rej_n1': rej_n1,
        'rej_rate0': rej_r0,
        'rej_rate1': rej_r1
    }
    