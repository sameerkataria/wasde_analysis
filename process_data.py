import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

def config(commodity):
    x = commodity
    condn = [x=='Corn',
             x=='Soybeans',
             x=='Hard Red Winter']
    choice = ['Corn',
              'Soybeans',
              'Wheat']
    code = np.select(condn, choice, 42)
    return str(code)
    

def commodity_data(commodity):
    df = pd.read_csv('data2.csv')
    comm_data = df[df['commodity'].str.contains(commodity)]
    comm_data_us = comm_data[comm_data['code'].str.contains(str.upper(config(commodity))+str('_US'))]
    comm_data_us = comm_data_us[comm_data_us['period']!='Annual']
    comm_data_us['Year'], comm_data_us['Month']  = zip(*comm_data_us['report_month'].apply(lambda x: x.split("-")))
    comm_data_us['Year'] = comm_data_us['Year'].astype('int')
    comm_data_us['Month'] = comm_data_us['Month'].astype('int')
    comm_data_us['period_true'] =comm_data_us['period'].apply(lambda x: datetime.strptime(x, '%b').month)
    sample_dat = comm_data_us[comm_data_us['period_true'] == comm_data_us['Month']]
    sample_dat = sample_dat[sample_dat['report_month'] !='2010-08']
    sample_dat['report_month'] = pd.to_datetime(sample_dat['report_month'], format='%Y-%m')
    sample_dat['YearMonth'] = sample_dat['report_month'].dt.strftime('%Y-%m')
    sample_dat = sample_dat.sort_values(['report_month'])
    return sample_dat

def get_area_planted(df):
    df = df[df['item']=='Area Planted']
    cols = ['report_month','value']
    df = df[cols]
    return df

def get_area_harvested(df):
    df = df[df['item']=='Area Harvested']
    cols = ['report_month','value']
    df = df[cols]
    return df

def get_beigning_stocks(df):
    df = df[df['item']=='Beginning Stocks']
    cols = ['report_month','value']
    df = df[cols]
    return df

def get_ending_stocks(df):
    df = df[df['item']=='Ending Stocks']
    cols = ['report_month','value']
    df = df[cols]
    return df

def get_imports(df):
    df = df[df['item']=='Imports']
    cols = ['report_month','value']
    df = df[cols]
    return df

def get_exports(df):
    df = df[df['item']=='Exports']
    cols = ['report_month','value']
    df = df[cols]
    return df

def get_yeild(df):
    df = df[df['item']=='Yield per Harvested Acre']
    cols = ['report_month','value']
    df = df[cols]
    return df
