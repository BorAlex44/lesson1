import re
import requests

reg_str = re.compile(r'((?:[0-9]{,3}[.]){3}[0-9]{,3}) - - '
                     r'(.[0-9]{,2}/\w+/[0-9]{4}:(?:[0-9]{2}:){2}[0-9]{2} \+[0-9]{4}]) .(\w+) '
                     r'([/\w+]{0,}) (?:[^\"]*)\" ([0-9]+) ([0-9]+)')
url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
content = requests.get(url).text
for arg in reg_str.findall(content):
    adr, datetime, r_type, resourse, code, size = arg
    print(adr, datetime, r_type, resourse, code, size)
