from cms.app_base import CMSAppConfig

from .models import Spouse
from .views import spouse_detail_view

class _(CMSAppConfig):
    cms_enabled = True
    cms_toolbar_enabled_models = [(Spouse, spouse_detail_view)]

