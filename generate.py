import json
import urllib.request

OWNER = "varlie9-spec"
REPO = "Delta-lama"

url = f"https://api.github.com/repos/{OWNER}/{REPO}/releases/latest"

req = urllib.request.Request(
    url,
    headers={"User-Agent":"GitHub Action"}
)

response = urllib.request.urlopen(req)

release = json.loads(response.read())

cards=""

for asset in release["assets"]:

    if asset["name"].lower().endswith(".apk"):

        size = round(asset["size"]/1024/1024,2)

        cards += f"""
<div class="card">

<h2>📦 {asset['name']}</h2>

<p>Ukuran : {size} MB</p>

<a class="btn"
href="{asset['browser_download_url']}">
DOWNLOAD
</a>

</div>
"""

html=f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="utf-8">

<title>Delta APK</title>

<style>

body{{
background:#0d1117;
font-family:Arial;
color:white;
padding:30px;
}}

h1{{
text-align:center;
}}

.card{{
background:#161b22;
padding:20px;
border-radius:12px;
margin:15px auto;
max-width:700px;
border:1px solid #30363d;
}}

.btn{{
display:inline-block;
margin-top:10px;
padding:10px 20px;
background:#2ea043;
color:white;
text-decoration:none;
border-radius:8px;
font-weight:bold;
}}

</style>

</head>

<body>

<h1>📦 Delta APK Download</h1>

{cards}

</body>

</html>
"""

with open("index.html","w",encoding="utf8") as f:
    f.write(html)

print("index.html berhasil dibuat")
