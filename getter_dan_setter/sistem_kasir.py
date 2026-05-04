class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.__id = 0
    
    @property
    def id(self):
        return self.__id


    @id.setter
    def id(self, id_barang):
        if id_barang != 0:
            self.__id = id_barang


class Keranjang:
    def __init__(self):
        self.daftar_barang = [] 
        self.member = False

    def set_member(self, status):
        self.member = status

    def tambah_produk(self, produk_baru, jumlah):
        if jumlah > produk_baru.stok:
            print(f"Stok {produk_baru.nama} tidak cukup! Sisa: {produk_baru.stok}")
            return
        
        produk_baru.stok -= jumlah
        self.daftar_barang.append({
            "produk": produk_baru,
            "jumlah": jumlah
        })
        
        print(f"Berhasil menambah: {produk_baru.nama} x{jumlah}")

    def hapus_produk(self, nama_produk):
        for barang in self.daftar_barang:
            if barang["produk"].nama == nama_produk:
                
                barang["produk"].stok += barang["jumlah"]
                self.daftar_barang.remove(barang)
                print(f"{nama_produk} dihapus dari keranjang")
                return
        print("Produk tidak ditemukan")

    def hitung_total(self):
        total = 0
        for barang in self.daftar_barang:
            total += barang["produk"].harga * barang["jumlah"]
        return total

    def cetak_struk(self):
        print("\n=== Struk Belanja ===")
        for barang in self.daftar_barang:
            p = barang["produk"]
            j = barang["jumlah"]
            print(f"- {p.nama} x{j} : Rp{p.harga * j}")

        total = self.hitung_total()

        
        if total > 100000:
            diskon = total * 0.1
            print(f"Diskon (10%) \t: -Rp{diskon}")
            total -= diskon

        
        if self.member:
            diskon_member = total * 0.05
            print(f"Diskon Member (5%) : -Rp{diskon_member}")
            total -= diskon_member

        
        pajak = total * 0.11
        print(f"PPN (11%) \t: +Rp{pajak}")
        total += pajak

        print(f"Total Akhir \t: Rp{total}")
        return total

    def bayar(self, uang_terima):
        total = self.cetak_struk()
        
        print(f"\nUang diterima : Rp{uang_terima}")
        
        if uang_terima < total:
            print("Uang tidak cukup!")
        else:
            kembalian = uang_terima - total
            print(f"Kembalian \t: Rp{kembalian}")