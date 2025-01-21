# Commands
Last Modified: 2024-01-21

1. Generate pygments
$ pygmentize -S solarized-light -f html -a .codehilite >> static\assets\plugins\pygments\pygments.css
  
2. Build static pages
$ cd web/app
$ python freeze.py build
  
3. Run flask
$ cd web
$ flask run