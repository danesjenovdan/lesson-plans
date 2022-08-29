# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q

from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from lessons.models import Lesson, Download
from lessons.serializers import LessonSerializer, DownloadSerializer
from lessons.filters import LessonFilter


class LessonViewSet(ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing lessons.
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_queryset(self):
        """
        Optionally filters lessons based on query parameters.
        """
        queryset = Lesson.objects.all()
        q_set = Q()

        # filter material_types
        material_types_q = Q()
        if material_types := self.request.query_params.get("material_type"):
            material_types = material_types.split(",")
            for material_type in material_types:
                material_types_q.add(Q(material_type__icontains=material_type), Q.OR)

        # filter languages
        languages_q = Q()
        if languages := self.request.query_params.get("language"):
            languages = languages.split(",")
            for language in languages:
                languages_q.add(Q(language__icontains=language), Q.OR)

        # filter topics
        topics_q = Q()
        if topics := self.request.query_params.get("topic"):
            topics = topics.split(",")
            for topic in topics:
                topics_q.add(Q(topic__icontains=topic), Q.OR)

        # # filter difficulties
        # difficulties_q = Q()
        # if difficulties := self.request.query_params.get("difficulty"):
        #     difficulties = difficulties.split(",")
        #     for difficulty in difficulties:
        #         difficulties_q.add(Q(difficulty__icontains=difficulty), Q.OR)

        # # filter ages
        # ages_q = Q()
        # if ages := self.request.query_params.get("age"):
        #     ages = ages.split(",")
        #     for age in ages:
        #         ages_q.add(Q(age__icontains=age), Q.OR)

        # filter age_and_difficulty
        ages_and_difficulties_q = Q()
        if ages_and_difficulties := self.request.query_params.get("age_and_difficulty"):
            ages_and_difficulties = ages_and_difficulties.split(",")
            for age_and_difficulty in ages_and_difficulties:
                ages_and_difficulties_q.add(
                    Q(age_and_difficulty__icontains=age_and_difficulty), Q.OR
                )

        # filter durations
        durations_q = Q()
        if durations := self.request.query_params.get("duration"):
            durations = durations.split(",")
            for duration in durations:
                durations_q.add(Q(duration__icontains=duration), Q.OR)

        # filter activity_types
        activity_types_q = Q()
        if activity_types := self.request.query_params.get("activity_type"):
            activity_types = activity_types.split(",")
            for activity_type in activity_types:
                activity_types_q.add(Q(language__icontains=activity_type), Q.OR)

        queryset = Lesson.objects.filter(
            material_types_q,
            languages_q,
            topics_q,
            # difficulties_q,
            # ages_q,
            ages_and_difficulties_q,
            durations_q,
            activity_types_q,
        )
        return queryset


class DownloadViewSet(ModelViewSet):
    queryset = Download.objects.all()
    serializer_class = DownloadSerializer
    http_method_names = ["post"]
