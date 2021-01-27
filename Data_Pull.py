
# File uses the pybaseball python package to pull the lahman database


from pybaseball.lahman import *
download_lahman() #download the entire lahman database to your current working directory


print("Successful Download")