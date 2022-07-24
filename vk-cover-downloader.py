from requests_html import HTMLSession
import wget
from sys import platform
import ctypes

link = input("Введите ссылку на трек или альбом: ")

if platform[0:3].lower() == "win":
	kernel32 = ctypes.windll.kernel32
	kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

try:
	session = HTMLSession()
	session = session.get(link)
	cover = (session.html.search("background-image:url('{}')")[0])
	wget.download(cover, "cover.png", bar=None)
	print("\033[92m" + "[+] Загрузка завершена")
except Exception:
	print("\033[91m" + "[!] Неправильная ссылка")