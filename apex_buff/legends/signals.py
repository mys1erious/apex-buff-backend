from django.dispatch import receiver
from django.db.models.signals import post_delete, pre_save

from .models import LegendType


@receiver(post_delete, sender=LegendType)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from storage
    when corresponding `LegendType` object is deleted.
    """
    if instance.icon_imgf:
        instance.icon_imgf.delete()


# @receiver(pre_save, sender=LegendType)
# def auto_delete_file_on_change(sender, instance, **kwargs):
#     """
#     Deletes old file from storage
#     when corresponding `LegendType` object is updated
#     with new file.
#     """
#     if not instance.pk:
#         return False
#
#     try:
#         old_icon = LegendType.objects.get(pk=instance.pk).icon_imgf
#     except LegendType.DoesNotExist:
#         return False
#
#     print("STILL WORKING: old icon ->", old_icon.url)
#
#     new_icon = instance.icon_imgf
#
#     print("STILL WORKING: new icon ->", new_icon.url)
#
#     if old_icon != new_icon:
#         old_icon.delete()
