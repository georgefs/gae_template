import site
import os

CUR_PATH = os.path.dirname(os.path.abspath(__file__))
SITE_PATH = os.path.join(CUR_PATH, 'site-packages/')
APPS_PATH = os.path.join(CUR_PATH, 'apps/')
print SITE_PATH

site.addsitedir(SITE_PATH)
site.addsitedir(APPS_PATH)
