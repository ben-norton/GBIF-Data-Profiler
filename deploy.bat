@echo off
:: Deploy build folder to github pages

rsync -r web/app/build/* docs