import site
import os

CUR_PATH = os.path.dirname(os.path.abspath(__file__))
SITE_PATH = os.path.join(CUR_PATH, 'site-packages/')

site.addsitedir(SITE_PATH)
