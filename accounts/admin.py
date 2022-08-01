from atexit import register
from django.contrib import admin

from accounts.models import MoreUserData

admin.site.register(MoreUserData)
