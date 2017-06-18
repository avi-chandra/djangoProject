# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Question, Choice, Person_details, Cities, States

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Person_details)
admin.site.register(Cities)
admin.site.register(States)
