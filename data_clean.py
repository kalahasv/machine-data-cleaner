import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import os
from datetime import datetime

def excel_to_df(file_path):
    df = pd.read_excel(file_path)
    return df

def remove_invalid_blank(df):
    df = df.dropna(how='any',axis=0)
    return df

def time_by_machine(df): 
    time_by_machine_data = df.groupby(['MACHINE','JOB ID','PART ID']).agg({'TOTAL TIME': 'sum'}).reset_index()

    return time_by_machine_data

def time_by_machinist(df): 

    df['OPERATOR'] = df['OPERATOR'].str.split('\n')
    df = df.explode('OPERATOR')
    time_by_machinist_df = df.groupby(['OPERATOR','MACHINE','JOB ID','PART ID']).agg({'TOTAL TIME': 'sum'}).reset_index()

    return time_by_machinist_df

def time_by_frame(tf): 
    

    match tf: 
        case 'W':
            dir_path = 'week_data'
            report_path = 'week_reports'
        case '_':
            print('Not implemented yet.')
            return

    for root, dirs, files in os.walk(dir_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            week_df = pd.read_csv(file_path)
            grouped = week_df.groupby(['MACHINE']).agg({'TOTAL TIME': 'sum'}).reset_index()
            grouped['UTILIZATION'] = (grouped['TOTAL TIME'] / 60)*100
            grouped['UTILIZATION'] = grouped['UTILIZATION'].apply('{:.2f}%'.format)

        
            file_name = '{}.txt'.format(filename.removesuffix('.csv'))
            full_path = os.path.join(report_path,file_name)
            grouped.to_csv(full_path, header=True, index=False, sep='\t', mode='a')
            

    

def average_quantity(): 
    pass

def time_per_part(df): 
    time_by_part_df = df.groupby(['JOB ID','PART ID']).agg({'TOTAL TIME': 'sum'}).reset_index()
    return time_by_part_df
    

#may want a dropdown for easy gui for non-tech people.
#may want option to select stats for specific job, specific job/part id, or all(default)

def find_week(timestamp):
    time = pd.to_datetime(timestamp)
    week = time.isocalendar()[1]
    return week

def index_by_week(df):
    df['WEEK_NUM'] = df['START DATE'].apply(find_week)
    df_by_week = df.groupby('WEEK_NUM')

    for name, group in df_by_week:
         path = 'week_data'
         file_name = '{}.csv'.format(name)
         full_path = os.path.join(path,file_name)
         group.to_csv(full_path)

    #print("Done")


def clean_data(inputs):
    data = excel_to_df(inputs[0])
    data = remove_invalid_blank(data)
    
    cleaned_data = pd.DataFrame(index=data.index)
    #print(time_by_machinist(data))
    #print(time_by_week(data))
    #print(grouped_data)
    #print(time_per_part(data))
    index_by_week(data)
    time_by_frame('W')

def print_df(df):
    print(df)

