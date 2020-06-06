import os
import time
import hmac, hashlib
import urllib.parse
import urllib.request
import ssl
# venderId, accesskey, secretkey 파일(memo.py)로 따로 관리
import memo

os.environ['TZ'] = 'GMT+0'

datetime=time.strftime('%y%m%d')+'T'+time.strftime('%H%M%S')+'Z'
method = "GET"
#replace with your own vendorId
vendorId = memo.vendorId
accesskey = memo.accesskey
secretkey = memo.secretkey

path = "/v2/providers/openapi/apis/api/v4/vendors/" + vendorId + "/returnRequests"
query = urllib.parse.urlencode({"createdAtFrom": "2018-08-08", "createdAtTo": "2018-08-08", "status": "UC"})

message = datetime+method+path+query


signature=hmac.new(secretkey.encode('utf-8'),message.encode('utf-8'),hashlib.sha256).hexdigest()

authorization  = "CEA algorithm=HmacSHA256, access-key="+accesskey+", signed-date="+datetime+", signature="+signature
#print(authorization)

# ************* SEND THE REQUEST *************
url = "https://api-gateway.coupang.com"+path+"?%s" % query

print('BEGIN REQUEST++++++++++++++++++++++++++++++++++++')
req = urllib.request.Request(url)
#print(req)

req.add_header("Content-type","application/json;charset=UTF-8")
req.add_header("Authorization",authorization)

req.get_method = lambda: method

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print(req.get_full_url())
print(req.get_header("Content-type"))
print(req.get_header("Authorization"))
print(req.get_method())

print('RESPONSE++++++++++++++++++++++++++++++++++++')
#resp = urllib.request.urlopen(req)

try:
    resp = urllib.request.urlopen(req,context=ctx)
except urllib.request.HTTPError as e:
    if e.code == 404:
        print("404")
    else:
        print("NOT 404")
except urllib.request.URLError as e:
    print(e.errno)
else:
    # 200
    body = resp.read().decode(resp.headers.get_content_charset())
    print(body)