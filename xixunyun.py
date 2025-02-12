import requests  # 导入requests库，用于发送HTTP请求
import json  # 导入json库，用于处理JSON数据
import time   # 导入time库，用于时间控制
import smtplib  # 导入smtplib库，用于发送邮件
from em import sent_email  
  
data={'account':'220723217',#账号
      'app_id':'cn.vanber.xixunyun.saas',
      'app_version':'5.1.5',
      'key':'',
      'model':'SM-G955N',
      'password':'Zyj@2003197819747',#密码
      'platform':'2',
      'registration_id':'160a3797c8437218079',
      'request_source':'3',
      'school_id':'2025',#学校代码
      'system':'4.4.2',
      'uuid':'48:45:20:B9:D7:19'}
login_header={
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '227',
        'Host': 'api.xixunyun.com',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.8.1',

}
login_url=' https://api.xixunyun.com/login/api?from=app&version=5.1.5&platform=android&entrance_year=0&graduate_year=0'
request=requests.post(url=login_url,headers=login_header,data=data)
login_data=json.loads(request.text)#登陆成功后返回的信息
token=login_data['data']['token']

#经度
longitude = 'Uqnsdv4Ik9TDuGmsYpdLeuwcyfVKHgnD7wOfkm7erxJ2sR3I/ns9YFVMLEC+GPTmXU74gIZdZ4GidPpcncQtSX9mrlRiyIW6q9xt8tSD3kHXSsbdVH2hMNDcoKfwdxfei62xXt/ltCc2+eGhhp256wNERqbW5KRMg4oYQnN52D0/rAhW3IIkRNILbtHDsWUIl1ZWWtkZPPtgoF6HBLuFD5C/xgH+ML7tgG8K0qKKXgNP/ZyhuqdSaqjrUKdIxT7sK+GfMDPd5DBbxXUBZnV1xEiXbukxXMc8NhjDzGYxHoTVnklYa+Zq0usFcm1pYkXYzPUCE2jRcwRigJFUm+pprw=='
#维度
latitude = '6I62BIOmgDlN9CRxs252fhhdv4/ES6cv5VfKsF/A1qdYEqSH4PmNnkq76saVoMxXXKIymZPOepBRr9hHJeblhW6QBs74hgIlysMPA1LzI2vkC0NkWIPxtwFd0FwiFN/p3jwvCNS/uOwIMEKHzc8qDqY2o6R2hazBLLJ2LEHNRa76pXqt1ZAVdb3f06pn/vRD70vcli5uc1LdB3O7tLk8PV0bPp3Z/XIAS5lTatk9mw3B7zilDaacEE1mrKBSFHjwJkykL9poozisBNp1d+vZipxmMUTmnqLMbd+b8vjVXtiyj38i9E4JeBCGfvSruCmegrb34tgm9FyJ0KX1t1GbvA=='
time.sleep(3)

sign_url='https://api.xixunyun.com/signin_rsa?token='+token+'&entrance_year=0&graduate_year=0&school_id=2025'
sign_data={'address':'浙江省嘉兴市南湖区建设街道中山东路699号',#签到地址
           'address_name':'土豆咖啡(嘉兴中路店)',#签到地点名称
           'change_sign_resource':'0',
           'comment':'',
           'latitude':latitude,
           'longitude':longitude,
           'remark':'0',
    }
sign_request=requests.post(url=sign_url,data=sign_data,headers=login_header)
sign=json.loads(sign_request.text)
sent_email()
