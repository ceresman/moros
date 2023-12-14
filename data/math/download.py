# Copyright 2023 undefined
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import re
import requests
from bs4 import BeautifulSoup

url = "https://web.evanchen.cc/problems.html"

# 发送请求并获取网页内容
response = requests.get(url)
content = response.text

# 使用BeautifulSoup解析网页内容
soup = BeautifulSoup(content, "html.parser")

# 查找所有的.tex文件链接
tex_links = soup.find_all("a", href=re.compile(r"\.pdf$"))

# 创建一个文件夹来存储下载的.tex文件
if not os.path.exists("pdf_files"):
    os.makedirs("pdf_files")

# 下载并保存.tex文件
for link in tex_links:
    tex_url = link["href"]
    tex_name = link["href"].split("/")[-1]
    tex_path = os.path.join("pdf_files", tex_name)
    print("download url ",tex_url)

    print(f"Downloading {tex_name}...")

    with requests.get(tex_url, stream=True) as tex_response:
        tex_response.raise_for_status()

        with open(tex_path, "wb") as tex_file:
            for chunk in tex_response.iter_content(chunk_size=8192):
                tex_file.write(chunk)

print("All .tex files have been downloaded.")