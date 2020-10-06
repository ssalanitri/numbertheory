''' Create a simple stocks correlation dashboard.

Choose stocks to compare in the drop down widgets, and make selections
on the plots to update the summary and histograms accordingly.

.. note::
    Running this example requires downloading sample data. See
    the included `README`_ for more information.

Use the ``bokeh serve`` command to run the example by executing:

    bokeh serve stocks

at your command prompt. Then navigate to the URL

    http://localhost:5006/stocks

.. _README: https://github.com/bokeh/bokeh/blob/master/examples/app/stocks/README.md

'''
from functools import lru_cache
from os.path import dirname, join

import pandas as pd

from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, PreText, Select
from bokeh.plotting import figure
from sympy.ntheory import isprime

DATA_DIR = join(dirname(__file__), 'data')

PRIMES_DISTRIBUTIONS = ['PI', 'x/log', 'Li', 'R']

RANGE = 100

def nix(val, lst):
    return [x for x in lst if x != val]


@lru_cache()
def load_primes(aprox):
    listPrimes = get_primes_list()
    x = [i for i in range(RANGE)]
    data = pd.DataFrame({'x': x , 'a1' : listPrimes})
    data = data.set_index('x')
    return pd.DataFrame({aprox: data.a1, aprox+'_returns': data.a1.diff()})
    
    
@lru_cache()
def get_primes_list():
    
    x = []
    
    for i in range(RANGE):
        if(isprime(i)):
            x.append(i)
        else:
            x.append(0)
        
    return x
    
    
@lru_cache()
def get_data(a1, a2):
    df1 = load_primes(a1)
    df2 = load_primes(a2)
    data = pd.concat([df1, df2], axis=1)
    data = data.dropna()
    data['a1'] = data[a1]
    data['a2'] = data[a2]
    data['a1_returns'] = data[a1+'_returns']
    data['a2_returns'] = data[a2+'_returns']
    return data

# set up widgets

stats = PreText(text='', width=500)
aprox1 = Select(value='PI', options=nix('PI', PRIMES_DISTRIBUTIONS))
aprox2 = Select(value='x/log', options=nix('x/log', PRIMES_DISTRIBUTIONS))

# set up plots

source = ColumnDataSource(data=dict(x=[], a1=[], a2=[], a1_returns=[], a2_returns=[]))
source_static = ColumnDataSource(data=dict(x=[], a1=[], a2=[], a1_returns=[], a2_returns=[]))
tools = 'pan,wheel_zoom,xbox_select,reset'

corr = figure(plot_width=350, plot_height=350,
              tools='pan,wheel_zoom,box_select,reset')
corr.circle('a1', 'a2', size=2, source=source,
            selection_color="orange", alpha=0.6, nonselection_alpha=0.1, selection_alpha=0.4)

ts1 = figure(plot_width=900, plot_height=200, tools=tools, x_axis_type='log', active_drag="xbox_select")
ts1.line('x', 'a1', source=source_static)
ts1.circle('x', 'a1', size=1, source=source, color=None, selection_color="orange")

ts2 = figure(plot_width=900, plot_height=200, tools=tools, x_axis_type='log', active_drag="xbox_select")
ts2.x_range = ts1.x_range
ts2.line('x', 'a2', source=source_static)
ts2.circle('x', 'a2', size=1, source=source, color=None, selection_color="orange")

# set up callbacks

def aprox1_change(attrname, old, new):
    aprox1.options = nix(new, PRIMES_DISTRIBUTIONS)
    update()

def aprox2_change(attrname, old, new):
    aprox2.options = nix(new, PRIMES_DISTRIBUTIONS)
    update()

def update(selected=None):
    a1, a2 = aprox1.value, aprox2.value

    df = get_data(a1, a2)
    data = df[['a1', 'a2']]
    source.data = data
    source_static.data = data

    update_stats(df, a1, a2)

    corr.title.text = '%s returns vs. %s returns' % (a1, a2)
    ts1.title.text, ts2.title.text = a1, a2

def update_stats(data, a1, a2):
    stats.text = str(data[[a1, a2, a1+'_returns', a2+'_returns']].describe())

aprox1.on_change('value', aprox1_change)
aprox2.on_change('value', aprox2_change)

def selection_change(attrname, old, new):
    a1, a2 = aprox1.value, aprox2.value
    data = get_data(a1, a2)
    selected = source.selected.indices
    if selected:
        data = data.iloc[selected, :]
    update_stats(data, a1, a2)

source.selected.on_change('indices', selection_change)

# set up layout
widgets = column(aprox1, aprox2, stats)
main_row = row(corr, widgets)
series = column(ts1, ts2)
layout = column(main_row, series)

# initialize
update()

curdoc().add_root(layout)
curdoc().title = "Primes Distribution"
