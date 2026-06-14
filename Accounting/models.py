from django.db import models

class Transaksi(models.Model):
    JENIS_PILIHAN = [
        ('masuk', 'Pemasukan'),
        ('keluar', 'Pengeluaran'),
    ]
    
    tanggal = models.DateField()
    keterangan = models.CharField(max_index=True, max_length=255)
    kategori = models.CharField(max_length=100)
    jenis = models.CharField(max_length=6, choices=JENIS_PILIHAN)
    jumlah = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.tanggal} | {self.jenis} - {self.keterangan}: Rp{self.jumlah}"
