import pandas as pd 
import networkx as nx  
from datetime import datetime, timedelta
from shutil import copyfile
import os, json
import math

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)


def dataGenerate(folder_name):
    files = os.listdir("./retweet/{}".format(folder_name))
    if files == []:
        return

    graph = {"nodes": [], "edges": []}
    edges = pd.DataFrame(columns= ["source", "target", "weight"])
    nodes = pd.DataFrame(columns=["id", "label", "weight"])

    res = pd.DataFrame()
    for file_name in files:

        path = "./retweet/{}/{}".format(folder_name, file_name)
        try:
            df = pd.read_csv(path)
            df["class"] = file_name[:-4]
            df = df.sort_values(by="to_user_followers",ascending=False)
            length = min(5, df.shape[0])
            df = df.iloc[:length, :]
        except:
            continue
        
        res = pd.concat([res, df])

    edges['source'] = res["from_user_id"]
    edges["target"] = res["to_user_id"]
    edges["weight"] = 1
    edges["class"] = res["class"]
    edges["time"] = folder_name

    # 去除重复的边
    edges = edges.drop_duplicates(subset=None,keep='first',inplace=False)

    edges_list = []
    for i in range(edges.shape[0]):
        source_ = str(edges.iloc[i, 0])   
        target_ = str(edges.iloc[i, 1])
        id_ = str(edges.iloc[i, 3]) # 表示这条边属于哪一条推特
        item_ = {"source": source_, "target": target_, "id": id_}
        edges_list.append(item_)
    graph["edges"] = edges_list

    # 去除重复点
    nodes1 = pd.DataFrame(res.iloc[:,1:4].values, columns=["id", "label", "weight"])
    nodes1["class"]=pd.Series(res["class"].tolist())
    nodes1 = nodes1.drop_duplicates(subset=["id"],keep='first',inplace=False)

    nodes2 = pd.DataFrame(res.iloc[:,4:7].values, columns=["id", "label", "weight"])
    nodes2["class"]=pd.Series(res["class"].tolist())
    nodes2 = nodes2.drop_duplicates(subset=["id"],keep='first',inplace=False)

    nodes = pd.concat([nodes1, nodes2], axis = 0).drop_duplicates(subset=["id"],keep='first',inplace=False)

    nodes_list = []
    for i in range(nodes.shape[0]):
        id_ = str(nodes.iloc[i, 0])
        label_ = str(nodes.iloc[i, 1])
        weight_ = int(nodes.iloc[i, 2])
        weight_ = math.log(weight_, 10)
        class_ = str(nodes.iloc[i, 3])
        item_ = {"id": id_, "label": label_, "size": weight_, "class": class_}
        # item_ = {"id": id_, "label": label_, "class": class_}

        nodes_list.append(item_)

    graph["nodes"] = nodes_list
    print(type(graph))
    json_str = json.dumps(graph, indent=4)
    print(type(json_str))

    # with open('{}.json'.format(folder_name), 'w') as f:
    #     json.dump(graph, f)

    with open('{}.json'.format(folder_name), 'w') as json_file:
        json_file.write(json_str)