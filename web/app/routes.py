from app import app
from flask import render_template
from markupsafe import Markup
import markdown2
import pandas as pd
import yaml

app.debug = True

with open('app/meta.yml') as metadata:
    meta = yaml.safe_load(metadata)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html',
                           pageTitle='404 Error'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html',
                           pageTitle='500 Unknown Error'), 500

# Homepage with content stored in markdown file
@app.route('/')
def home():
    home_mdfile = 'app/md/home-content.md'
    with open(home_mdfile, encoding="utf-8") as f:
        marked_text = markdown2.markdown(f.read(), extras=["tables", "fenced-code-blocks"])
    return render_template('home.html',
                           home_markdown=Markup(marked_text),
                           pageTitle='Home',
                           title=meta['title'],
                           githubRepo=meta['github-repo'],
                           slug='home'
                           )
@app.route('/datasets')
def datasets():
    datasets_mdfile = 'app/md/datasets-content.md'
    with open(datasets_mdfile, encoding="utf-8") as f:
        marked_text = markdown2.markdown(f.read(), extras=["tables", "fenced-code-blocks"])

    datasets_csv = 'app/data/web_source.csv'
    df = pd.read_csv(datasets_csv, encoding='utf-8')
    df_datasets = df.sort_values(by=['package_id', 'profile_library'])

    df_datasets_index = df[['package_id','title','institution_code']]
    df_datasets_index = df_datasets_index.drop_duplicates()
    df_datasets_index = df_datasets_index.sort_values(by=['institution_code','title'])

    grpdict = df.groupby(['package_id','title','institution_code'])[
        ['record_count','download_date','doi','profile_library','profile_link']].apply(
        lambda g: list(map(tuple, g.values.tolist()))).to_dict()

    grouped_datasets = []
    for i in grpdict:
        grouped_datasets.append({
            'package_id': i[0],
            'title': i[1],
            'profiles': grpdict[i]
        })
    #grouped_datasets =  grouped_datasets.sort_values(by=['institution_code', 'title'])

    return render_template('datasets.html',
                           datasets_markdown=Markup(marked_text),
                           datasets=df_datasets,
                           datasets_index=df_datasets_index,
                           pageTitle='Datasets',
                           title=meta['title'],
                           githubRepo=meta['github-repo'],
                           slug='datasets'
                           )