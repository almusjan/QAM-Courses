from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from mysite.models import FavoriteSite


@receiver(post_save, sender=FavoriteSite)
def increase_favorites(sender, instance, **kwargs):
    instance.site.site_favorites = FavoriteSite.objects.filter(site=instance.site).count()
    instance.site.save()


@receiver(post_delete, sender=FavoriteSite)
def decrease_favorites(sender, instance, **kwargs):
    instance.site.site_favorites = FavoriteSite.objects.filter(site=instance.site).count()
    instance.site.save()
