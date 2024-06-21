import myops.config as config
from myops.config import awsconfig,dbconfig

config.sayHello()
print(config.dbconfig["dburl"])
print(config.useremails[1])

print(awsconfig["accesskey"])
print(dbconfig["username"])