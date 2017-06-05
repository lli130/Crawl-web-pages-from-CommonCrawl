## Common-Crawl
### Objective
This repository is to retrieve text data of web pages from Common Crawl.
### Procedures 
1. Predefine:
- Define the number of index  
Currently available index collections are listed: [CommonCrawl_Index Collections](http://index.commoncrawl.org/). It will be upodated periodically.
- Define targeting domains
2. Settle down Python environment
- [Python environment](https://github.com/lli130/Tensor-Flow)
- [git clone crawl functions](https://github.com/lli130/Common-Crawl/tree/cdx-index-client)
3. Fetch URL from specific domains  
- [Fetch URL][https://github.com/lli130/Common-Crawl/blob/master/url_fetch.py]  
4. Process URL to get WET text data of web pages  
- [Process URL][https://github.com/lli130/Common-Crawl/blob/master/url_processing.py]  
- [Prepare WET path][https://github.com/lli130/Common-Crawl/blob/master/warc3.py]
5. Access to WET through WET path  
- [Download WGET][https://github.com/lli130/Common-Crawl/blob/master/wget64.exe]
- Access to WET: 
> path.wget.exe https://commoncrawl.s3.amazonaws.com/crawl-data/CC-MAIN-2016-50/segments/1480698542112.77/wet/CC-MAIN-20161202170902-00193-ip-10-31-129-80.ec2.internal.warc.wet.gz

### Findings
1. CommonCrawl updates indexing periodically  
2. WARC file stores metadata of target URL  
```  
{"urlkey": "org,un)/", "timestamp": "20161205025237", "status": "200", "url": "http://www.un.org",  
"filename": "crawl-data/CC-MAIN-2016-50/segments/1480698541518.17/warc/CC-MAIN-20161202170901-00503-ip-10-31-129-80.ec2.internal.warc.gz",  
"length": "2792", "mime": "text/html", "offset": "779704853", "digest": "IEMMH3LZKDO23GHYNHH4B3WYZPBDIL3U"}  
```
3. WET file stores text data of multiple URL besides targeting URL. However, it includes many irrelevant ones  
- metadata:  
```  
WARC/1.0 WARC-Type: conversion WARC-Target-URI: http://www.2159.go.jp/info/nichiendo/nichiendo.html  
WARC-Date: 2016-12-04T18:24:03Z WARC-Record-ID: <urn:uuid:2912374a-6c73-4702-aeb0-3b49a8d96616>  
WARC-Refers-To: <urn:uuid:e9b751a2-3542-42e1-acb5-067df0479346>  
WARC-Block-Digest: sha1:OYHU2OKNVIZDCVT3KYAPA6KMR3IKHLKR  
Content-Type: text/plainContent-Length: 1733  
``` 
- main content: includes title, body, foot and excludes hyperlinks  
```  
【新潟国道事務所】日本海沿岸東北道　村上都市計画道路　朝日山北幹線道路　都市計画と環境影響評価に関する手続きを行いました。日本海沿岸東北道　 
村上都市計画道路　朝日山北幹線道路　都市計画と環境影響評価に関する手続きを行いました。みちナビ新潟TOP　＞　 
都市計画と環境影響評価に関する手続きを行いました。参考（記者発表資料）平成24年7月27日：※新潟県側、山形県側　同時記者発表日本海沿岸東北自動車道  
（朝日〜温海）都市計画決定に向けて関係機関との協議に着手します。（PDF：368KB）平成24年8月8日：「日本海沿岸東北道　環境影響評価検討委員会」  
を開催します。 (PDF:0.3MB) 平成24年8月30日：新潟県側　「都市計画に関する説明会」を開催します。 (PDF：0.1MB)山形県側　都市計画手続きに関する  
説明会について（PDF：697KB)平成24年12月19日「第２回 日本海沿岸東北道 環境影響評価検討委員会」を開催します。(PDF：1.0MB)平成25年01月10日新  
潟県都市計画審議会　平成24年度開催状況（新潟県ホームページ）平成25年01月18日環境影響評価書を公表します。(PDF：1.0MB)お問い合わせ先国土交通省   
北陸地方整備局 新潟国道事務所 計画課　TEL.025-246-7775　FAX.025-246-7763新潟県 土木部 都市局 都市政策課　TEL.025-280-5429　FAX.025-285-0624  
新潟県 土木部 道路建設課 高規格道路推進室　TEL.025-280-5845　FAX.025-285-6225村上市 都市整備課 計画室　TEL.0254-53-2111　FAX.0254-53-3840  
```


