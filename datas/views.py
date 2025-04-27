from rest_framework import viewsets
from .models import Fakultet, TalimShakli, TalimTuri, Stipendiya, Guruh, Talaba, Ustoz, IlmiyFaoliyat
from .serializers import FakultetSerializer, TalimShakliSerializer, TalimTuriSerializer, StipendiyaSerializer, GuruhSerializer, TalabaSerializer, UstozSerializer, IlmiyFaoliyatSerializer


class FakultetViewSet(viewsets.ModelViewSet):
    queryset = Fakultet.objects.all()
    serializer_class = FakultetSerializer


class TalimShakliViewSet(viewsets.ModelViewSet):
    queryset = TalimShakli.objects.all()
    serializer_class = TalimShakliSerializer


class TalimTuriViewSet(viewsets.ModelViewSet):
    queryset = TalimTuri.objects.all()
    serializer_class = TalimTuriSerializer


class StipendiyaViewSet(viewsets.ModelViewSet):
    queryset = Stipendiya.objects.all()
    serializer_class = StipendiyaSerializer


class GuruhViewSet(viewsets.ModelViewSet):
    queryset = Guruh.objects.all()
    serializer_class = GuruhSerializer


class TalabaViewSet(viewsets.ModelViewSet):
    queryset = Talaba.objects.all()
    serializer_class = TalabaSerializer


class UstozViewSet(viewsets.ModelViewSet):
    queryset = Ustoz.objects.all()
    serializer_class = UstozSerializer


class IlmiyFaoliyatViewSet(viewsets.ModelViewSet):
    queryset = IlmiyFaoliyat.objects.all()
    serializer_class = IlmiyFaoliyatSerializer
