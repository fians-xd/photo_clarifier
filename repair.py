import os
import time
import replicate
import requests
import shutil
from tqdm import tqdm
from collections.abc import MutableMapping

# Warna
hg = ('\x1b[0;32m') # hijau gelap
ht = ('\x1b[32;1m') # hijau terang
b  = ('\x1b[0;36m') # biru gelap
bt = ('\x1b[36;1m') # biru terang
m  = ('\x1b[31;1m') # merah
p  = ('\x1b[37;1m') # putih
h  = ('\x1b[30;1m') # hitam
k  = ('\x1b[33;1m') # kuning
kt = ('\x1b[1;33m') # kuning terang
pg = ('\x1b[00m')   # putih gelap

# logo
___logo___ = (f"""
 {bt}██▀███  {hg}▓{bt}█████  ██▓{bt}███   {bt}▄▄▄       ██{hg}▓ {bt}██▀███      ██▓███   ██{hg}░ {bt}██  {hg}▒{bt}█████  ▄▄▄█████{hg}▓ ▒{bt}█████    ██████{hg} 
{ht}▓{bt}██ {hg}▒ {bt}██{hg}▒▓{bt}█   ▀ {hg}▓{bt}██{hg}░  {bt}██{hg}▒▒{bt}████▄    {hg}▓{bt}██{hg}▒▓{bt}██ {hg}▒ {bt}██{hg}▒   ▓{bt}██{hg}░  {bt}██{hg}▒▓{bt}██{hg}░ {bt}██{hg}▒▒{bt}██{hg}▒  {bt}██{hg}▒▓  {bt}██{hg}▒ ▓▒▒{bt}██{hg}▒  {bt}██{hg}▒▒{bt}██    {hg}▒{bt} 
{ht}▓{bt}██ {hg}░{bt}▄█ {hg}▒▒{bt}███   {hg}▓{bt}██{hg}░ {bt}██{hg}▓▒▒{bt}██  ▀█▄  {hg}▒{bt}██{hg}▒▓{bt}██ {hg}░{bt}▄█ {hg}▒   ▓{bt}██{hg}░ {bt}██{hg}▓▒▒{bt}██▀▀██{hg}░▒{bt}██{hg}░  {bt}██{hg}▒▒ ▓{bt}██{hg}░ ▒░▒{bt}██{hg}░  {bt}██{hg}▒░ ▓{bt}██▄   
{ht}▒{bt}██▀▀█▄  {hg}▒{bt}▓█  ▄ {hg}▒{bt}██▄█{hg}▓▒ ▒░{bt}██▄▄▄▄██ {hg}░{bt}██{hg}░▒{bt}██▀▀█▄     {hg}▒{bt}██▄█{hg}▓▒ ▒░▓{bt}█ {hg}░{bt}██ {hg}▒{bt}██   ██{hg}░░ ▓{bt}██{hg}▓ ░ ▒{bt}██   ██{hg}░  ▒   {bt}██{hg}▒
{ht}░{bt}██{hg}▓ ▒{bt}██{hg}▒░{bt}▒████{hg}▒▒{bt}██{hg}▒ ░  ░ ▓{bt}█   {hg}▓{bt}██{hg}▒░{bt}██{hg}░░{bt}██{hg}▓ ▒{bt}██{hg}▒   ▒{bt}██{hg}▒ ░  ░░▓{bt}█{hg}▒░{bt}██{hg}▓░ {bt}████{hg}▓▒░  ▒{bt}██{hg}▒ ░ ░ {bt}████{hg}▓▒░▒{bt}██████{hg}▒▒
{hg}░ ▒▓ ░▒▓░░░ ▒░ ░▒▓▒░ ░  ░ ▒▒   ▓▒{bt}█{hg}░░▓  ░ ▒▓ ░▒▓░   ▒▓▒░ ░  ░ ▒ ░░▒░▒░ ▒░▒░▒░   ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
  {hg}░▒ ░ ▒░ ░ ░  ░░▒ ░       ▒   ▒▒ ░ ▒ ░  ░▒ ░ ▒░   ░▒ ░      ▒ ░▒░ ░  ░ ▒ ▒░     ░      ░ ▒ ▒░ ░ ░▒  ░ ░
  {hg}░░   ░    ░   ░░         ░   ▒    ▒ ░  ░░   ░    ░░        ░  ░░ ░░ ░ ░ ▒    ░      ░ ░ ░ ▒  ░  ░  ░
   {hg}░        ░  ░               ░  ░ ░     ░                  ░  ░  ░    ░ ░               ░ ░        ░

	     {k}^ ^			{bt}-{k}={m}[ {ht}Author Script {m}]{k}={bt}-		                {k}^ ^
	    ({m}O{bt},{m}O{k})                      {bt}-{k}={m}[ {ht}Sofian Nasution {m}]{k}={bt}-                         {k}({m}O{bt},{m}O{k})
	    (   ) {ht}Sistem ini digunakan untuk memperbaiki Foto yang kualitas nya rendah {k}(   )
	    {h}-{k}"{h}-{k}"{h}------------------------------------------------------------------------{k}"{h}-{k}"{h}-
{pg}""")

# Set token as environment variable
os.environ["REPLICATE_API_TOKEN"] = "r8_AvRLMaDO8J9YaUY8UzqzkFgdr74Cg9d3x4shx"

# Input path file
os.system("clear")
print(___logo___)
input_file_path = input(f"{hg}Masukan file fotomu lurd{k}:{pg} ")

# Run the model
print(f"\n{hg}Server sedang memproses, Seruput kopi dulu ngab jo lali ambekan...")
output = replicate.run(
    "xinntao/realesrgan:1b976a4d456ed9e4d1a846597b7614e79eadad3032e9124fa63859db0fd59b56",
    input={"img": open(input_file_path, "rb")}
)
print(f"{hg}Duarr rampung..{m}!!{pg}\n")

# Check the type of output
if isinstance(output, dict):
    output_url = output.get("output_url", "")
else:
    output_url = output

# Specify the output file name
output_file_name = input(f"{hg}Masukan nama file hasil{k}:{pg} ")

# Download the file
output_file_path = os.path.join(os.path.dirname(__file__), "hasil", output_file_name)
with requests.get(output_url, stream=True) as response, open(output_file_path, "wb") as f:
    response.raise_for_status()
    total_size = int(response.headers.get('Content-Length', 0))
    block_size = 1024
    progress_bar_format = "\x1b[0;32mAgi di download kie Sabar\x1b[33;1m: \x1b[36;1m{percentage:3.0f}%|{bar}| \x1b[0;32m{n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]"
    with tqdm(total=total_size, unit='iB', unit_scale=True, ncols=80, bar_format=progress_bar_format) as progress_bar:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            f.write(data)

print(f"\n{hg}File download selesai...{m}!!!\n")

# Print the output file path
print(f"{hg}Selamat kepo, jalur hasil{k}:{pg}", output_file_path)
