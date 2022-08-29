from django_filters import FilterSet, MultipleChoiceFilter

from lessons.models import Lesson


class LessonFilter(FilterSet):
    language = MultipleChoiceFilter(
        field_name="language", choices=Lesson.LANGUAGE_CHOICES
    )

    class Meta:
        model = Lesson
        fields = ("language",)


# class LessonFilter(BaseFilterBackend):
#     """ """

#     def filter_queryset(self, request, queryset, view):
#         print(request.GET.get("language"))
#         return queryset
