import{_ as t,c as r,a1 as a,o}from"./chunks/framework.D_tc8BW1.js";const p=JSON.parse('{"title":"Dataset Corrections","description":"","frontmatter":{},"headers":[],"relativePath":"dataset-corrections.md","filePath":"dataset-corrections.md"}'),s={name:"dataset-corrections.md"};function i(d,e,n,l,c,h){return o(),r("div",null,e[0]||(e[0]=[a('<h1 id="dataset-corrections" tabindex="-1">Dataset Corrections <a class="header-anchor" href="#dataset-corrections" aria-label="Permalink to &quot;Dataset Corrections&quot;">​</a></h1><h2 id="last-modified-2025010" tabindex="-1"><strong>Last Modified: 2025010</strong> <a class="header-anchor" href="#last-modified-2025010" aria-label="Permalink to &quot;**Last Modified: 2025010**&quot;">​</a></h2><h3 id="purpose" tabindex="-1">Purpose: <a class="header-anchor" href="#purpose" aria-label="Permalink to &quot;Purpose:&quot;">​</a></h3><p>Inventory of errroneous rows removed from datasets to resolve column errors (see below)</p><h3 id="saving-convention" tabindex="-1">Saving Convention <a class="header-anchor" href="#saving-convention" aria-label="Permalink to &quot;Saving Convention&quot;">​</a></h3><p>Original occurrence file preserved as occurrence_original.txt New corrected file saved as occurrence.txt</p><h2 id="revisions" tabindex="-1">Revisions <a class="header-anchor" href="#revisions" aria-label="Permalink to &quot;Revisions&quot;">​</a></h2><p>Tabulated summary of lines removed from original source files to resolve errors. The removed lines are listed by gbifID and catalogNumber</p><table tabindex="0"><thead><tr><th>Dataset ID</th><th>gbifID</th><th>catalogNumber</th><th>Date</th></tr></thead><tbody><tr><td>0052484-241126133413365</td><td>1318382410</td><td>USNMENT00398378</td><td>20250106</td></tr><tr><td>0052487-241126133413365</td><td>1318769830</td><td>US 2118062</td><td>20240106</td></tr><tr><td>0052489-241126133413365</td><td>4122282362</td><td>USNM 1446788</td><td>20240103</td></tr><tr><td>0055081-241126133413365</td><td>1319787323</td><td>USNM 64641</td><td>20240106</td></tr><tr><td>0049395-241126133413365</td><td>1321816491</td><td>US 580118</td><td>20240107</td></tr></tbody></table><hr><h2 id="errors" tabindex="-1">Errors <a class="header-anchor" href="#errors" aria-label="Permalink to &quot;Errors&quot;">​</a></h2><p>Dataset: 0052484-241126133413365 pandas.errors.ParserError: Error tokenizing data. C error: Expected 223 fields in line 316363, saw 264</p><p>Dataset: 0052487-241126133413365 pandas.errors.ParserError: Error tokenizing data. C error: Expected 223 fields in line 631633, saw 241</p><p>Dataset: 0052489-241126133413365 pandas.errors.ParserError: Error tokenizing data. C error: Expected 223 fields in line 252991, saw 253</p><p>Dataset: 0055081-241126133413365 pandas.errors.ParserError: Error tokenizing data. C error: Expected 223 fields in line 83516, saw 268</p><hr><h2 id="notes" tabindex="-1">Notes <a class="header-anchor" href="#notes" aria-label="Permalink to &quot;Notes&quot;">​</a></h2><ol><li>Its clear that the error is causing a misalignment of columns, most likely due to tab characters embedded in comment fields.</li><li>Removing a single line resolved the error for several. The liklihood that a tab character issue is exclusive to a single record in a dataset containing hundreds of thousands sheds doubt on the tab characters as being the sole culprit.</li><li>In file 0052487-241126133413365, the following values occur on line 631633 earliestEraOrLowestErathem: 44.2923 latestEraOrHighestErathem: -71.2808</li></ol>',18)]))}const f=t(s,[["render",i]]);export{p as __pageData,f as default};