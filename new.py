from bokeh.layouts import column
from bokeh.plotting import figure, show, output_file, curdoc
from bokeh.io import show
from bokeh.models import Dropdown, Select, Row, CustomJS, ColumnDataSource
import pandas as pd
p = figure(x_range=(1,12), y_range=(0,600), x_axis_label='month', y_axis_label='average respond time in h', title='311 service respond time in different zipcode')
data =pd.read_csv('/home/ubuntu/nycapp/result.csv',delimiter='\t').astype(str)
dorpdowna = Select(title='zipcode1',color ='green', options=sorted(data['zip'].unique()))
dorpdownb = Select(title='zipcode2',color ='yellow', options=sorted(data['zip'].unique()))
def get_val_byzip(zip):
    value = data[(data['zip'] == zip)]
    value = value['time'].tolist()
    return {'month':months, 'time':value}
months = ['1','2','3','4','5','6','7','8','9']
all = ['40','82.50769779044904','90','80.332227165835','105.494635','113.61785745791664','120','156','175']
pall = p.line(x=months, y=all, legend_label = 'All', color='black', line_width=2)
sourcedata1 = ColumnDataSource()
sourcedata2 = ColumnDataSource()
pz1 =p.line('month', 'time', source=sourcedata1, legend_label = 'zipcode1', color = 'red', line_width=2)
pz2 =p.line('month', 'time', source=sourcedata2, legend_label = 'zipcode2', color = 'pink', line_width=2)
def updatez1(attr,old,new):
    sourcedata1.data =get_val_byzip(new)
def updatez2(attr,old,new):
    sourcedata2.data =get_val_byzip(new)
dorpdowna.on_change('value',updatez1())
dorpdownb.on__change('value',updatez2())
curdoc().add_root(column(dorpdowna, dorpdownb, p))




