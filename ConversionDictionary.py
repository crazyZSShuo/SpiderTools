import re

Str = '''
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cache-control: no-cache
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: same-origin
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36
'''
pattern = '^(.*?): (.*?)$'


def str_to_dict(str=None):
    if not str:
        str = Str
    for line in str.splitlines():
        print(re.sub(pattern, '\'\\1\':\'\\2\',', line).strip())


if __name__ == '__main__':
    str_to_dict()
