from faker import Faker
fake = Faker(['zh_CN', 'en_US', 'ja_JP'])
for _ in range(10):
    print(fake.name())
    print(fake.text())