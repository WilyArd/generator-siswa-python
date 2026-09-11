"""
Package Generator Siswa untuk Format Sidigs Murid Dapodik Excel
"""

from generator.jenjang import JENJANG_CONFIG, normalize_jenjang
from generator.student import generate_single_student, generate_nik, clean_username
from generator.excel import generate_siswa_excel
from generator.cli import main, interactive_prompt

__all__ = [
    "JENJANG_CONFIG",
    "normalize_jenjang",
    "generate_single_student",
    "generate_nik",
    "clean_username",
    "generate_siswa_excel",
    "interactive_prompt",
    "main",
]
