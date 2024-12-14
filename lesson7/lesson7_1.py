from tools import taipei

try:
    youbike_data:list[dict] = taipei.get_youbikes()
except Exception as e:
    print(e)
else:
    print(youbike_data)



