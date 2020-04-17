# encoding=utf-8
import sys
import io
import re
from elasticsearch import Elasticsearch
from creole import CreoleParser, HtmlEmitter
from opencc import OpenCC
from E_mysql import insert_db

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
#繁转简
c = OpenCC('t2s')
es = Elasticsearch(hosts="127.0.0.1", port=9200, timeout=200)


with open("your.json","r")as f:
    counts=f.read()
# print(counts)
people_name = re.findall(pattern="'page': (.*?)]", string=counts.replace("\n", ''))
def datas():
    for v in people_name:
        v1 = str(v).replace("[", "").replace("'", '').split(",")
        for v2 in v1:
            v3 = v2.strip()
            print(v3, "开始")
            dsl = {"query": {
                "bool": {"must": [{'term': {"title.keyword": v3}}]}}}

            result = es.search(index='index', doc_type='type', body=dsl)
            try:
                hits=result["hits"]["hits"][0]['_source']
                a="123"
            except:
                a="没有查询到"
            if a == "没有查询到":
                print(a)
            else:
                parm_key = hits["parm_key"]
                title=hits["title"]
                titles = (str(title).replace('\t', ' '))
                # 繁简转化
                zh_title = c.convert(titles)
                ns=hits["ns"]
                id=hits["id"]
                revision=hits["revision"]
                parentid=hits["parentid"]

                timestamps=hits["timestamp"]

                contributor=hits["contributor"]

                username=hits["username"]
                usernames = (str(username).replace('\t', ' '))
                # 繁简转化
                zh_username = c.convert(usernames)
                model=hits["model"]

                format=hits["format"]

                text=hits["text"]
                
                sha1=hits["sha1"]

                restrictions=hits["restrictions"]

                minor=hits["minor"]

                comment=hits["comment"]
                comments = (str(comment).replace('\t', ' '))
                # 繁简转化
                zh_comment = c.convert(comments)
                ip=hits["ip"]
                all_count=(parm_key,zh_title,ns,id,revision,parentid,timestamps,contributor,zh_username,model,format,str(zh_text_html),sha1,restrictions,minor,zh_comment,ip)
                insert_db_gzbd(all_count,parm_key)
                print("success")
if __name__ == '__main__':

    datas()
