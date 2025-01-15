# App

```
├───analysis
│   │   basic-stats.py
│   │   detect-csv-column_type.py
│   │   parameter-counts.py
│   │   unique-values.py
│   ├───output
│   │   └───parameter-counts
├───profilers
│   │   sweetviz-profiler.py    | Generate Sweetviz profiles
│   │   ydata-profiler.py       | Generate YData profiles
│   ├───configs                 | Configuration files for profiler libraries
│   └───output                  | Ouput profiles from both sweetviz-profiler.py and ydata-profiler.py
├───schemas
│   │   generate-csvstats.py    | Generate CSV Statitics for specified CSV files in source data directory
│   │   generate-table-schemas.py   | Generate Tableschemes for specified CSV files in source data directory
│   ├───csvstats                | Output from generate-csvstats.py
│   └───tableschemas            | Output from generate-table-schemas.py
└───utils
        columns.py
        convert-tsv-to-csv.py
        copy-files-to-web.py
        parse-xml.py
        path-tests.py
        __init__.py
```