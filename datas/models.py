from django.db import models


class Fakultet(models.Model):
    nomi = models.CharField(max_length=255)
    yaratilgan_sana = models.DateField()
    dekan = models.CharField(max_length=255)
    zam_dekan = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi


class Guruh(models.Model):
    fakultet = models.ForeignKey(Fakultet, on_delete=models.CASCADE)
    nomi = models.CharField(max_length=100)
    turi = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nomi} ({self.turi})"


class TalimShakli(models.Model):
    nomi = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi


class TalimTuri(models.Model):
    turi = models.CharField(max_length=255)

    def __str__(self):
        return self.turi


class Stipendiya(models.Model):
    nomi = models.CharField(max_length=255)
    puli = models.DecimalField(max_digits=10, decimal_places=2)
    muddati = models.CharField(max_length=100)

    def __str__(self):
        return self.nomi


class Talaba(models.Model):
    ism = models.CharField(max_length=255)
    familiya = models.CharField(max_length=255)
    tugilgan_kun = models.DateField()
    fakultet = models.ForeignKey(Fakultet, on_delete=models.CASCADE)
    guruh = models.ForeignKey(Guruh, on_delete=models.SET_NULL, null=True)
    rasm = models.ImageField(upload_to='talaba_rasm/', null=True, blank=True)
    talim_shakli = models.ForeignKey(TalimShakli, on_delete=models.SET_NULL, null=True)
    talim_turi = models.ForeignKey(TalimTuri, on_delete=models.SET_NULL, null=True)
    nomdor_stipendiya = models.ForeignKey(Stipendiya, on_delete=models.SET_NULL, null=True, blank=True)
    telefon = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.ism} {self.familiya}"


class Ustoz(models.Model):
    ism = models.CharField(max_length=255)
    familiya = models.CharField(max_length=255)
    mutaxassislik = models.CharField(max_length=255)
    yosh = models.PositiveIntegerField()
    daraja = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.ism} {self.familiya}"


class IlmiyFaoliyat(models.Model):
    nomi = models.CharField(max_length=255)
    turi = models.CharField(max_length=255)
    sanasi = models.DateField()
    izoh = models.TextField()
    ishtirokchilar = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    rahbar = models.ForeignKey(Ustoz, on_delete=models.SET_NULL, null=True)
    natija = models.TextField()
    holati = models.CharField(max_length=255)
    moliyaviy_manba = models.CharField(max_length=255)
    tadqiqot_joyi = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi
