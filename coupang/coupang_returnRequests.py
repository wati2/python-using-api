# 쿠팡 반품요청 단건 조회
# method: GET
# path: /v2/providers/openapi/apis/api/v4/vendors/{vendorId}/returnRequests/{receiptId}

# 요청 파라미터
# vendorId	O	 String	
# 판매자 ID
# receiptId	O	 Number	
# 취소(반품)접수번호
# ReceiptId는 반품요청 목록 조회API를 통해 확인가능합니다.
# ReceiptId는 반드시 number타입이어야 합니다.

import os
import time
import hmac, hashlib
import urllib.parse
import urllib.request
import ssl
import json
# venderId, accesskey, secretkey 파일(memo.py)로 따로 관리
import memo

# 현재경로
currentDirectory = os.getcwd()
file_path = currentDirectory + "\\result.json"



os.environ['TZ'] = 'GMT+0'

datetime=time.strftime('%y%m%d')+'T'+time.strftime('%H%M%S')+'Z'
method = "GET"
accesskey = memo.accesskey
secretkey = memo.secretkey
vendorId = memo.vendorId
receiptId = memo.receiptId

path = f"/v2/providers/openapi/apis/api/v4/vendors/{vendorId}/returnRequests/{receiptId}"
query = urllib.parse.urlencode({})

# HMAC 
message = datetime+method+path+query
signature=hmac.new(secretkey.encode('utf-8'),message.encode('utf-8'),hashlib.sha256).hexdigest()
authorization  = "CEA algorithm=HmacSHA256, access-key="+accesskey+", signed-date="+datetime+", signature="+signature

# RequestUrl
url = "https://api-gateway.coupang.com"+path

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

    # with open(file_path, 'w', encoding='utf-8') as outfile:
    #     json.dump(body, outfile, indent=4, ensure_ascii=False)