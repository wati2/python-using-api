import os
import time
import hmac, hashlib
import urllib.parse
import urllib.request
import ssl
# venderId, accesskey, secretkey 파일(memo.py)로 따로 관리
import memo

# 테스트 완료 2020-06-07

os.environ['TZ'] = 'GMT+0'

datetime=time.strftime('%y%m%d')+'T'+time.strftime('%H%M%S')+'Z'
method = "GET"

vendorId = memo.vendorId
accesskey = memo.accesskey
secretkey = memo.secretkey

path = f"/v2/providers/openapi/apis/api/v4/vendors/{vendorId}/returnRequests"
query = urllib.parse.urlencode({"createdAtFrom": "2020-06-04", "createdAtTo": "2020-06-05", "status": "UC"})

message = datetime+method+path+query

signature=hmac.new(secretkey.encode('utf-8'),message.encode('utf-8'),hashlib.sha256).hexdigest()
authorization  = "CEA algorithm=HmacSHA256, access-key="+accesskey+", signed-date="+datetime+", signature="+signature

url = "https://api-gateway.coupang.com"+path+"?%s" % query

req = urllib.request.Request(url)
req.add_header("Content-type","application/json;charset=UTF-8")
req.add_header("Authorization",authorization)
req.add_header("X-EXTENDED-TIMEOUT", "20000")

req.get_method = lambda: method

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    resp = urllib.request.urlopen(req,context=ctx)
except urllib.request.HTTPError as e:
    print(e.code)
    print(e.reason)
    print(e.fp.read())
except urllib.request.URLError as e:
    print(e.errno)
    print(e.reason)
    # print(e.fp.read())
else:
    # 200
    body = resp.read().decode(resp.headers.get_content_charset())
    print(body)