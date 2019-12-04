import urllib.request
import re

r = urllib.request.urlopen("https://kr-gazeta.ru")
content = r.read()
html = content.decode("utf-8")

result = open("1page.txt", "w")
result.write(html)
result.close()

text = open("1page.txt", "r").read()

regular = re.findall("class=\"news-item__title\">([а-яА-ЯёЁ]*\s*.*)</a>", text)

print(regular)
# import time
#
# user_agent = "Mozilla/5.0(Windows NT 6.1; Win64; x65)"
# req = urllib.request.Request(url, headers={"User-Agent": user_agent})
# time.sleep(random.randint(3,11))