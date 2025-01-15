import csv
import globals as cfg
import schemas as sch

dataset_code = 'all'
datasets = cfg.get_datasets(dataset_code)
root_dir = cfg.get_project_root()
cols = sch.get_gbif_columns()
col_dtypes = sch.get_gbif_columns_dtypes()

for dataset in datasets:
    archive_code = dataset
    print(archive_code)
    source_filename = 'verbatim.txt'
    file_path = str(root_dir) + '/source-data/' + archive_code

    source_file = str(file_path) + '/verbatim.txt'
    target_file = str(file_path) + '/verbatim.csv'

    def tsv_to_csv(tsv_file, csv_file):
        csv.field_size_limit(100000000)
        with open(tsv_file, 'r', newline='', encoding='utf-8') as tsvfile:
            tsvreader = csv.reader(tsvfile, delimiter='\t')

            with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerows(tsvreader)

    tsv_to_csv(source_file, target_file)
    print(archive_code + ' successfully converted')