from django.shortcuts import render
from django.views import View
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from datas.models import IlmiyFaoliyat


def download_ilmiyfaoliyat(request, id):
    # Ilmiy faoliyatni olish
    ilmiy = IlmiyFaoliyat.objects.get(id=id)

    # PDF faylini yaratish uchun response sozlamalari
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="ilmiy_faoliyat_{ilmiy.id}.pdf"'

    # PDF canvas
    pdf = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    # PDF faylini yozish
    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, height - 100, f"Faoliyat nomi: {ilmiy.nomi}")
    pdf.drawString(100, height - 120, f"Muallif: {ilmiy.rahbar}")
    pdf.drawString(100, height - 140, f"Turi: {ilmiy.turi}")
    pdf.drawString(100, height - 160, f"Izoh: {ilmiy.izoh if ilmiy.izoh else 'Izoh mavjud emas'}")

    # PDF-ni saqlash va foydalanuvchiga yuborish
    pdf.showPage()
    pdf.save()

    return response


class FakultetView(View):
    def get(self, request):
        return render(request, "fakultetlar.html")


class FakultetDetailView(View):
    def get(self, request):
        return render(request, "fakultet_detail.html")


class FakultetCreateView(View):
    def get(self, request):
        return render(request, "fakultet_create.html")


class GuruhListView(View):
    def get(self, request):
        return render(request, "guruhlar.html")


class GuruhDetailView(View):
    def get(self, request):
        return render(request, "guruh_detail.html")


class GuruhCreateView(View):
    def get(self, request):
        return render(request, "guruh_create.html")


class TalabalarListView(View):
    def get(self, request):
        return render(request, "talabalar.html")


class TalabalarDetailView(View):
    def get(self, request):
        return render(request, "talaba_detail.html")


class TalabalarCreateView(View):
    def get(self, request):
        return render(request, "talaba_create.html")


class UstozListView(View):
    def get(self, request):
        return render(request, "ustozlar.html")


class UstozDetailView(View):
    def get(self, request):
        return render(request, "ustoz_detail.html")


class UstozCreateView(View):
    def get(self, request):
        return render(request, "ustoz_create.html")


class IlmiyListView(View):
    def get(self, request):
        return render(request, "ilmiyfaoliyat.html")


class IlmiyDetailView(View):
    def get(self, request):
        return render(request, "ilmiyfaoliyat_detail.html")


class IlmiyCreateView(View):
    def get(self, request):
        return render(request, "ilmiy_create.html")


class StipendiyaListView(View):
    def get(self, request):
        return render(request, "stipendiyalar.html")


class StipendiyaDetailView(View):
    def get(self, request):
        return render(request, "stipendiyalar_detail.html")


class StipendiyaCreateView(View):
    def get(self, request):
        return render(request, "stipendiyalar_create.html")

