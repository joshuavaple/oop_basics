import other_script 

# the other script will get executed upon being imported
# however, the name displayed when running via importing 
# is no longer __main__ but the module name
print("")
print("****inside current script.py*****")
print("__name__ is ",__name__)