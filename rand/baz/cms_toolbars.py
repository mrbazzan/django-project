from django.shortcuts import reverse

from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from cms.toolbar.items import Break, SubMenu
from cms.cms_toolbars import ADMIN_MENU_IDENTIFIER, ADMINISTRATION_BREAK


@toolbar_pool.register
class SpouseToolbar(CMSToolbar):
    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu(ADMIN_MENU_IDENTIFIER, "Apps")
        position = admin_menu.get_alphabetical_insert_position(
            "Staff",
            SubMenu
        )
        if not position:
            position = admin_menu.find_first(Break, identifier=ADMINISTRATION_BREAK) + 1
            admin_menu.add_break('custom-break', position=position)

        menu = admin_menu.get_or_create_menu("staff-menu", "Staff ...", position=position)
        menu.add_sideframe_item("Staff List", url=reverse("admin:baz_spouse_changelist"))
        menu.add_modal_item("Add new staff member", url=reverse("admin:baz_spouse_add"))

