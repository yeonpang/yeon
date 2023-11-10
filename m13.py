"""import multiprocessing
import time

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")
        
if __name__ == "__main__":
        process1 = multiprocessing.Process(target=counter, args=("1num",))
        process2 = multiprocessing.Process(target=counter, args=("2num",))
        process3 = multiprocessing.Process(target=counter, args=("2num",))

start = time.time()

process1.start()
process2.start()
process3.start()

process1.join()
process2.join()
process3.join()
end = time.time()

print("proc-end, end-start") """

"""
import asyncio
import random as rd

async def tester(name):
    snum = rd.randint(10,20)
    print(f"{name} - {snum}")
    for i in range(snum) :
        await asyncio.sleep(1)
        print(f"{name} - {snum} - {i}")
        
    print(f"end of {name}")
    
async def main():
    task1 = asyncio.create_task(tester("1test"))
    
    task2 = asyncio.create_task(tester("2test"))
    
    task3 = asyncio.create_task(tester("3test"))
    
    print("start")
    await task1
    await task2
    await task3
    print("end")
    
if __name__ == '__main__':
    asyncio.run(main()) """
 
"""   
import asyncio

async def worker1():
    for i in range(1, 6):
        print(f"Task 1: Step {i}")
        await asyncio.sleep(1)
        
async def worker2():
    for i in range(1, 4):
        print(f"Task 2: Step {i}")
        await asyncio.sleep(2)
        
async def main():
    
    task_1 = asyncio.create_task(worker1())
    task_2 = asyncio.create_task(worker2())
    
    print("start task")
    await task_1
    await task_2
    print("end task")
    
if __name__ == '__main__':
    asyncio.run(main()) """
 
"""   
import time
import sched

start = time.time()

def tester(name):
    print(f"start-time {time.time() - start}")
    for i in range(3) :
        print(f"{name} - {1}")
        
    print(f"end of {name}")
    
    
def run() :
    s = sched.scheduler()
    s.enter(5, 1, tester, ('1num',))
    s.enter(5, 1, tester, ('4num',))
    s.enter(3, 1, tester, ('2num',))
    s.enter(7, 1, tester, ('3num',))
    s.run

if __name__ == "__main__" :
    run()
    # main
    print("end")
"""

"""
import diff_match_patch.diff_match_patch as dm

origin = "To be or not to be, That is a question!"
copyed = "To be or not to be, That is a question!"

dmp = dm()
diff = dmp.diff_main(origin, copyed)
dmp.diff_cleanupSemantic(diff)

for d in diff:
    print(d)
"""

"""
from faker import Faker as fk

# temp = fk()
temp =fk("ko-KR")
print(temp.name())

# temp - fk("ko-KR")
print(temp.name() + "\n" + 
	temp.address() + "\n" + 
	temp.postcode() + "\n" + 
	temp.company() + "\n" + 
	temp.job() + "\n" + 
	temp.phone_number() + "\n" + 
	temp.email() + "\n" + 
	temp.user_name() + "\n" + 
	temp.ipv4_private() + "\n" + 
	temp.ipv4_public() + "\n" + 
	temp.catch_phrase() + "\n" + 
	temp.color_name()) """
 
"""
 
from faker import Faker as fk

# temp = fk()
temp =fk("ko-KR")
print(temp.name())

with open("fktemp.txt", "w", newline='') as f :
    for i in range (30) :
        f.write(temp.name() + "," +
        temp.address() + "," +
        temp.postcode() + "," +
        temp.company() + "," + 
	    temp.job() + "," + 
	    temp.phone_number() + "," + 
	    temp.email() + "," + 
	    temp.user_name() + "," + 
	    temp.ipv4_private() + "," + 
	    temp.ipv4_public() + "," + 
	    temp.catch_phrase() + "," + 
	    temp.color_name() + "\n") 
	"""

"""
import subprocess as sp
 
res = sp.run(["cmd", "/c", "dir"], capture_output=True)
print(res)
"""

"""
import traceback as tb

def tester() :
    return 1/0

def caller() :
    tester()
    
def main() :
    try :
        caller()
        
    except ZeroDivisionError:
        print("zde error")
        
    except ValueError :
        print("ve error")
        
    except Exception as ex:
        print("ex error", ex)
        
    else :
        print("ok")
        
    finally :
        print("end")"""
        
"""
        
from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://news.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

pres = res_html.find("h1")
print(pres)
print("\n1--------------------\n")
print(pres.get_text().strip())
print("\n2--------------------\n")
print(pres.next_element.get_text().strip())
print(pres.get_text())
print("\n6--------------------\n")

tres = res_html.find("title")
print(tres)
print("\n3--------------------\n")
print(tres.next_element)
print("\n4--------------------\n")
print(tres.get_text().strip())

fares = res_html.findAll("a")
for i in fares:
    print(i.get_text())
    
print("\n5--------------------\n")

clres = res_html.findAll(class_="doc-title")
print(clres)

print("\n6--------------------\n")
clrs = res_html.find(class_="head_top")
print(clrs)
print(clrs.get_text())"""


"""
from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://news.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')
item = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > strong")

print(item.get_text())

wt = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > div > span.txt_name")
print(wt.get_text())

goods = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_reply > div > button > strong")
print(goods.get_text())

"""

from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://news.daum.net/"
res = rq.get(url)
 
hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

iss = res_html.select("a.wrap_thumb")
# print(iss)
print("\n6-------------------------------\n")	

for i in iss :
    issue = i.get_text()
    print(issue)
    
print("\n6-------------------------------\n")
ct = res_html.select("a.wrap_thumb")
for j in ct :
    c = j.attrs["date-trara-custom"]
    print(c + "\n")
    
