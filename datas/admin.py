from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from .models import Fakultet, Guruh, TalimShakli, TalimTuri, Stipendiya, Talaba, Ustoz, IlmiyFaoliyat


class FakultetResource(resources.ModelResource):
    class Meta:
        model = Fakultet


class GuruhResource(resources.ModelResource):
    class Meta:
        model = Guruh


class TalimShakliResource(resources.ModelResource):
    class Meta:
        model = TalimShakli


class TalimTuriResource(resources.ModelResource):
    class Meta:
        model = TalimTuri


class StipendiyaResource(resources.ModelResource):
    class Meta:
        model = Stipendiya


class TalabaResource(resources.ModelResource):
    class Meta:
        model = Talaba


class UstozResource(resources.ModelResource):
    class Meta:
        model = Ustoz


class IlmiyFaoliyatResource(resources.ModelResource):
    class Meta:
        model = IlmiyFaoliyat


# Admin klasslar
@admin.register(Fakultet)
class FakultetAdmin(ImportExportModelAdmin):
    resource_class = FakultetResource
    list_display = ('nomi', 'yaratilgan_sana', 'dekan', 'zam_dekan')


@admin.register(Guruh)
class GuruhAdmin(ImportExportModelAdmin):
    resource_class = GuruhResource
    list_display = ('nomi', 'turi', 'fakultet')


@admin.register(TalimShakli)
class TalimShakliAdmin(ImportExportModelAdmin):
    resource_class = TalimShakliResource
    list_display = ('nomi',)


@admin.register(TalimTuri)
class TalimTuriAdmin(ImportExportModelAdmin):
    resource_class = TalimTuriResource
    list_display = ('turi',)


@admin.register(Stipendiya)
class StipendiyaAdmin(ImportExportModelAdmin):
    resource_class = StipendiyaResource
    list_display = ('nomi', 'puli', 'muddati')


@admin.register(Talaba)
class TalabaAdmin(ImportExportModelAdmin):
    resource_class = TalabaResource
    list_display = ('ism', 'familiya', 'fakultet', 'guruh', 'talim_shakli', 'talim_turi', 'telefon')


@admin.register(Ustoz)
class UstozAdmin(ImportExportModelAdmin):
    resource_class = UstozResource
    list_display = ('ism', 'familiya', 'mutaxassislik', 'yosh', 'daraja')


@admin.register(IlmiyFaoliyat)
class IlmiyFaoliyatAdmin(ImportExportModelAdmin):
    resource_class = IlmiyFaoliyatResource
    list_display = ('nomi', 'turi', 'sanasi', 'ishtirokchilar', 'rahbar', 'holati')
