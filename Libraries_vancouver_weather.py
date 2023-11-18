import pandas as pd
v2013_df1 = pd.read_csv(r"C:\Users\Tombra\Vancouver_Weather_Predictions\Vancouver_raw_data\en_climate_daily_BC_1108395_2013_P1D.csv")
v2014_df1 = pd.read_csv(r"C:\Users\Tombra\Vancouver_Weather_Predictions\Vancouver_raw_data\en_climate_daily_BC_1108395_2014_P1D.csv")
v2015_df1 = pd.read_csv(r"C:\Users\Tombra\Vancouver_Weather_Predictions\Vancouver_raw_data\en_climate_daily_BC_1108395_2015_P1D.csv")
v2016_df1 = pd.read_csv(r"C:\Users\Tombra\Vancouver_Weather_Predictions\Vancouver_raw_data\en_climate_daily_BC_1108395_2016_P1D.csv")
v2017_df1 = pd.read_csv(r"C:\Users\Tombra\Vancouver_Weather_Predictions\Vancouver_raw_data\en_climate_daily_BC_1108395_2017_P1D.csv")
v2018_df1 = pd.read_csv(r"C:\Users\Tombra\Vancouver_Weather_Predictions\Vancouver_raw_data\en_climate_daily_BC_1108395_2018_P1D.csv")
v2019_df1 = pd.read_csv(r"C:\Users\Tombra\Vancouver_Weather_Predictions\Vancouver_raw_data\en_climate_daily_BC_1108395_2019_P1D.csv")
v2020_df1 = pd.read_csv(r"C:\Users\Tombra\Vancouver_Weather_Predictions\Vancouver_raw_data\en_climate_daily_BC_1108395_2020_P1D.csv")
v2021_df1 = pd.read_csv(r"C:\Users\Tombra\Vancouver_Weather_Predictions\Vancouver_raw_data\en_climate_daily_BC_1108395_2021_P1D.csv")
v2022_df1 = pd.read_csv(r"C:\Users\Tombra\Vancouver_Weather_Predictions\Vancouver_raw_data\en_climate_daily_BC_1108395_2022_P1D.csv")

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
pio.templates.default = "plotly_white"
