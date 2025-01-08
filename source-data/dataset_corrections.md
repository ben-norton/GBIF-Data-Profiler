# Dataset Corrections
**Last Modified: 2025010**
---
### Purpose: 
Inventory of errroneous rows removed from datasets to resolve column errors (see below)

### Saving Convention
Original occurrence file preserved as occurrence_original.txt
New corrected file saved as occurrence.txt

## Revisions
Tabulated summary of lines removed from original source files to resolve errors. The removed lines are listed by gbifID and catalogNumber

| Dataset ID | gbifID      | catalogNumber   | Date     |
| -- |-------------|-----------------|----------|
| 0052484-241126133413365 | 1318382410  | USNMENT00398378 | 20250106 |
| 0052487-241126133413365 | 1318769830  | US 2118062      | 20240106 |
| 0052489-241126133413365 | 4122282362  | USNM 1446788    | 20240103 |
| 0055081-241126133413365 | 1319787323 | USNM 64641 | 20240106 |
| 0049395-241126133413365 | 1321816491 | US 580118 | 20240107 |



------------------------
## Errors

Dataset: 0052484-241126133413365
pandas.errors.ParserError: Error tokenizing data. C error: Expected 223 fields in line 316363, saw 264

Dataset: 0052487-241126133413365
pandas.errors.ParserError: Error tokenizing data. C error: Expected 223 fields in line 631633, saw 241

Dataset: 0052489-241126133413365
pandas.errors.ParserError: Error tokenizing data. C error: Expected 223 fields in line 252991, saw 253

Dataset: 0055081-241126133413365
pandas.errors.ParserError: Error tokenizing data. C error: Expected 223 fields in line 83516, saw 268

--- 
## Notes
1. Its clear that the error is causing a misalignment of columns, most likely due to tab characters embedded in comment fields.
2. Removing a single line resolved the error for several. The liklihood that a tab character issue is exclusive to a single record in a dataset containing hundreds of thousands sheds doubt on the tab characters as being the sole culprit.
3. In file 0052487-241126133413365, the following values occur on line 631633
    earliestEraOrLowestErathem: 44.2923
    latestEraOrHighestErathem: -71.2808
