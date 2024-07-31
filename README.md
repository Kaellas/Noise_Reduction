This is a simple project for the Aarhus Uni High Frequency and Algorithmic Trading summer course.

First, using C#, I extract the EURUSD ticker data from the [cTrader](https://ctrader.com) platform. I do so in three frequencies - 1, 5 and 15 minutes - to make sure any discovered patterns are scale invariant.

Second, with Python, I do my best to eliminate microstructure noise and then run some basic analyses and visualisations on the data.
