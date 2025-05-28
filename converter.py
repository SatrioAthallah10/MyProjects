import argparse
import os
from docx2pdf import convert

def konvert(input_file_path, output_file_path=None):
    if not os.path.exists(input_file_path):
        print(f"File tidak ditemukan di '{input_file_path}'")
        return
    
    if output_file_path is None:
        base_name = os.path.splitext(input_file_path)[0]
        output_file_path = base_name + ".pdf"

        output_direktori = os.path.dirname(output_file_path)
        if output_direktori and not os.path.exists(output_direktori):
            try:
                os.makedirs(output_direktori)
                print(f"File berhasil dikonversi: '{output_direktori}'")
            except OSError as e:
                print(f"Error saat membuat file '{output_direktori}': {e}")
                return
            
        print(f"Loading: '{input_file_path}' -> '{output_file_path}'")

        try:
            convert(input_file_path, output_file_path)
            print(f"konversi berhasil! File disimpan di: '{output_file_path}'")
        except Exception as e:
            print(f"Error selama proses konversi: {e}")

if __name__ == "__main__":
    proses1 = argparse.ArgumentParser(description="Konversi file word ke PDF")

    proses1.add_argument("input_file", help="Path ke file yang akan dikonversi")

    proses1.add_argument("-o", "--output_file", help="Path untuk menyimpan file yang sudah dikonversi", default=None)

    proses2 = proses1.parse_args()

    konvert(proses2.input_file, proses2.output_file)