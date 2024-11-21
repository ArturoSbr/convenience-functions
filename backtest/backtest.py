"""Functions for backtesting models."""

# Imports
import numpy as np
from typing import Union, List


# Function that calculates goods and bads per threshold
def backtest(
    y_true: np.array,
    proba: np.array,
    thr: Union[List, np.array],
    ascending_proba: bool = True
):
    """Backtest the probabilities predicted by a model.

    This function splits the population into accepted and rejected groups for
    each threshold passed in `thr`. It calculates additional metrics such as
    the number and rate of goods and bads within each of the two groups.

    Parameters
    ----------
    y_true: np.array
        A numpy array of binary values (0 and 1), where 1 means that the i-th
        observation is bad.
    proba: np.array
        A numpy array of probabilities predicted by the model to be
        backtested. All probabilities in the array must be greater or equal to
        zero and less than or equal to one.
    thr: Union[List, np.array]
        A list or numpy array of thresholds to be used to split the population
        into accepted and rejected groups.
    ascending_proba: bool (default True)
        Set to True if higher probabilities indicate greater risk. Set to False
        if higher probabilities indicate less risk.

    Returns
    -------
    result: dict
        A dictionary containing numpy arrays with the following keys:
        - thr: The thresholds passed by the user.
        - acc_n: Number of accepted observations for each threshold.
        - acc_n0: Number of good observations in the accepted group.
        - acc_n1: Number of bad observations in the accepted group.
        - acc_rate0: Good rate in the accepted group.
        - acc_rate1: Bad rate in the accepted group.
        - rej_n: Number of rejected observations for each threshold.
        - rej_n0: Number of good observations in the rejected group.
        - rej_n1: Number of bad observations in the rejected group.
        - rej_rate0: Good rate in the rejected group.
        - rej_rate1: Bad rate in the rejected group.
    """
    # Cast to np array
    thr = np.asarray(thr)

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
