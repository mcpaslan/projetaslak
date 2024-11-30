import tkinter as tk
from tkinter import messagebox
from veri_yonetimi import VeriYonetimi
class Uygulama:
    def __init__(self, pencere):
        self.pencere = pencere
        self.veri_yonetimi = VeriYonetimi()

        self.pencere.title("Film/Dizi Yönetim Uygulaması")

        # Arayüz elemanlarını oluşturma
        self.gui_elemanlarini_olustur()

        # Listeyi güncelle
        self.listeyi_guncelle()

    def gui_elemanlarini_olustur(self):
        """GUI elemanlarını oluşturur."""
        # Ad
        tk.Label(self.pencere, text="Ad:").grid(row=0, column=0, sticky="e")
        self.ad_entry = tk.Entry(self.pencere, width=30)
        self.ad_entry.grid(row=0, column=1, padx=10, pady=5)

        # Tür
        tk.Label(self.pencere, text="Tür:").grid(row=1, column=0, sticky="e")
        self.tur_var = tk.StringVar(value="Film")
        self.tur_menu = tk.OptionMenu(self.pencere, self.tur_var, "Film", "Dizi")
        self.tur_menu.grid(row=1, column=1, padx=10, pady=5)

        # Durum
        tk.Label(self.pencere, text="Durum:").grid(row=2, column=0, sticky="e")
        self.durum_var = tk.StringVar(value="İzlenecek")
        self.durum_menu = tk.OptionMenu(self.pencere, self.durum_var, "İzlenecek", "İzlendi", "Bekleniyor")
        self.durum_menu.grid(row=2, column=1, padx=10, pady=5)

        # Yıldız
        tk.Label(self.pencere, text="Yıldız:").grid(row=3, column=0, sticky="e")
        self.yildiz_var = tk.StringVar(value="5")
        self.yildiz_menu = tk.OptionMenu(self.pencere, self.yildiz_var, "1", "2", "3", "4", "5")
        self.yildiz_menu.grid(row=3, column=1, padx=10, pady=5)

        # Notlar
        tk.Label(self.pencere, text="Notlar:").grid(row=4, column=0, sticky="ne")
        self.notlar_text = tk.Text(self.pencere, width=30, height=5)
        self.notlar_text.grid(row=4, column=1, padx=10, pady=5)

        # Liste
        tk.Label(self.pencere, text="Filmler/Diziler:").grid(row=0, column=2, sticky="w", padx=10)
        self.liste = tk.Listbox(self.pencere, width=50, height=15)
        self.liste.grid(row=1, column=2, rowspan=4, padx=10, pady=5)

        # Butonlar
        ekle_buton = tk.Button(self.pencere, text="Ekle", command=self.ekle)
        ekle_buton.grid(row=5, column=1, pady=10)

        sil_buton = tk.Button(self.pencere, text="Sil", command=self.sil)
        sil_buton.grid(row=6, column=1, pady=10)

    def listeyi_guncelle(self):
        """Film/Dizi listesini günceller."""
        self.liste.delete(0, tk.END)
        for i, veri in enumerate(self.veri_yonetimi.veriler):
            self.liste.insert(tk.END, f"{i + 1}. {veri['ad']} ({veri['durum']}, {veri['yildiz']} yıldız)")

    def ekle(self):
        """Yeni bir film veya dizi ekler."""
        ad = self.ad_entry.get()
        tur = self.tur_var.get()
        durum = self.durum_var.get()
        yildiz = self.yildiz_var.get()
        notlar = self.notlar_text.get("1.0", tk.END).strip()

        if not ad or not tur or not durum or not yildiz:
            messagebox.showwarning("Uyarı", "Tüm alanları doldurun!")
            return

        yeni_icerik = {
            "ad": ad,
            "tur": tur,
            "durum": durum,
            "yildiz": int(yildiz),
            "not": notlar,
        }
        self.veri_yonetimi.ekle(yeni_icerik)
        self.listeyi_guncelle()
        messagebox.showinfo("Başarılı", "Film/Dizi başarıyla eklendi!")

    def sil(self):
        """Seçilen filmi/diziyi siler."""
        secilen_index = self.liste.curselection()
        if not secilen_index:
            messagebox.showwarning("Uyarı", "Silmek için bir öğe seçin!")
            return

        index = secilen_index[0]
        self.veri_yonetimi.sil(index)
        self.listeyi_guncelle()
        messagebox.showinfo("Başarılı", "Film/Dizi başarıyla silindi!")
