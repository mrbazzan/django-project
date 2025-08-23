
from .menus import SpouseSubMenu

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

from .models import Spouse


@apphook_pool.register
class SpouseApp(CMSApp):
    name = "Spouse"
    _urls = ["baz.urls",]
    app_name = "baz"
    _menus = [SpouseSubMenu, ]
