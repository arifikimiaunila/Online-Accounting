from django.shortcuts import render
from django.http import JsonResponse
from .models import Transaksi
from django.db.models import Sum

def dashboard_view(request):
    return render(request, 'dashboard.html')

def api_data_keuangan(request):
    # Mengambil data transaksi dan mengelompokkannya berdasarkan jenis untuk grafik
    data = list(Transaksi.objects.values('tanggal', 'jenis', 'jumlah'))
    
    # Alternatif: Ringkasan untuk Donut Chart (Pemasukan vs Pengeluaran)
    ringkasan = list(
        Transaksi.objects.values('jenis')
        .annotate(total=Sum('jumlah'))
    )
    
    return JsonResponse({
        'transaksi': data,
        'ringkasan': ringkasan
    }, safe=False)
