# Pandas provides built-in exponentially weighted moving window functions with the .ewm method.
# Consider using .ewm().mean(), and be sure to properly specify the alpha parameter
# (hint: it is related to, but not equal to λ).
#
# Note that .ewm().std() and .ewm().var() implement ewmvar(x) = ewma(x**2) - ewma(x)**2,
# which is slightly different than what you'll want to implement for this problem.

import pandas as pd
import numpy as np


def estimate_volatility(prices, l):
    """Create an exponential moving average model of the volatility of a stock
    price, and return the most recent (last) volatility estimate.

    Parameters
    ----------
    prices : pandas.Series
        A series of adjusted closing prices for a stock.

    l : float
        The 'lambda' parameter of the exponential moving average model. Making
        this value smaller will cause the model to weight older terms less 
        relative to more recent terms.

    Returns
    -------
    last_vol : float
        The last element of your exponential moving averge volatility model series.
    """

    # calculate log returns
    log_returns = np.log(prices) - np.log(prices.shift(1))

    # see ewm.png for alternative formula to calculate EWMA from log returns by using alpha
    alpha = 1 - l
    volatility = np.sqrt((log_returns**2).ewm(alpha=alpha, adjust=True).mean())

    # The exponential moving average model of volatility tracks changes in the volatility. The lambda parameter determines how responsive the estimate of the daily volatility is to the most recent daily return.
    return volatility.iloc[-1]


def test_run(filename='data.csv'):
    """Test run get_most_volatile() with stock prices from a file."""
    prices = pd.read_csv(filename, parse_dates=[
                         'date'], index_col='date', squeeze=True)
    print("Most recent volatility estimate: {:.6f}".format(
        estimate_volatility(prices, 0.7)))


if __name__ == '__main__':
    test_run()
