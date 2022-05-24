from setuptools import setup

setup(
   name='spongeman-cli',
   version='1.1',
   install_requires=["termcolor", "BeautifulSoup4", "prettytable", "youtube-dlc", "halo", "requests"], 
   scripts=
   [
      'spongeman-cli',
      'func.py'
   ]
)
