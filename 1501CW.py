import urllib.request
import json
import re


# r = urllib.request.urlopen("https://api.vk.com/method/users.get?user_id=51934405&v=5.52&access_token=3c4bff72d3f985bf625a49d81787e645a72c2cc651f1626d16763cd8e811477fa905be72edc54a692fa3a")
# content = r.read().decode("utf-8")
# print(content) # 1. Получить ответ от API без ошибок

r = urllib.request.urlopen("https://api.vk.com/method/wall.getComments?params[post_id=24165]?user_id=-114039499&v=5.52&access_token=3c4bff72d3f985bf625a49d81787e645a72c2cc651f1626d16763cd8e811477fa905be72edc54a692fa3a")
content = r.read().decode("utf-8")

with open("com.json", "w") as fj:
    json.dump(content, fj, ensure_ascii=False, indent=2)

