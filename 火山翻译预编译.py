import json,time

from volcengine.ApiInfo import ApiInfo
from volcengine.Credentials import Credentials
from volcengine.ServiceInfo import ServiceInfo
from volcengine.base.Service import Service

#火山翻译
def huoshan_trans(text,to):
    k_access_key = 'abcd1234' # https://console.volcengine.com/iam/keymanage/
    k_secret_key = 'abcd1234'
    k_service_info = \
        ServiceInfo('open.volcengineapi.com',
                    {'Content-Type': 'application/json'},
                    Credentials(k_access_key, k_secret_key, 'translate', 'cn-north-1'),
                    30,
                    30)
    k_query = {
        'Action': 'TranslateText',
        'Version': '2020-06-01'
    }
    k_api_info = {
        'translate': ApiInfo('POST', '/', k_query, {}, {})
    }
    service = Service(k_service_info, k_api_info)
    body = {
        'TargetLanguage': to,
        'TextList': [text],
    }
    res = service.json('translate', {}, json.dumps(body))
    # print(json.loads(res))
    return json.loads(res)['TranslationList'][0]['Translation']


#火山翻译
def huoshan_language(text):
    k_access_key = 'abcd1234' # https://console.volcengine.com/iam/keymanage/
    k_secret_key = 'abcd1234'
    k_timeout = 30  # second
    k_service_info = \
        ServiceInfo('open.volcengineapi.com',
                    {'Content-Type': 'application/json'},
                    Credentials(k_access_key, k_secret_key, 'translate', 'cn-north-1'),
                    k_timeout,
                    k_timeout)
    k_query = {
        'Action': 'LangDetect',
        'Version': '2020-06-01'
    }
    k_api_info = {
        'langdetect': ApiInfo('POST', '/', k_query, {}, {})
    }
    service = Service(k_service_info, k_api_info)
    body = {
        'TextList': [text],
    }
    res=service.json('langdetect', {}, json.dumps(body))
    return json.loads(res)['DetectedLanguageList'][0]['Language']


if __name__ == '__main__':
    start=time.time()
    print(huoshan_trans('你好','en'))
    print(huoshan_language('你好'))
    end=time.time()
    print(f'耗时：{end-start:.2f}s')

