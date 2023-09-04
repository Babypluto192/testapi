from django.contrib import admin
from .models import Chasti
from .models import Trailers
from .models import SpinOff
from .models import Fanati

# Register your models here.

admin.site.register(Chasti)
admin.site.register(Trailers)
admin.site.register(SpinOff)
admin.site.register(Fanati)
