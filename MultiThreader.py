import requests
import threading

url = ""##the URL you get from spam mails in your personal gmail

data = {
    'cc_number':'4 9754 1524',
    'cc_expmonth':'08',
    'cc_expyear':'21',
    'cc_cvv':'234',
}

def do():
    while True:
        response = requests.post(url, data=data).text
        print(response)
        
threads       = []

for i in range(50):
    t         = threading.Thread(target=do)
    t.daemon  = True
    threads.append(t)
    
for i in range(50):
    threads[i].start()
    
for i in range(50):
    threads[i].join()
