import os
rootdir = r'C:/Users/xiaoji/Desktop/result/result1'

for a,b,filenames in os.walk(rootdir):
    tk = r'domain-go.jp'
    for filename in filenames:
        if filename.find(tk)==-1:
            filenames.remove(filename)

for filename in filenames:
    fname = rootdir+r'/'+filename
    f = open(fname,'r+')
    data = f.read()
    f.close()
    data = data.replace(r'/warc/',r'/wet/')
    data = data.replace(r'.warc.gz','.warc.wet.gz')
    data = data.replace(r'crawl-data' , 'https://commoncrawl.s3.amazonaws.com/crawl-data')
    f = open(fname,'w+')
    f.write(data)
    f.close()
