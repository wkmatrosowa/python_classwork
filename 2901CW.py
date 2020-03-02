#"6634ed7e6634ed7e6634ed7ef0665bcc3a666346634ed7e382bd58b71deaef09756266b"

import urllib.request
import json
import re

r = urllib.request.urlopen("https://api.vk.com/method/wall.get?owner_id=-31480508&count=100&v=5.52&access_token=aec0e590aec0e590aec0e59043aeafc4d4aaec0aec0e590f0f1216e5ff98f31238f5d80")
content = r.read().decode("utf-8")

with open("posts.json", "w") as fj:
    json.dump(content, fj, ensure_ascii=False, indent=3)

