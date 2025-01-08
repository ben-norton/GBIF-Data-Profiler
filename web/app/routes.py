from flask import render_template
from markupsafe import Markup
import markdown2
import pandas as pd
import yaml
from web import app

with open('app/meta.yml') as metadata:
    meta = yaml.safe_load(metadata)


