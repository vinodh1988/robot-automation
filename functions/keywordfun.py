def processConfig(url,username,password,drivername):
    print("url-",url)
    print("username-",username)
    print("password-",password)
    print("drivername-",drivername)

processConfig(url="x://store",password="dfjlsjdf",username="store",drivername="dd.driver")

processConfig("h3://url","vinodh",drivername="x.driver",password="password")

#if positionalparameters and keyword parameters used together
#order is first positional then keyword and viceversa is not accepted