import os

# script to install necessary packages in vscode server hosted on google colab
os.system('pip install fastai -Uq')

os.system('pip install nbdev -Uq')

os.system('sudo apt-get install vim')

os.system('pip install ipywidgets -Uq')

os.system('jupyter nbextension enable --py widgetsnbextension')
