
from flask import Flask, render_template
from flask_frozen import Freezer
from flask_assets import Environment, Bundle
from markupsafe import Markup
import sys
import markdown2
import pandas as pd
import yaml
from pathlib import Path

current_dir = Path.cwd()
root_dir = current_dir.parent.parent
build_dir = str(root_dir) + 'web/app/build'
app = Flask(__name__, template_folder='templates')
freezer = Freezer(app)

assets = Environment(app)
css = Bundle("custom/css/custom.css", "assets/plugins/pygments/pygments.css", output="bundled/style.css")
assets.register("site_css", css)

#app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['FREEZER_DESTINATION'] = 'build'
app.config['FREEZER_RELATIVE_URLS'] = True
#app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True

with open('meta.yml') as metadata:
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
    home_mdfile = 'md/home-content.md'
    with open(home_mdfile, encoding="utf-8") as f:
        marked_text = markdown2.markdown(f.read(), extras=["tables", "fenced-code-blocks"])
    return render_template('home.html',
                           home_markdown=Markup(marked_text),
                           pageTitle='Home',
                           title=meta['title'],
                           githubRepo=meta['github-repo'],
                           slug='home'
                           )
@app.route('/datasets/')
def source_datasets():
    datasets_mdfile = 'md/datasets-content.md'
    with open(datasets_mdfile, encoding="utf-8") as f:
        marked_text = markdown2.markdown(f.read(), extras=["tables", "fenced-code-blocks"])

    datasets_csv = 'data/web-source.csv'
    df = pd.read_csv(datasets_csv, encoding='utf-8')
    df_datasets = df.sort_values(by=['package_id', 'profile_library'])

    df_datasets_index = df[['package_id','title']]
    df_datasets_index = df_datasets_index.drop_duplicates()
#    df_datasets_index = df_datasets_index.sort_values(by=['title'])

    return render_template('datasets.html',
                           datasets_markdown=Markup(marked_text),
                           datasets=df_datasets,
                           datasets_index=df_datasets_index,
                           pageTitle='Datasets',
                           title=meta['title'],
                           githubRepo=meta['github-repo'],
                           slug='datasets'
                           )

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
        print("Written to: " + build_dir)
    else:
        app.run(port=8000)