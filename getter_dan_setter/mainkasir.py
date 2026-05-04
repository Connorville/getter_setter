from sistem_kasir import Produk, Keranjang

p1 = Produk("Kopi Kenangan", 25000, 40)
p2 = Produk("Susu UHT", 18000, 20)
p3 = Produk("Keyboard Gaming", 250000, 80)

keranjang_saya = Keranjang()

keranjang_saya.set_member(False)

keranjang_saya.tambah_produk(p1, 7)
keranjang_saya.tambah_produk(p2, 6)
keranjang_saya.tambah_produk(p3, 4)

keranjang_saya.bayar(500000)