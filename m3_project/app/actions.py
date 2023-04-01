from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Group, Permission
from objectpack.tree_object_pack.actions import ObjectPack
from objectpack.ui import ModelEditWindow

from .ui import ( ContentTypeListWindow, 
                UserListWindow, UserAddWindow,
                GroupListWindow,
                PermissionListWindow, PermissionAddWindow
)


class ContentTypeActionPack(ObjectPack):
    """
    Класс, реализующий набор действий для работы с моделью ContentType.
    """
    model = ContentType
    list_window = ContentTypeListWindow
    add_window = edit_window = ModelEditWindow.fabricate(model=ContentType)
    add_to_menu = True
    add_to_desktop = True


class UserActionPack(ObjectPack):
    """
    Класс, реализующий набор действий для работы с моделью User.
    """
    model = User
    list_window = UserListWindow
    add_window = edit_window = UserAddWindow
    add_to_menu = True
    add_to_desktop = True


class GroupActionPack(ObjectPack):
    """
    Класс, реализующий набор действий для работы с моделью Group.
    """
    model = Group
    list_window = GroupListWindow
    add_window = edit_window = ModelEditWindow.fabricate(model=Group)
    add_to_menu = True
    add_to_desktop = True


class PermissionActionPack(ObjectPack):
    """
    Класс, реализующий набор действий для работы с моделью Permission.
    """
    model = Permission
    list_window = PermissionListWindow
    add_window = edit_window = PermissionAddWindow
    add_to_menu = True
    add_to_desktop = True
