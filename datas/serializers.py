from rest_framework import serializers
from .models import Fakultet, TalimShakli, TalimTuri, Stipendiya, Guruh, Talaba, Ustoz, IlmiyFaoliyat


class FakultetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fakultet
        fields = '__all__'


class TalimShakliSerializer(serializers.ModelSerializer):
    class Meta:
        model = TalimShakli
        fields = '__all__'


class TalimTuriSerializer(serializers.ModelSerializer):
    class Meta:
        model = TalimTuri
        fields = '__all__'


class StipendiyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stipendiya
        fields = '__all__'


class GuruhSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guruh
        fields = '__all__'


class TalabaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talaba
        fields = '__all__'


class UstozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ustoz
        fields = '__all__'


class IlmiyFaoliyatSerializer(serializers.ModelSerializer):
    class Meta:
        model = IlmiyFaoliyat
        fields = '__all__'
