# How tos

## How to Use the Data Profilers for a GBIF occurrence dataset
Created: 2025-01-21

1. Search and select a dataset to download using the GBIF dataset search portal: https://www.gbif.org/dataset/search. Its important to download the dataset as a package and not directly from the dataset page. See below for instructions.
2. Download the full Darwin Core Archive of the selected dataset. Datasets are placed in a queue for download. You should receive an email when the download is ready (assuming you created a GBIF account)
3. Place the zip archive under source-datasets/archives
4. Extract the archive to a folder named using the package_id (0000214-250121130708018). Move the folder to the source_data root directory. Make sure the files are located in the root of the package folder (not nested)
5. Copy the meta.yml file from project-docs/templates to the package folder. Enter the package information (all fields are required except for filter_paramter and filter_value). The requested information can be found in the xml file under the meta directory and the source landing page at gbif.org. (In the future this step will be automated, but currently requires manual entry.)
6. Edit the globals.py configuration file by creating a dictionary using the institution code, then add the package_id to the new dictionary. You'll specify the datasets in the script using the dictionary name.
7. Open the sweetviz or ydata profiler scripts (see below)
8. Edit the dataset_code to reflect the list you added the package_id to in step 8

## How To Download a Data Package
1. Go to https://www.gbif.org/dataset/search
2. Locate a dataset of interest, then click the link Example: https://www.gbif.org/dataset/99e6b736-3119-4081-9467-a9c8a4a7a01b
3. Click on the green occurrences button that shows the number of records in the dataset (do not download from this page). Example page: https://www.gbif.org/occurrence/search?dataset_key=99e6b736-3119-4081-9467-a9c8a4a7a01b
4. Click the Download link above the tabulated results
5. Click the Darwin Core Archive button
6. You should now be the download processing page. The title should be 'Under processing'. When the process is complete, you will receive an email. 
7. If you downloaded the correct product, the file name should be similar to the following: 0000214-250121130708018.zip
8. Note the DOI, Dataset name (at the bottom), and the current date as YYYY-MM-DD

## How To Publish Dataset Profiles
1. Copy the dataset profiles to the web directory by running the utils/processing/copy-profiles-to-web.py script.
2. Generate the master metadata yaml file by running the utils/processing/generate-master-meta-yaml.py script
3. Generate source data for webpages by running the utils/processing/generate-web-source-data.py script

## Launch the documentation pages
1. Open the console, activate the virtual environment
2. From the web folder, run $flask run
3. Open a browser to localhost:5000