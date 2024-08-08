from tools import get_path,station_info,merge_dataFrame
import pandas as pd
if __name__ == '__main__':
    fileName_list = get_path()
    station_df = station_info()
    all_inout = merge_dataFrame(fileName_list,station_df)
    inout_info = pd.concat(all_inout)
    inout_info.to_csv('inout_info.csv')