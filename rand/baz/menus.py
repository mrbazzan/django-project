
from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from cms.menu_bases import CMSAttachMenu

from .models import Spouse


class SpouseSubMenu(CMSAttachMenu):
    name = "Staff sub-menu"

    def get_nodes(self, request):
        nodes = []
        for spouse in Spouse.objects.all():
            node = NavigationNode(
                spouse.name,
                spouse.absolute_url(),
                spouse.id
            )
            nodes.append(node)
        return nodes

menu_pool.register_menu(SpouseSubMenu)
