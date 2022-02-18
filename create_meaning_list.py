import requests
from bs4 import BeautifulSoup
import itertools

idiom_list=[i.strip() for i in open("Static_idioms.txt").readlines()]
repls=["one","one's","the"]
meanings=[]

def find_defs(link):
    text=requests.get(link).text
    soup=BeautifulSoup(text,features="html.parser")
    defs = soup.findAll("div", attrs={"class": "ds-list"}) + soup.findAll("div", attrs={"class": "ds-single"})
    return defs


for idiom in idiom_list:
    prons_count=idiom.count("[pron]")
    defs=[]
    cands=list(itertools.product(repls, repeat=prons_count))
    if prons_count>1:
        for cand in cands:
            idiom2=idiom
            while cand:
                idiom2=idiom2.replace("[pron]",cand[0],1)
                cand=cand[1:]
            url="https://idioms.thefreedictionary.com/"+"+".join(idiom2.split())
            cand_defs=find_defs(url)
            if len(cand_defs)>len(defs):
                defs=cand_defs
    else:
        url = "https://idioms.thefreedictionary.com/" + "+".join(idiom.split())
        defs = find_defs(url)
    meanings.append(defs)
    defs=[]

fp=open("Static_idioms_meanings.txt",'w')
fp.write("\n".join(str(i) for i in meanings))
fp.close()

