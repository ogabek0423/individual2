from rest_framework.routers import DefaultRouter
from .views import FakultetViewSet, TalimShakliViewSet, TalimTuriViewSet, StipendiyaViewSet, GuruhViewSet, TalabaViewSet, UstozViewSet, IlmiyFaoliyatViewSet

router = DefaultRouter()
router.register(r'fakultetlar', FakultetViewSet)
router.register(r'talimshakllar', TalimShakliViewSet)
router.register(r'talimturlari', TalimTuriViewSet)
router.register(r'stipendiyalar', StipendiyaViewSet)
router.register(r'guruhlar', GuruhViewSet)
router.register(r'talabalar', TalabaViewSet)
router.register(r'ustozlar', UstozViewSet)
router.register(r'ilmiyfaoliyatlar', IlmiyFaoliyatViewSet)

urlpatterns = router.urls
