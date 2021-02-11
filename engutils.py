import pandas as pd
from scipy import interpolate  
import numpy as np

def sig_return(num, n_sigs):
    return float(f'{num:.{n_sigs}f}')

def sig_print(num, n_sigs):
    print(f'{num:.{n_sigs}f}')

def lin_interp(x, x1, y1, x2, y2):
    return ((x - x1) * (y2 - y1)) / (x2 - x1) + y1

def gas_interp(given, val):
    gas_table = pd.read_csv('data/gas_table.csv')
    
    mach_series = np.array(gas_table['Ma'][:]).astype('float')
    pres_series = np.array(gas_table['P/P_0'][:]).astype('float')
    temp_series = np.array(gas_table['T/T_0'][:]).astype('float')
    area_series = np.array(gas_table['A/A*'][:]).astype('float')

    if given == 'M':
        mach = val

        pres = interpolate.interp1d(mach_series, pres_series)(val)
        temp = interpolate.interp1d(mach_series, temp_series)(val)
        area = interpolate.interp1d(mach_series, area_series)(val) 

    elif given == 'P':
        pres = val
        
        mach = interpolate.interp1d(pres_series, mach_series)(val)
        temp = interpolate.interp1d(pres_series, temp_series)(val)
        area = interpolate.interp1d(pres_series, area_series)(val)

    elif given == 'T':
        temp = val

        mach = interpolate.interp1d(temp_series, mach_series)(val)
        pres = interpolate.interp1d(temp_series, pres_series)(val)
        area = interpolate.interp1d(temp_series, area_series)(val)

    elif given == 'A':
        area = val

        mach = interpolate.interp1d(area_series, mach_series)(val)
        pres = interpolate.interp1d(area_series, pres_series)(val)
        temp = interpolate.interp1d(area_series, temp_series)(val)


    print('Mach: {0} \nPressure Ratio: {1} \nTemperature Ratio: {2} \nArea Ratio: {3}'.format(mach, pres, temp, area))
