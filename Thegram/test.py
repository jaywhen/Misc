# from faker import Faker
# fake = Faker(['zh_CN', 'en_US', 'ja_JP'])
# for _ in range(10):
#     print(fake.name())
#     print(fake.text())

from qiniu import Auth, put_file, etag
import qiniu.config
#需要填写你的 Access Key 和 Secret Key
access_key = 'jt9aI2ok1ldGwtRfWORz4TqMF8nDxgv_gJA2dgGJ'
secret_key = 'AvVZPtBub-IZilnFNjwewy7YM57UuFLi5B0s84kW'
#构建鉴权对象
q = Auth(access_key, secret_key)
#要上传的空间
bucket_name = 'thegram'
#上传后保存的文件名
key = 'iconf.png'
#生成上传 Token，可以指定过期时间等
token = q.upload_token(bucket_name, key, 3600)
#要上传文件的本地路径
localfile = './sleep.png'
ret, info = put_file(token, key, localfile)
print(info)
assert ret['key'] == key
assert ret['hash'] == etag(localfile)