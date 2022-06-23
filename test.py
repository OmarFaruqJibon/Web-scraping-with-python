from gevent import monkey
monkey.patch_all() # will help the program enable to work as in collabrate way
import gevent, time, requests

start = time.time()
# start to record the time

url_list = ['https://www.baidu.com/',
          'https://www.bing.com/',
          'https://www.sohu.com/',
          'https://www.swpu.edu.cn/',
          'https://www.qq.com/',
          'https://www.tmall.com/',
          'https://www.163.com/',
          'http://www.ifeng.com/',
          'http://www.google.com/'
]
#package 8 websites in a list


def crawler(url):
    r = requests.get(url)
    print(url, time.time()-start, r.status_code)

task_list = []

for url in url_list:
    task = gevent.spawn(crawler, url) #setup the taskes
    task_list.append(task) #put the task into the task_list

gevent.joinall(task_list) #execute all the tasks in the list, in other words, crawling the websites

end = time.time()
print(end-start)
