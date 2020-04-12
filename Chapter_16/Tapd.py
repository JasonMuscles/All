import requests

r = requests.get(
    'https://api.tapd.cn/stories?workspace_id=30959932',
    auth=('jOD?hXg~', '523D7721-C09A-0939-259F-94AB457DCCDA'),
)

ret = r.text  # 获取接口返回结果

file_path = "TAPD.json"
with open(file_path, "w") as file_object:
    file_object.write(ret)
