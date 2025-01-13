import csv
import config as cfg

dataset_code = 'all'
datasets = cfg.get_datasets(dataset_code)
root_dir = cfg.get_project_root()
cols = cfg.get_gbif_columns()
col_dtypes = cfg.get_gbif_columns_dtypes()

for dataset in datasets:
    archive_code = dataset
    print(archive_code)
    source_filename = 'occurrence.txt'
    file_path = str(root_dir) + '/source-data/' + archive_code

    source_file = str(file_path) + '/occurrence.txt'
    target_file = str(file_path) + '/occurrence.csv'

    def tsv_to_csv(tsv_file, csv_file):
        csv.field_size_limit(100000000)
        with open(tsv_file, 'r', newline='', encoding='utf-8') as tsvfile:
            tsvreader = csv.reader(tsvfile, delimiter='\t')

            with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerows(tsvreader)

    tsv_to_csv(source_file, target_file)
    print(archive_code + ' successfully converted')