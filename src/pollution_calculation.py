import numpy as np
import pandas as pd
import os

from utils import *

K = 0.2

pollution_data_location = 'data/raw/WaterQuality/'
water_flow_data_path = 'data/raw/WaterFlow.csv'
water_speed_data_path = 'data/raw/WaterSpeed.csv'
location_distance_data_path = 'data/raw/LocationDistance.csv'

pollution_file_paths = get_file_paths(pollution_data_location)

water_flow = pd.read_csv(water_flow_data_path)
water_speed = pd.read_csv(water_speed_data_path)
location_distance = pd.read_csv(location_distance_data_path)
location_distance = location_distance.iloc[1][1:].astype(float).to_list()
locations = water_flow.columns.to_list()[1:]
years = water_flow['观测时间']

columns = ['观测时间'] + locations
CODMn_result = pd.DataFrame(columns=columns)
CODMn_result['观测时间'] = years
NH3N_result = pd.DataFrame(columns=columns)
NH3N_result['观测时间'] = years

for i, pollution_file_path in enumerate(pollution_file_paths[10: -5]):
    water_speed_yearly = water_speed.iloc[i][1:].astype(float).to_list()
    water_flow_yearly = water_flow.iloc[i][1:].astype(float).to_list()
    df = pd.read_csv(pollution_file_path)
    CODMns = df['CODMn'].to_list()[:7]
    NH3Ns = df['NH3-N'].to_list()[:7]
    pre_CODMn = 0
    pre_NH3N = 0
    for j, location in enumerate(locations):
        if j == 0:
            pre_CODMn = calculate_pollution_flow(0, CODMns[0], water_flow_yearly[j], 0)
            CODMn_result.at[i, location] = pre_CODMn
            pre_NH3N = calculate_pollution_flow(0, NH3Ns[0], water_flow_yearly[j], 0)
            NH3N_result.at[i, location] = pre_NH3N
            continue
        alpha = get_alpha(location_distance[j], 
                          water_speed=mean(water_speed_yearly[j-1], water_speed_yearly[j]))
        pre_CODMn = calculate_pollution_flow(pre_CODMn, CODMns[j], water_flow_yearly[j], alpha)
        pre_NH3N = calculate_pollution_flow(pre_NH3N, NH3Ns[j], water_flow_yearly[j], alpha)
        CODMn_result.at[i, location] = pre_CODMn
        NH3N_result.at[i, location] = pre_NH3N

CODMn_result.to_csv('data/result/CODMnResult.csv', index=False)
NH3N_result.to_csv('data/result/NH3NResult.csv', index=False)
