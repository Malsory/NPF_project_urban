import pandas as pd
import numpy as np
import sys

# Read dataset
df = pd.read_csv(r'C:\\Users\\Masloriy\\Desktop\\Data_urban\\dodo\\output_combined.csv')
# Prep the dataset
df = df.dropna()
df = df.drop(df.columns[df.columns.str.contains('Unnamed')], axis=1)
df['date'] = pd.to_datetime(df['date'])
df['date'] = df['date'].dt.dayofyear
df = df.drop(df.index[-1])

npf_df_NPF = df[df['day.type'] == 'NPF']
average_temp_NPF = np.mean(npf_df_NPF['temperature'])
average_P_NPF = np.mean(npf_df_NPF['pressure'])
average_RH_NPF = np.mean(npf_df_NPF['RH'])
average_SRAD_NPF = np.mean(npf_df_NPF['SRAD'])
average_SO2_NPF = np.mean(npf_df_NPF['so2'])
average_pm10 = np.mean(npf_df_NPF['pm10'])

npf_df_non_NPF = df[df['day.type'] == 'Non']
average_temp_non = np.mean(npf_df_non_NPF['temperature'])
average_P_non = np.mean(npf_df_non_NPF['pressure'])
average_RH_non = np.mean(npf_df_non_NPF['RH'])
average_SRAD_non = np.mean(npf_df_non_NPF['SRAD'])
average_SO2_non = np.mean(npf_df_non_NPF['so2'])
average_pm10_non = np.mean(npf_df_non_NPF['pm10'])

npf_df_undef = df[df['day.type'] == 'undefined']
average_temp_undef = np.mean(npf_df_undef['temperature'])
average_P_undef = np.mean(npf_df_undef['pressure'])
average_RH_undef = np.mean(npf_df_undef['RH'])
average_SRAD_undef = np.mean(npf_df_undef['SRAD'])
average_SO2_undef = np.mean(npf_df_undef['so2'])
average_pm10_undef = np.mean(npf_df_undef['pm10'])

# Redirect stdout to a file
with open(r'C:\\Users\\Masloriy\\Desktop\\Data_urban\\dodo\\statistics_results.txt', 'w') as file:
    sys.stdout = file
    print('Avg temperature during NPF days:', average_temp_NPF)
    print('Avg temperature during non-NPF days:', average_temp_non)
    print('Avg temperature during Undefined days:', average_temp_undef)
    print('-----------------------------------------------------------------------------------')
    print('Avg pressure during NPF days:', average_P_NPF)
    print('Avg pressure during non-NPF days:', average_P_non)
    print('Avg pressure during Undefined days:', average_P_undef)
    print('-----------------------------------------------------------------------------------')
    print('Avg RH during NPF days:', average_RH_NPF)
    print('Avg RH during non-NPF days:', average_RH_non)
    print('Avg RH during Undefined days:', average_RH_undef)
    print('-----------------------------------------------------------------------------------')
    print('Avg SRAD during NPF days:', average_SRAD_NPF)
    print('Avg SRAD during non-NPF days:', average_SRAD_non)
    print('Avg SRAD during Undefined days:', average_SRAD_undef)
    print('-----------------------------------------------------------------------------------')
    print('Avg SO2 during NPF days:', average_SO2_NPF)
    print('Avg SO2 during non-NPF days:', average_SO2_non)
    print('Avg SO2 during Undefined days:', average_SO2_undef)
    print('-----------------------------------------------------------------------------------')
    print('Avg pm10 during NPF days:', average_SO2_NPF)
    print('Avg pm10 during non-NPF days:', average_SO2_non)
    print('Avg pm10 during Undefined days:', average_SO2_undef)
    sys.stdout = sys.__stdout__
