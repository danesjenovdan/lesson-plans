from django.db.models.signals import post_save
from django.dispatch import receiver

from lessons.models import Lesson


# @receiver(post_save, sender=Lesson)
# def create_other_side_of_similar_to(sender, instance, created, **kwargs):
#     others = Lesson.objects.filter(
#         id__in=instance.similar_to.all().values_list("id", flat=True)
#     )
#     for other in others:
#         other.similar_to.add(instance)
#         other.save()
