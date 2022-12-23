from rest_framework import serializers
from rest_framework.fields import MultipleChoiceField

from lessons.models import Lesson, Download


class BaseLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            "id",
            "title",
            "description",
            "equipment",
            "pdf",
            "material_type",
            "language",
            "topic",
            # "difficulty",
            # "age",
            "age_and_difficulty",
            "duration",
            "activity_type",
            "links",
        ]


class LessonSerializer(BaseLessonSerializer):
    similar_lessons = serializers.SerializerMethodField()
    language = MultipleChoiceField(choices=Lesson.LANGUAGE_CHOICES)

    class Meta:
        model = Lesson
        fields = [
            "id",
            "created_at",
            "title",
            "description",
            "equipment",
            "pdf",
            "material_type",
            "language",
            "topic",
            # "difficulty",
            # "age",
            "age_and_difficulty",
            "duration",
            "activity_type",
            "similar_lessons",
            "links",
        ]

    def get_similar_lessons(self, lesson):
        similar_to = Lesson.objects.filter(id__in=lesson.similar_to.all()).exclude(
            id=lesson.id
        )
        similar_from = Lesson.objects.filter(similar_to=lesson).exclude(id=lesson.id)

        # the | (pipe) operator works like a union, except it merges
        # the querysets after they were returned instead of in the query
        all_similar_lessons = set(similar_to | similar_from)
        serializer = BaseLessonSerializer(all_similar_lessons, many=True)

        return serializer.data


class DownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Download
        fields = "__all__"
