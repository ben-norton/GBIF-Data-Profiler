from PIL import Image
from pathlib import Path
import globals as cfg
import os

root_dir = cfg.get_project_root()
media_root_dir = cfg.get_media_directory()
package_id = '0000214-250121130708018'

media_dir = str(media_root_dir) + '/' + package_id + '_media'
images = Path(media_dir).glob('*.jpg')

def create_dir(package_id):
	target_dir = str(media_dir) + '/thumbnails'
	if not os.path.isdir(target_dir):
		os.mkdir(target_dir)
	return target_dir


target_path = create_dir(package_id)

for image in images:
	filename = Path(image).name
	with Image.open(filename) as im:
		width, height = im.size
		thumb_height = 450
		thumb_width = thumb_height * width / height


