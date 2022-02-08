import json
from urllib import parse
from wsgiref.simple_server import make_server
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tbp.v20190627 import tbp_client, models

def hello_world_app(environ, start_response):
    # j = json.loads(environ)
    # print("------",environ['wsgi.input'])

    try:
        request_body_size = int(environ.get('CONTENT_LENGTH',0))
    except(ValueError):
        request_body_size = 0 

    request_body = environ['wsgi.input'].read(request_body_size)    
    d = json.loads(request_body)
    keyword = d["keyword"]
    res = robot(keyword)
    status = '200 OK'  # HTTP Status
    headers = [('Content-type', 'text/plain; charset=utf-8')]  # HTTP Headers
    start_response(status, headers)
  
    msg = res
    return [msg.encode('utf8')]

def robot(str):
    try:
        cred = credential.Credential("your appId", "your appKey")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "tbp.tencentcloudapi.com"
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        
        client = tbp_client.TbpClient(cred, "",clientProfile)

        req = models.TextProcessRequest()
        params = {
            "Action":"TextProcess",
            "Version":"2019-06-27",
            "BotId": "your BotId",
            "BotEnv": "release",
            "TerminalId": "0001",
            "InputText": str
        }
        req.from_json_string(json.dumps(params))
        resp = client.TextProcess(req)
        # print('11111',resp)
        jsonTxt = json.loads(resp.to_json_string())
        arr = jsonTxt['ResponseMessage']['GroupList']
        res = arr[0]['Content']
        return res
      
    except TencentCloudSDKException as err:
        print(err)

with make_server('127.0.0.1', 5678, hello_world_app) as httpd:
    # print("Serving on port 5678...")
    httpd.serve_forever()
