from objectpack.ui import BaseListWindow, BaseEditWindow, make_combo_box
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Group, Permission
from m3_ext.ui import all_components as ext


class ContentTypeListWindow(BaseListWindow):
    """
    Окно списка объектов ContentType
    """
    model = ContentType  # модель, по которой строится список объектов


class UserListWindow(BaseListWindow):
    """
    Окно списка объектов User
    """
    model = User  # модель, по которой строится список объектов


class UserAddWindow(BaseEditWindow):
    """
    Окно создания нового пользователя
    """
    def _init_components(self):
        """
        Инициализируем компоненты окна
        """
        super(UserAddWindow, self)._init_components()

        self.field__username = ext.ExtStringField(
            label=u'Имя пользователя',
            name='username',
            allow_blank=False,
            anchor='100%')

        self.field__password = ext.ExtStringField(
            label=u'Пароль',
            name='password',
            allow_blank=False,
            anchor='100%')

        self.field__email = ext.ExtStringField(
            label=u'E-mail',
            name='email',
            allow_blank=False,
            anchor='100%')
        
        self.field__first_name = ext.ExtStringField(
            label=u'Имя',
            name='first_name',
            allow_blank=False,
            anchor='100%')
        
        self.field__last_name = ext.ExtStringField(
            label=u'Фамилия',
            name='last_name',
            allow_blank=False,
            anchor='100%')

        self.field__is_superuser = ext.ExtCheckBox(
            label=u'Администратор',
            name='is_superuser',
            anchor='100%',
            checked=False
        )

        self.field__is_staff = ext.ExtCheckBox(
            label=u'Персонал',
            name='is_staff',
            anchor='100%',
            checked=False
        )

        self.field__is_active = ext.ExtCheckBox(
            label=u'Активный',
            name='is_active',
            anchor='100%',
            checked=True
        )

        self.field__last_login = ext.ExtDateField(
                    label=u'Последний вход',
                    name='last_login',
                    anchor='100%',
                    format='d.m.Y'
                )

        self.field__date_joined = ext.ExtDateField(
                    label=u'Дата регистрации',
                    name='date_joined',
                    anchor='100%',
                    format='d.m.Y'
                )



    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__username,
            self.field__password,
            self.field__email,
            self.field__first_name,
            self.field__last_name,
            self.field__is_superuser,
            self.field__is_staff,
            self.field__is_active,
            self.field__last_login,
            self.field__date_joined
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'


class GroupListWindow(BaseListWindow):
    """
    Окно списка объектов Group
    """
    model = Group  # модель, по которой строится список объектов


class PermissionListWindow(BaseListWindow):
    """
    Окно списка объектов Permission
    """
    model = Permission  # модель, по которой строится список объектов

class PermissionAddWindow(BaseEditWindow):
    """
    Окно создания нового Permission
    """
    def _init_components(self):
        """
        Инициализируем компоненты окна
        """
        super(PermissionAddWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label=u'Название',
            name='name',
            allow_blank=False,
            anchor='100%'
        )

        content_types = ContentType.objects.all()
        content_type_choices = [(ct.id, ct.name) for ct in content_types]
        self.field__content_type = make_combo_box(
            label=u'Тип контента',
            name='content_type_id',
            allow_blank=False,
            anchor='100%',
            data=content_type_choices,
            display_field='name',
        )

        self.field__codename = ext.ExtStringField(
            label=u'Кодовое имя',
            name='codename',
            allow_blank=False,
            anchor='100%'
        )

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(PermissionAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__content_type,
            self.field__codename,
        ))

    def set_params(self, params):
        """
        Установка параметров окна
        :params: Словарь с параметрами, передается из пака
        """
        super(PermissionAddWindow, self).set_params(params)
        self.height = 'auto'

