from operator import index
from sklearn.linear_model import LinearRegression
import pandas as pd
import openpyxl


def predpy(files):
    study_files = [i for i in files if not 'predict' in i]
    predict_file = [i for i in files if 'predict' in i]
    predict_file = predict_file[0]
    
    pred_df = pd.read_excel(predict_file)
    X_pred = pred_df[['PAX']]

    df = pd.DataFrame()
    for i in study_files:
        base_df = pd.read_excel(i)
        df = pd.concat([df, base_df])

    X = df[['PAX']]
    y = df['WGT']

    lr = LinearRegression()
    lr.fit(X, y)
    result = lr.predict(X_pred)
    pred_df['WGT'] = result
    pred_df['日付'] = pred_df['日付'].dt.strftime('%Y/%m/%d')

    result_path =  'download/' + predict_file[6:-5] + '_result.xlsx'
    pred_df.to_excel(result_path)

    workbook = openpyxl.load_workbook(result_path)
    worksheet = workbook.worksheets[0]
    worksheet.delete_cols(1)
    workbook.save(result_path)

    print(result_path)


if __name__ == '__main__':
    files = ['files/sample1.xlsx', 'files/predict.xlsx',]
    predpy(files)

