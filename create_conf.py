import yaml
import json
import os


# 每个配置文件中有几个账户 count
# 文件的路径前缀
worker_dir = "worker"

def accounts(count):
    with open("./accounts.yaml", "r", encoding="utf-8") as f:
        result = yaml.load_all(f.read(), Loader=yaml.FullLoader)

    ret = []
    for index, item in enumerate(result):
        if len(ret) == count:
            yield ret
            ret = []
        else:
            ret.append(item["account"])

    if ret != []:
        yield ret
        ret = []

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        print("---  %s 创建成功！ ---" % path)
    else:
        print("---  %s 已经存在!  ---" % path)

for index, item in enumerate(accounts(5)):
    mkdir(worker_dir+str(index+1))
    with open(worker_dir+str(index+1)+"/accounts.json", "w", encoding="utf-8") as f:
        json.dump(item, f)
