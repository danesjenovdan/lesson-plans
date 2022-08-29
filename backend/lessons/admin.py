# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib.admin.widgets import FilteredSelectMultiple

from lessons.models import Lesson, Link, Download

admin.site.register(Lesson)
admin.site.register(Link)
admin.site.register(Download)
