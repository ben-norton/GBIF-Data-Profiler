
import globals as cfg

# Processing Scripts globals file

root_dir = cfg.get_project_root()

source_dir = str(root_dir) + '/app/profilers/output'
target_dir = str(root_dir) + '/web/app/static/components/dataset-profiles'
source_data_dir = str(root_dir) + '/source-data'
md_file = str(root_dir) + '/web/app/md/dataset-profiles-table.md'
source_datasets_ymlfile = str(root_dir) + '/web/app/md/source-datasets.yaml'
web_source_csv = str(root_dir) + '/web/app/data/web_source.csv'