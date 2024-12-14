import tools

try:
    youbike_data:list[dict] = tools.get_youbikes()
except Exception as e:
    print(e)
else:
    print(youbike_data)



