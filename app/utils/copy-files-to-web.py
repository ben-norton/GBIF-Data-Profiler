import os
import re
import datetime
import shutil
import globals as cfg
import pathlib
import pandas as pd

root_dir = cfg.get_project_root()

source_dir = str(root_dir) + '/app/profilers/output'
target_dir = str(root_dir) + '/web/docs/public/dataset-profiles'
source_data_dir = str(root_dir) + '/source-data'
md_file = str(root_dir) + '/web/docs/includes/dataset-profiles-table.md'

# Copy Files
def copy(src, dest):
    for name in os.listdir(src):
        pathname = os.path.join(src, name)
        if os.path.isfile(pathname):
            if name.endswith('.html'):
                shutil.copy2(pathname, dest)
                print(pathname + ' copied')
        else:
            copy(pathname, dest)

#copy(source_dir, target_dir)


# Generate Table
def generate_table(target):
    master_list = list()
    for name in os.listdir(target):
        pathname = os.path.join(target, name)
        data_dict = {}
        if os.path.isfile(pathname):
            path = pathlib.Path(pathname)
            mtime = path.stat().st_mtime
            last_modified = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M')
            if name.endswith('.html'):
                data_dict['profile_file'] = '[' + name + '](/dataset-profiles/' + name + '){target="_self"}'
                data_dict['last_modified'] = last_modified
                data_dict['package_id'] = re.search(r"\d{7}-\d{15}", name).group()
                # Split filename by hyphen and remove extension
                name_split = path.stem.split("-")
                # Get Institution Code and add to Dict
                data_dict['source_file'] = name_split[3] + '.txt'
                data_dict['institution_code'] = name_split[4]
                # Get Profiler Library and add to Dict
                profiler_notation = name_split[5]
                if (profiler_notation == 'yd'):
                    profiler = 'YData'
                elif (profiler_notation == 'sv'):
                    profiler = 'Sweetviz'
                else:
                    profiler = 'Unknown'
                data_dict['profile_library'] = profiler
                master_list.append(data_dict)
    df = pd.DataFrame.from_dict(master_list)
    md_table = df.to_markdown(index=False)
    with open(md_file, 'w') as f:
        f.write(md_table)

generate_table(target_dir)


