from wagtail import hooks

@hooks.register('construct_main_menu')
def remove_unwanted_main_menu_items(request, menu_items):
    items_to_remove = ['explorer', 'help', 'search', 'documents', 'reports']
    menu_items[:] = [item for item in menu_items if item.name not in items_to_remove]

@hooks.register('construct_settings_menu')
def keep_only_users_in_settings_menu(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name == 'users']
