# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class LessonsConfig(AppConfig):
    name = "lessons"

    def ready(self):
        import lessons.signals
