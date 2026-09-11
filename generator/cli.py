"""
Modul penanganan antarmuka baris perintah (CLI) dan mode interaktif tanya jawab.
"""

import os
import argparse

from generator.jenjang import JENJANG_CONFIG, normalize_jenjang
from generator.excel import generate_siswa_excel


DEFAULT_EXPORT_DIR = "export_excel"


def resolve_output_path(filename_or_path: str, count: int = 1000) -> str:
    """
    Memastikan file output disimpan ke dalam folder 'export_excel' jika hanya berupa nama file,
    serta memastikan ekstensi '.xlsx' otomatis ditambahkan jika belum ada.
    """
    if not filename_or_path:
        filename_or_path = f"hasil_siswa_{count}.xlsx"
    else:
        filename_or_path = filename_or_path.strip()
        if not filename_or_path.lower().endswith((".xlsx", ".xls")):
            filename_or_path += ".xlsx"

    if os.path.dirname(filename_or_path) == "":
        return os.path.join(DEFAULT_EXPORT_DIR, filename_or_path)
    return filename_or_path


def interactive_prompt(default_template: str) -> dict:
    """
    Mode interaktif tanya-jawab jika script dijalankan tanpa argumen CLI.
    """
    print("=" * 65)
    print("   GENERATOR DATA SISWA FORMAT SIDIGS / MURID DAPODIK EXCEL")
    print("=" * 65)

    # 1. Jumlah siswa
    count_input = input(f"\n1. Masukkan jumlah siswa yang ingin digenerate [Default 1000]: ").strip()
    count = int(count_input) if count_input.isdigit() and int(count_input) > 0 else 1000

    # 2. Output filename
    default_out = f"hasil_siswa_{count}.xlsx"
    out_input = input(f"2. Nama file output Excel [Default: {default_out}] (tersimpan di folder '{DEFAULT_EXPORT_DIR}/'): ").strip()
    output_path = resolve_output_path(out_input, count)

    # 3. Jenjang sekolah
    print("\n3. Pilih Jenjang Sekolah:")
    print("   [1] SMA  - Sekolah Menengah Atas (Umur ~15-18 tahun) [Default]")
    print("   [2] SMK  - Sekolah Menengah Kejuruan (Jurusan: RPL, TKJ, AKL, DKV, dll.)")
    print("   [3] SMP  - Sekolah Menengah Pertama (Umur ~12-15 tahun)")
    print("   [4] SD   - Sekolah Dasar (Umur ~6-12 tahun)")
    print("   [5] TK   - TK / PAUD (Umur ~4-6 tahun)")
    print("   [6] MA   - Madrasah Aliyah (Umur ~15-18 tahun)")
    print("   [7] MTs  - Madrasah Tsanawiyah (Umur ~12-15 tahun)")
    print("   [8] MI   - Madrasah Ibtidaiyah (Umur ~6-12 tahun)")
    print("   [9] SLB  - Sekolah Luar Biasa (Disertai kebutuhan khusus)")
    level_choice = input("   Pilihan [1-9 atau ketik SMA/SMK/SMP/SD/TK/dll]: ").strip()
    choice_map = {
        "1": "SMA", "2": "SMK", "3": "SMP", "4": "SD", "5": "TK",
        "6": "MA", "7": "MTS", "8": "MI", "9": "SLB"
    }
    level = choice_map.get(level_choice, normalize_jenjang(level_choice))

    # 4. Mode pengisian
    print("\n4. Pilih Mode Pengisian Kolom:")
    print("   [1] Standar Template (Data utama + NIS & NISN terisi, kelas opsional) [Default]")
    print("   [2] Lengkap / Full   (Mengisi semua kolom termasuk Alamat, No KK, Fisik BB/TB, dsb.)")
    mode_choice = input("   Pilihan [1/2]: ").strip()
    mode = "full" if mode_choice == "2" else "standard"

    # 5. Kelas / Rombel spesifik
    rombel_input = input("\n5. Tentukan Kelas / Rombel? [OPSIONAL - Tekan ENTER untuk mengosongkan / ketik misal: X-A, X-B]: ").strip()
    rombel = rombel_input if rombel_input else None

    return {
        "template": default_template,
        "output": output_path,
        "count": count,
        "level": level,
        "mode": mode,
        "rombel": rombel,
        "seed": None
    }


def parse_args():
    """Mendefinisikan argumen baris perintah."""
    parser = argparse.ArgumentParser(
        description="Program pembuat (generator) data dummy siswa format Sidigs Murid-Dapodik Excel hingga 1000+ data."
    )
    parser.add_argument("-n", "--count", type=int, default=None, help="Jumlah siswa yang akan digenerate (contoh: 1000, 1500, 2000)")
    parser.add_argument("-t", "--template", type=str, default="format sidigs murid-dapodik.xlsx", help="Path file template Excel")
    parser.add_argument("-o", "--output", type=str, default=None, help="Nama/path file output Excel (otomatis ke folder 'export_excel/' jika hanya nama file)")
    parser.add_argument("-l", "--level", "--jenjang", type=str, default="SMA", help="Jenjang sekolah: SMA, SMK, SMP, SD, TK, PAUD, MA, MTS, MI, SLB (default: SMA)")
    parser.add_argument("-m", "--mode", type=str, choices=["standard", "full"], default="standard", help="Mode pengisian: 'standard' (persis sample template) atau 'full' (lengkap termasuk Alamat, No KK, dsb.)")
    parser.add_argument("-r", "--rombel", "--kelas", type=str, default=None, dest="rombel", help="Tentukan nama kelas/rombel (opsional, contoh: 'X-A' atau 'XII TKJ 1' atau 'X-1, X-2')")
    parser.add_argument("-s", "--seed", type=int, default=None, help="Random seed untuk hasil yang deterministik")
    return parser.parse_args()


def main():
    """Fungsi utama eksekusi program."""
    args = parse_args()

    # Jika tidak ada parameter jumlah atau output yang diberikan, jalankan mode interaktif
    if args.count is None and args.output is None:
        params = interactive_prompt(args.template)
    else:
        count = args.count if args.count is not None else 1000
        output = resolve_output_path(args.output, count)
        params = {
            "template": args.template,
            "output": output,
            "count": count,
            "level": normalize_jenjang(args.level),
            "mode": args.mode,
            "rombel": args.rombel,
            "seed": args.seed
        }

    out_file = generate_siswa_excel(
        template_path=params["template"],
        output_path=params["output"],
        count=params["count"],
        level=params["level"],
        mode=params["mode"],
        rombel=params["rombel"],
        seed=params["seed"]
    )

    cfg = JENJANG_CONFIG.get(normalize_jenjang(params["level"]), JENJANG_CONFIG["SMA"])
    print("\n" + "=" * 65)
    print("   RINGKASAN DATA YANG BERHASIL DIGENERATE")
    print("=" * 65)
    print(f"File Output : {os.path.abspath(out_file)}")
    print(f"Jumlah Siswa: {params['count']:,}")
    print(f"Jenjang     : {cfg['nama']}")
    print(f"Mode        : {params['mode'].upper()}")
    if params.get('rombel'):
        print(f"Kelas/Rombel: {params['rombel']}")
    print("=" * 65 + "\n")
