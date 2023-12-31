import smtplib
import email
# 负责构造文本
from email.mime.text import MIMEText
# 负责构造图片
from email.mime.image import MIMEImage
# 负责将多个对象集合起来
from email.mime.multipart import MIMEMultipart
from email.header import Header


# SMTP服务器,这里使用163邮箱
mail_host = "smtp.qq.com"
# 发件人邮箱
mail_sender = "1060819195@qq.com"
# 邮箱授权码,注意这里不是邮箱密码,如何获取邮箱授权码,请看本文最后教程
mail_license = "cnarhjfuiltxbahi"
# 收件人邮箱，可以为多个收件人
mail_receivers = "799827759@qq.com"


mm = MIMEMultipart('related')


# 邮件主题
subject_content = """Python邮件测试"""
# 设置发送者,注意严格遵守格式,里面邮箱为发件人邮箱
mm["From"] = "sender_name<1060819195@qq.com>"
# 设置接受者,注意严格遵守格式,里面邮箱为接受者邮箱
mm["To"] = "receiver_1_name<799827759@qq.com>"
# 设置邮件主题
mm["Subject"] = Header(subject_content,'utf-8')


# 邮件正文内容
body_content = """你好，这是一个测试邮件！"""
# 构造文本,参数1：正文内容，参数2：文本格式，参数3：编码方式
message_text = MIMEText(body_content,"plain","utf-8")
# 向MIMEMultipart对象中添加文本对象
mm.attach(message_text)

# 构造附件
read = open('BZDHT.ttf', 'rb').read()
atta = MIMEText(read, 'base64', 'utf-8')
# 设置附件信息
atta["Content-Disposition"] = 'attachment; filename="BZDHT.ttf"'
# 添加附件到邮件信息当中去
mm.attach(atta)


# 创建SMTP对象
stp = smtplib.SMTP()
# 设置发件人邮箱的域名和端口，端口地址为25
stp.connect(mail_host, 587)
# set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
stp.set_debuglevel(1)
# 登录邮箱，传递参数1：邮箱地址，参数2：邮箱授权码
stp.login(mail_sender,mail_license)
# 发送邮件，传递参数1：发件人邮箱地址，参数2：收件人邮箱地址，参数3：把邮件内容格式改为str
stp.sendmail(mail_sender, mail_receivers, mm.as_string())
print("邮件发送成功")
# 关闭SMTP对象
stp.quit()
