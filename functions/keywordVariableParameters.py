def processConfig(**config):
    #config is a dictionary in this case
    for key,value in config.items():
        print(f"{key} -> {value}")


processConfig(cpu="2 vCpus",memory="16gb", disk="200GB")
print("---------------------------------------------------")
processConfig(team="devopos",size=20,manager="Peterson",technology="Java",cloud="AWS")