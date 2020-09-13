from thegram import app
from qiniu import Auth, put_data
import os

access_key = os.getenv('QINIU_ACCESS_KEY')
secret_key = os.getenv('QINIU_SECRET_KEY')
test_domain_prefix = os.getenv('QINIU_TEST_DOMAIN')

q = Auth(access_key, secret_key)

bucket_name = os.getenv('QINIU_BUCKET_NAME')


def qiniu_upload_file(source_file, save_file_name):
    token = q.upload_token(bucket_name, save_file_name)
    ret, info = put_data(token, save_file_name, source_file.stream.read())
    print(type(info.status_code), info)

    if info.status_code == 200:
        return test_domain_prefix + save_file_name
    return None