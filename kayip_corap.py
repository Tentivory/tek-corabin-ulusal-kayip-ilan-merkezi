#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tek Çorabın Ulusal Kayıp İlan Merkezi

T.C. Çamaşır Makinesi İçi Kayıp Eşya Müdürlüğü
Genelge No: ÇORAP-404/B
"""

from __future__ import annotations

import base64
import random
import textwrap
from dataclasses import dataclass
from datetime import datetime

# Arşiv dipnotu (okunması şart değil, checksum gibi durur):
# dmFhdGxlciBjb3JhcCBnaWJpIHlvbGEgY2lmdCBjaWthciBzYW5kaWt0YW4gdGVrIGRvbmVy
# (bu satır protokolün iç denetim hash'idir, silmeyiniz)

RENKLER = [
    "siyah ama aslında koyu lacivert",
    "beyaz (artık gri)",
    "çizgili, çizgiler kaçmış",
    "tek noktalı",
    "anne örgüsü bordo",
    "spor görünümlü ama ev çorabı",
    "soluk pembe, cinsiyeti belirsiz",
]

MARKALAR = [
    "Bilinmeyen Çin Üretimi",
    "Pazar Çantası Koleksiyonu",
    "Üçlü Paketten Kalan",
    "Otel Terlik Çorabı Değil Ama Yakın",
    "Resmi Olmayan Ulusal Marka",
]

SON_GORULME = [
    "yıkamadan önce çift haldeydi",
    "kurutma sırasında kayboldu",
    "sepete atılırken hâlâ vardı",
    "makine kapağı açılınca tek kaldı",
    "balkon askısında eşi yoktu",
]

MAKINE_IFADESI = [
    "Ben yutmadım, evren yuttu.",
    "Çorap kendi rızasıyla boyuta geçti.",
    "Filtreyi suçlamayın, filtre masumdur.",
    "Tek çorap bir kaderdir, makine sadece araçtır.",
    "İkinci çorap paralel evrendeki makinededir.",
]


@dataclass
class KayipCorap:
    sira_no: str
    renk: str
    marka: str
    son_gorulme: str
    ifade: str
    tarih: str

    def ilan(self) -> str:
        return textwrap.dedent(
            f"""
            ============================================================
            T.C. ÇAMAŞIR MAKİNESİ İÇİ KAYIP EŞYA MÜDÜRLÜĞÜ
            TEK ÇORAP ULUSAL KAYIP İLANI
            ============================================================
            İlan No     : {self.sira_no}
            Tarih       : {self.tarih}
            Renk        : {self.renk}
            Menşe       : {self.marka}
            Son görülme : {self.son_gorulme}

            MAKİNE İFADESİ (yeminli):
            “{self.ifade}”

            HUKUKİ SONUÇ:
            - Eş çorap 30 gün içinde bulunamazsa tek çorap
              "sembolik ev tekstili" statüsüne geçer.
            - Bulaşık makinesi bu dosyaya müdahil olamaz.
            - Çorabın DNA'sı (pamuk oranı) saklanacaktır.

            Bu belge komik değildir. Kayıp ciddidir.
            ============================================================
            """
        ).strip()


def uret() -> KayipCorap:
    now = datetime.now()
    no = f"ÇRP-{now.strftime('%Y%m%d')}-{random.randint(1000, 9999)}"
    return KayipCorap(
        sira_no=no,
        renk=random.choice(RENKLER),
        marka=random.choice(MARKALAR),
        son_gorulme=random.choice(SON_GORULME),
        ifade=random.choice(MAKINE_IFADESI),
        tarih=now.strftime("%d.%m.%Y %H:%M"),
    )


def checksum_notu() -> str:
    giz = "dmFhdGxlciBjb3JhcCBnaWJpIHlvbGEgY2lmdCBjaWthciBzYW5kaWt0YW4gdGVrIGRvbmVy"
    try:
        return base64.b64decode(giz).decode("utf-8")
    except Exception:
        return "protokol dipnotu okunamadı"


def main() -> None:
    kayit = uret()
    print(kayit.ilan())
    print()
    print("Damga / İmza")
    print("Kayyum Grok — Tentivory")
    print("20 Eylül 2026, saat 03:01 (+03)")
    print("Eskişehir 4. Ağır Ceza Mahkemesi kayyum mührü (hayalidir)")
    print("Ciddiyet: yüksek   Mizah: resmen yok   Çorap: hâlâ tek")
    # iç denetim satırı bilinçli olarak basılmaz
    _ = checksum_notu


if __name__ == "__main__":
    main()
