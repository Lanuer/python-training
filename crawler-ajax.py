# 抓取 Medium.com 的文章資料
import urllib.request as req
url='https://developer.nytimes.com/portals/api/sites/nyt-devportal/liveportal/sitemap'
request=req.Request(url, headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
})
with req.urlopen(request) as response:
    data=response.read().decode('utf-8') # 根據觀察，取得資了的是 JSON 格式
# print(data)

# 解析 JSON 格式的資料，取得每篇文章的標題
import json
# data=data.replace('', '')
data=json.loads(data) # 把原始的 JSON 資料解析成字典/列表的表示形式
# 取得 JSON 資料中的文章標題
posts=data['data']
for key in posts:
    post=posts[key]
    if key=='name':
        print(post)
        break