# gbif-data-utils
GBIF Data Parsing Utilities using Python

## Data Quality and Tabular Data Utility Libraries
| Library | PIP                                         | URL                                       | Description                                                                                                                                                                                                                                                           | 
| -- |---------------------------------------------|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| YData Profiler |                                             | https://docs.profiling.ydata.ai/latest/   | Data quality profiling and exploratory data analysis are crucial steps in the process of Data Science and Machine Learning development. YData-profiling is a leading tool in the data understanding step of the data science workflow as a pioneering Python package. |
| Pandas DQ | pandas_dq                                   | https://github.com/AutoViML/pandas_dq     | pandas-dq is the ultimate data quality toolkit for pandas dataframes.                                                                                                                                                                                                 |
| CSV Detective | csv-detective                               | https://github.com/datagouv/csv-detective | This is a package to automatically detect column content in tabular files.                                                                                                                                                                                            |
| Sweetviz | sweetviz | https://pypi.org/project/sweetviz/        | A pandas-based library to visualize and compare datasets.                                                                                                                                                                                                             |

## Profiling Library Notes
1. Sweetviz requires downgrading numpy to 1.26.4 (last version before 2.0.0)