import chartify
import pandas as pd
import numpy as np


data = pd.read_csv('static/trackdata.csv', encoding = "ISO-8859-1")
date_strings = np.array(data['date'])
dates = [pd.to_datetime(x, format="%Y.%m.%d") for x in date_strings]

# valence vs energy scatterplot
d = {'valence': data['valence'], 'energy': data['energy']}
df = pd.DataFrame(d)
ch = chartify.Chart(blank_labels=False, x_axis_type='linear')
ch.plot.scatter(
    data_frame=df,
    x_column='valence',
    y_column='energy')
ch.set_title("Valence and Energy")
ch.set_subtitle("includes all songs from 'lately'")
ch.axes.set_xaxis_label('valence')
ch.axes.set_yaxis_label('energy')
ch.set_source_label("lately 2016-2018")
ch.show()