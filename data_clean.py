import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
def excel_to_df(file_path):
    df = pd.read_excel(file_path)

    return df
    print_df(df)

def remove_invalid_blank(df):
    df = df.dropna(how='any',axis=0)
    return df

def time_by_machine(df): #calculates time that machine was running per job/part id. most helpful in comparing against estimated total time for part.
    time_by_machine_data = df.groupby(['MACHINE','JOB ID','PART ID']).agg({'TOTAL TIME': 'sum'}).reset_index()

    return time_by_machine_data

def time_by_machinist(df): #calculates total time spent on a part per machinist across all operations. 
    #explode the rows
    #time_by_machine_data = df.groupby(['MACHINE','JOB ID','PART ID']).agg({'TOTAL TIME': 'sum'}).reset_index()
    df['OPERATOR'] = df['OPERATOR'].str.split('\n')
    df = df.explode('OPERATOR')
    time_by_machinist = df.groupby(['OPERATOR','MACHINE','JOB ID','PART ID']).agg({'TOTAL TIME': 'sum'}).reset_index()
    return time_by_machinist

def time_by_week():
    # calculates how much time each of the machines were running per week.most helpful for figuring out theoretical max capacity time running versus actual time running.
    pass

def average_quantity(): #finds out average quantity/day per operation. most helpful for figuring out actual quantity/day versus estimate. 
    pass


#may or may not want indexer to index by week, by month, etc. Default is all data.
#may want a dropdown for easy gui for non-tech people.
#may want option to select stats for specific job, specific job/part id, or all(default)

def clean_data(inputs):
    data = excel_to_df(inputs[0])
    data = remove_invalid_blank(data)
    
    cleaned_data = pd.DataFrame(index=data.index)
    print(time_by_machinist(data))

    #print(grouped_data)

def print_df(df):
    print(df)

