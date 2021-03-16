from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from .models import Favourite

User = get_user_model()


def add_favourite(obj, user):
    """Добовляет в избранное `obj`.
    """
    obj_type = ContentType.objects.get_for_model(obj)
    favourite, is_created = Favourite.objects.get_or_create(
        content_type=obj_type, object_id=obj.id, user=user)
    return favourite


def remove_favourite(obj, user):
    """Удаляет из избранного `obj`.
    """
    obj_type = ContentType.objects.get_for_model(obj)
    Favourite.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user
    ).delete()


def is_favourite(obj, user):
    """Проверяет, добавил ли `user` `obj`.
    """
    if not user.is_authenticated:
        return False
    obj_type = ContentType.objects.get_for_model(obj)
    favourite = Favourite.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user)
    return favourite.exists()
