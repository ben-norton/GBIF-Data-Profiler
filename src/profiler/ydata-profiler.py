from ydata_profiling import ProfileReport
import pandas as pd
from datetime import date
from pathlib import Path
import os
import config as cfg


root_dir = cfg.get_project_root()
archive_code = '0049395-241126133413365'
source_filename = 'occurrence.txt'

today = date.today()
ts = today.strftime("%Y%m%d")

# Paths
current_path = Path().absolute()
source_path = current_path.parent.parent

# Load file (CSV should be automatically identified)
source_file = str(source_path) + '/source-data/' + archive_code + '/' + source_filename
target_path = str(current_path) + '/output/' + str(ts)

if not os.path.isdir(target_path):
    os.mkdir(target_path)

target_report = str(target_path) + '/' + archive_code + '-output.html'

df = pd.read_csv(source_file, sep='\t', lineterminator='\n', on_bad_lines='skip')
profile = ProfileReport(df, minimal=True)
profile.to_file(target_report)