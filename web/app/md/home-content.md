## GBIF Occurrence Dataset Exploration Tools and Profiler
A collection of interactive dataset profiles of GBIF Occurrence Datasets

### Source Data
The source data directory contains the source occurrence datasets downloaded using the [Dataset Search](https://www.gbif.org/dataset/search) in the GBIF Portal
Datasets are organized by package ID, the identifier assigned by GBIF when a dataset is selected for download. See the source--data-inventory.md document for a tabulated summary.

### Datset Profiler Libraries
| Library | URL                                                                                | Description                                                                                                                                                                                                                                                          | 
| -- |------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| YData Profiler | [https://docs.profiling.ydata.ai/latest/](https://docs.profiling.ydata.ai/latest/) | Data quality profiling and exploratory data analysis are crucial steps in the process of Data Science and Machine Learning development. YData-profiling is a leading tool in the data understanding step of the data science workflow as a pioneering Python package. |
| Sweetviz | [https://pypi.org/project/sweetviz/](https://pypi.org/project/sweetviz/) | A pandas-based library to visualize and compare datasets.                                                                                                                                                                                                            |

### Profiling Library Notes
1. Sweetviz requires downgrading numpy to 1.26.4 (last version before 2.0.0)

