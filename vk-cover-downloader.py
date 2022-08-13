import os
import wget

from requests_html import HTMLSession

os.system("")

link = input("Ссылка на трек, альбом или страницу исполнителя: ")

try:
	session = HTMLSession()
	session = session.get(link)

	if ("artist" in link):
		cover = (session.html.search("background-image: url('{}')")[0])
		wget.download(cover, "cover.png", bar=None)
		print("\033[92m" + "[+] Загрузка завершена")
	else:
		cover = (session.html.search("background-image:url('{}')")[0])
		wget.download(cover, "cover.png", bar=None)
		print("\033[92m" + "[+] Загрузка завершена")
except Exception as e:
	print("\033[91m" + "[!] Неправильная ссылка")