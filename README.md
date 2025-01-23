# GBIF Data Profiler
GBIF Data Parsing Utilities, Profilers, and Web-based publishing site

## Website
You can explore an existing inventory of interactive profiles by visiting the repository website: [https://ben-norton.github.io/GBIF-Data-Profiling/](https://ben-norton.github.io/GBIF-Data-Profiling/)

## Project Directory Structure
```
├───app
|   ├───analysis    | A collection of scripts for running basic structural analysis of source data files
|   ├───profilers   | Scripts to generate interactive dataset profiles, see dataset profiler libraries
|   ├───schemas     | Tabular schemas and CSV file statistics generated from the source dataset files
|   └───utils       | General support utility scripts for performing specific tasks such as converting tab-delimited to comma-separated
├───docs            | Documentation markdown files
├───source-data     | Source occurrence datasets
├───web             | Static site generator for publishing interactive profiles using VitePress
```

## Source Data
All source datasets downloaded from [Dataset Search](https://www.gbif.org/dataset/search) in the GBIF Portal are extracted and stored in the source-datasets folder. Many occurrence datasets
are very large > 1GB, which can exceed the allocation provided by certain GitHub plans. Therefore, a simple example is included with the repo. Except for the example dataset, the contents of 
the source-datasets are set to ignore in order to prevent exceeding the GitHub limitations.

Datasets are organized by package ID, the identifier assigned by GBIF when a dataset is selected for download. See the source--data-inventory.md document for a tabulated summary.
Please see the README file in the source-datasets folder and the README.md file in the project-docs for more information including procedures for downloading your own datasets.


## Datset Profiler Libraries
| Library | PIP                                         | URL                                       | Description                                                                                                                                                                                                                                                           | 
| -- |---------------------------------------------|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| YData Profiler |                                             | https://docs.profiling.ydata.ai/latest/   | Data quality profiling and exploratory data analysis are crucial steps in the process of Data Science and Machine Learning development. YData-profiling is a leading tool in the data understanding step of the data science workflow as a pioneering Python package. |
| Sweetviz | sweetviz | https://pypi.org/project/sweetviz/        | A pandas-based library to visualize and compare datasets.                                                                                                                                                                                                             |

## Profiling Library Notes
1. Sweetviz requires downgrading numpy to 1.26.4 (last version before 2.0.0)

