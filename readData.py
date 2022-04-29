"""
Student number:20090444
Student name:Kaiyun Guo
"""
import numpy as np
import pandas as pd # read file, data processing

def readFile():
    df = pd.read_csv('corona_tests.english.csv')
    # above 60 ==

    df = df[~df['cough'].isin(["None"])]
    df = df[~df['fever'].isin(["None"])]
    df = df[~df['age_60_and_above'].isin(["None"])]
    df = df[~df['test_indication'].isin(["other"])]
    df = df[~df['corona_result'].isin(["other"])]
    # df['cough'] = (df['cough'] == 1).astype(int)
    # df['fever'] = (df['fever'] == 1).astype(int)
    df['age_60_and_above'] = (df['age_60_and_above'] == "Yes").astype(int)
    df['gender'] = (df['gender'] == "male").astype(int)
    df['test_indication'] = (df['test_indication'] == 'Contact with confirmed').astype(int)
    df['corona_result'] = (df['corona_result'] == "positive").astype(int)

    df.dropna()
    return df, len(df.columns)-1

def readFile1():
    df = pd.read_csv('archive/Cleaned-Data.csv')
    df = df.drop(['Country'], axis = 1)
    df = df[~df['Gender_Transgender'].isin([1])]
    df = df.drop(['Gender_Transgender'], axis = 1)
    df = df.drop(['Gender_Female'], axis = 1)
    df['Gender_Male'] = (df['Gender_Male'] == 1).astype(int)
    df = df[~df['Contact_Dont-Know'].isin([1])]
    df = df.drop(['Contact_Dont-Know'], axis = 1)
    df = df.drop(['Contact_No'], axis = 1)
    df['Contact_Yes'] = (df['Contact_Yes'] == 1).astype(int)
    df.dropna()
    print(df)
    entity = np.array(df)
    # use severity as classifacation indicator
    severity = []
    for i in range(len(df)):
        # 'Severity_Mild', 'Severity_Moderate', 'Severity_None', 'Severity_Severe'
        if entity[i,17] == 1:
            severity.append(0)
        if entity[i,18] == 1:
            severity.append(1)
        if entity[i,19] == 1:
            severity.append(0)
        if entity[i,20] == 1:
            severity.append(1)

    # remove redundant entities
    df = df.drop(['Severity_Mild'], axis=1)
    df = df.drop(['Severity_None'], axis=1)
    df = df.drop(['Severity_Moderate'], axis=1)
    df = df.drop(['Severity_Severe'], axis=1)

    # print(df.columns)
    # print(len(df.columns))
    df.insert(18, "severity", severity, True)
    return df, len(df.columns)


if __name__ == '__main__':
    a, b = readFile1()
    print(a)
    print(b)
    h = a.columns
    print(h)
    print(type(h), h[1])
