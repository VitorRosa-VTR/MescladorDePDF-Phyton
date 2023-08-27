import PyPDF2
import os

merger = PyPDF2.PdfMerger()

lista_arquivos = os.listdir("arquivos_para_mesclar")
lista_arquivos.sort()
print(lista_arquivos)

for arquivo in lista_arquivos:
    if ".pdf" in arquivos_para_mesclar:
        merger.append(f"arquivos_para_mesclar/{arquivo}")

merger.write("PDF Final.pdf")