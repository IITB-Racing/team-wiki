# IITB DV Team wiki

1. git & python should be installed
2. pip install mkdocs, mkdocstrings, mkdocs-video
3. change directory to team_wiki/
4. mkdocs serve (this locally hosts the website at http://127.0.0.1:8000/)


You can change the left nav bar structure in - mkdocs.yml

Changing individual pages in docs/... changes the page content. These use Markdown syntax (.md), check docs/estimation/overview.md for syntax (pretty intuitive, but thoda bt).

For deploying on github pages:
1. mkdocs build: makes all the html files from mds in /site folder
2. mkdocs gh-deploy: takes the newly build /site and pushes it to gh-pages branch in this repo with only the req html files. then that is pushed to web.