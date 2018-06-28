# MPE CDT Machine Learning Project w/ Met Office 
A small project for experimenting with machine learning for interpolating
weather data.

Essentially, can we make fewer observations and run coarser simulations,
and use machine learning to interpolate between them?

Makes for a nice introduction to machine learning. See the code below for
expected usage of much of this - it's simple enough that we didn't take
the time to write intricate docstrings!

The overall results seem to be that super-basic linear interpolation is
actually working better than any of the (compeletely arbitrarily chosen)
machine learning algorithms. This is likely because the data is already
at a very coarse resolution, so it is already pretty smooth - there is
little to be gained by trying to do something clever! Ideally we'd be
using smaller-scaler data. Not to mention the fact that we really need
more data and time to actually apply them.
