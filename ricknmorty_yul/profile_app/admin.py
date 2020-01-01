from django.contrib import admin

# Register your models here.


from profile_app.models import Profile, Planet, Gender, Species, Status, Type

admin.site.register(Planet)
admin.site.register(Gender)
admin.site.register(Profile)
admin.site.register(Species)
admin.site.register(Status)
admin.site.register(Type)