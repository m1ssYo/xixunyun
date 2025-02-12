import smtplib
from email.mime.text import MIMEText
from email.header import Header

def sent_email():
    smtp_server = 'smtp.qq.com'
    smtp_port = 465  # 使用SSL

    # 邮件主题和正文
    subject = '张宇杰'
    body = '签到成功'

    # 构建邮件
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = '1691733533@qq.com'
    msg['To'] = '1691733533@qq.com'

    try:
        # 登录并发送邮件
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login('1691733533@qq.com', 'fsflozzupmlbfdaj')
            server.sendmail('1691733533@qq.com', ['1691733533@qq.com'], msg.as_string())
    except smtplib.SMTPResponseException as e:
        pass
    except Exception as ex:
        pass
