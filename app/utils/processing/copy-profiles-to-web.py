import os
import shutil
import vars as pvars

# Copy dataset profiles to web directory

def copy(src, dest):
    for name in os.listdir(src):
        pathname = os.path.join(src, name)
        if os.path.isfile(pathname):
            if name.endswith('.html'):
                shutil.copy2(pathname, dest)
                print(pathname + ' copied')
        else:
            copy(pathname, dest)

copy(pvars.source_dir, pvars.target_dir)