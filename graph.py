from bokeh.plotting import figure, output_file, show
from bokeh.models import Legend
import pandas as pd
import numpy as np

# get data
data = pd.read_csv('static/trackdata.csv', encoding = "ISO-8859-1")
valence = np.array(data['valence'])
energy = np.array(data['energy'])
date_strings = np.array(data['date'])
dates = [pd.to_datetime(x, format="%Y.%m.%d") for x in date_strings]


window_size = 30
window = np.ones(window_size)/float(window_size)
val_avg = np.convolve(valence, window, 'same')
en_avg = np.convolve(energy, window, 'same')

# output to static HTML file
output_file("valence-test.html", title="valence")

# generate new plot with datetime axis
p = figure(width=800, height=350, x_axis_type="datetime", toolbar_location="right")

# renderers
# p.circle(dates, valence, size=4, color='darkgrey', alpha=0.2, legend="pts")
r0 = p.line(dates, val_avg, color="navy", legend="avg valence")
r1 = p.line(dates, en_avg, color="red",legend="avg energy")

# add labels and determine tick marks
p.title.text = "Valence and Energy Averages"
p.legend.location = "bottom_left"
p.grid.grid_line_alpha = 0
p.xaxis.axis_label = 'Date'
p.yaxis.axis_label = 'Score'
p.ygrid.band_fill_color = "darkblue"
p.ygrid.band_fill_alpha = 0.1
p.xaxis[0].ticker.desired_num_ticks=18
p.yaxis[0].ticker.desired_num_ticks=10

"""
# add legend outside of window
legend = Legend(items=[
	("avg valence", [r0]),
	("avg energy", [r1])
], location=(0,-75))

p.add_layout(legend, 'right')
"""
# show the results
show(p)