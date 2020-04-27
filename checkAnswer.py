import requests

'''
查答案

args topic: 传入题目关键词，查找答案
'''
def checkAnswer(topic):
    headers = {
         'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 9; COR-AL10 Build/HUAWEICOR-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.111 Mobile Safari/537.36 MMWEBID/8547 MicroMessenger/7.0.13.1640(0x27000D39) Process/tools NetType/WIFI Language/zh_CN ABI/arm64 WeChat/arm64',
        'X-Requested-With': 'com.tencent.mm',
        'Referer': 'https://xuexi1905.cn/?code=061FufZG1tysc30KzWZG1Sg1ZG1FufZ-&state=',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImNrOWg3cXB2dzJpZDYwODE5dmpubGZscG8iLCJpYXQiOjE1ODc5NTM5MTYsImV4cCI6MTU4ODEyNjcxNn0.gOFfodiNrXzasqYiTErVjy-fQBf5FppkWL6MO4ypByU',
        'Origin': 'https://xuexi1905.cn',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'Connection': 'keep-alive',
        'Host': 'api.deeract.com'
    }

    res = requests.get('https://api.deeract.com/l2s/api/questions?keyword='+topic, headers=headers)
    i = 1
    for line in res.json():
        print('{}、{}'.format(str(i), line['title']))
        i += 1

if __name__ == '__main__':
    print('-'*50)
    print('|'+(' '*48)+'|')
    print('|    name：强国-挑战答题-查答案                  |')
    print('|    author：lonely                              |')
    print('|'+(' '*48)+'|')
    print('-'*50)
    print('\n'+'-'*80+'\n')
    
    while True:
        kw = input('直接输入任意词组作为关键词，2-4字即可，输入q可退出：')
        if kw == 'q':
            break
            
        checkAnswer(kw)
        print('-'*50)
    
