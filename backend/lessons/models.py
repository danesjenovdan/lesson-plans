# -*- coding: utf-8 -*-
from django.db import models
from lessons.behaviors.models import BaseModel
from django.db import models
from django.utils import timezone

from multiselectfield import MultiSelectField


class Link(BaseModel):
    url = models.URLField(blank=False, null=False)
    name = models.TextField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.name


class Download(BaseModel):
    ROLE_CHOICES = [
        ("teacher", "Teacher"),
        ("coach", "Debate coach"),
        ("parent", "Parent"),
        ("student", "Student"),
    ]

    name_lastname = models.TextField(blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    country = models.TextField(blank=False, null=False)
    organization = models.TextField(blank=False, null=False)
    role = models.CharField(max_length=7, choices=ROLE_CHOICES, default="student")

    def __str__(self):
        return self.role


class Lesson(BaseModel):
    MATERIAL_TYPE_CHOICES = [
        ("lesson", "Lesson plan"),
        ("coaching", "Coaching guide"),
        ("program", "Program guide"),
        ("curriculum", "Curriculum"),
    ]
    LANGUAGE_CHOICES = [
        ("EN", "English"),
        ("HR", "Croatian"),
        ("NL", "Dutch"),
        ("SL", "Slovenian"),
        ("SK", "Slovak"),
        ("PL", "Polish"),
    ]
    TOPIC_CHOICES = [
        ("argumentation", "Argumentation and reasoning"),
        ("case", "Case building"),
        ("evidence", "Empirical evidence and knowledge"),
        ("games", "Exercises and debate club games"),
        ("intro", "Introduction to debate and debate formats"),
        ("analysis", "Non-argumentative analysis"),
        ("public_speaking", "Public speaking"),
        ("critical_thinking", "Critical thinking"),
        ("motion_analysis", "Motion analysis"),
        ("teacher_development", "Coach/teacher development"),
        ("program_development", "Debate program development"),
    ]
    DIFFICULTY_CHOICES = [
        ("advanced", "Advanced"),
        ("intermediate", "Intermediate"),
        ("beginner", "Beginner"),
    ]
    AGE_CHOICES = [
        ("under_14", "Under 14"),
        ("between_14_and_19", "Between 14 and 19"),
        ("over_19", "Over 19"),
    ]
    DURATION_CHOICES = [
        ("45_min", "45 minutes"),
        ("between_60_and_90 min", "60 - 90 minutes"),
        ("over_90_min", "over 90 minutes"),
    ]
    ACTIVITY_TYPE_CHOICES = [
        ("2yr", "2-year debate program"),
        ("1yr", "1-year debate program"),
        ("6mo", "6-month debate program"),
        ("short", "Short term debate program"),
    ]

    title = models.TextField(blank=False, null=False)
    description = models.TextField(
        blank=False,
        null=False,
        default="Description missing. Please notify the administrator.",
    )
    equipment = models.TextField(blank=True, null=True)
    similar_to = models.ManyToManyField("Lesson", blank=True)
    links = models.ManyToManyField("Link", blank=True)
    pdf = models.FileField()

    # filters/choice fields
    material_type = MultiSelectField(max_length=10, choices=MATERIAL_TYPE_CHOICES)
    language = MultiSelectField(choices=LANGUAGE_CHOICES)
    topic = MultiSelectField(choices=TOPIC_CHOICES)
    # difficulty = MultiSelectField(choices=DIFFICULTY_CHOICES)
    # age = MultiSelectField(choices=AGE_CHOICES)
    age_and_difficulty = MultiSelectField(
        choices=AGE_CHOICES + DIFFICULTY_CHOICES, default=DIFFICULTY_CHOICES[0]
    )
    duration = MultiSelectField(choices=DURATION_CHOICES)
    activity_type = MultiSelectField(choices=ACTIVITY_TYPE_CHOICES)

    def __str__(self):
        return self.title
