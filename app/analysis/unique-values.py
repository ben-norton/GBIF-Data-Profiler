import pandas as pd
import globals as cfg
from datetime import date


today = date.today()
ts = today.strftime("%Y%m%d")

datasets = cfg.get_test_datasets()

for dataset in datasets:
    archive_code = dataset
    print(archive_code)
    root_dir = cfg.get_project_root()
    source_file = str(root_dir) + '/source-data/' + archive_code + '/occurrence.txt'
#    target_path = str(root_dir) + '/app/analysis/output/unique-values/' + str(ts)
#    if not os.path.isdir(target_path):
#        os.mkdir(target_path)

    '''
    unique_counts_file = str(target_path) + '/' + archive_code + '-unique.xlsx'
    writer = pd.ExcelWriter(unique_counts_file)
    wb = Workbook()
    # Create Contents Sheet
    ws0 = wb.create_sheet('Contents')
    worksheet = wb['Contents']
    worksheet['A1'] = "Unique Value Sets"
    worksheet['A2'] = "Each worksheet contains the unique values for a given column"
    worksheet[
        'A3'] = "Columns with text datatypes and schema identifiers are omitted from the results. Omitted: " + omits
    worksheet['A4'] = "Created On: "
    worksheet['B4'] = today
    currentCell = worksheet['B4']
    currentCell.alignment = Alignment(horizontal='left')
    worksheet["A6"] = "Source Dataset: "
    worksheet['B7'] = archive_code
    worksheet['A9'] = "Columns"
    '''
    # Load Source Dataset
    df = pd.read_csv(source_file, sep='\t', lineterminator='\n', encoding='utf-8', low_memory=False)

    # Iterate over columns
    # for series_name, series in df.items():
    for col in df.columns[1:50]:
#        ws = wb.create_sheet(col)
        col_idx = df.columns.get_loc(col)
        # Get first 5 unique values then convert to list
        unique_list = df[col].dropna().unique()[:5].tolist()
        # Print meta if more than one unique value
        if(len(unique_list) > 0):
            print(df[col].dtype)
            print(col)
            print(col_idx)
            print(unique_list)
#        unique_values = df[col].unique()
#            for val in unique_list:
#                print(val)
#            ws.append([val])

