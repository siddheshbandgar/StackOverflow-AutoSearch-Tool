import subprocess
import os
import sys
from subprocess import Popen,PIPE
import requests
import json
import webbrowser
import random

process = subprocess.Popen(['python3','test.py'], stdout=PIPE, stderr=PIPE)
out, err = process.communicate()
err = err.decode('utf-8')
if err == "":
    print("No errors found!")
    exit()

l1 = err.split()

err = ' '.join(l1)

error_list = ["NameError:","IndexError:","KeyError:","TypeError:","ValueError:","ImportError:","ModuleNotFound:"]

for element in l1:
    if element in error_list:
        error_type = element
error_type = error_type[:-1]
print("Error Type" +": "+ error_type)

error_msg = err[err.index(error_type)+len(error_type)+2:]
print("Error Msg"+": "+ error_msg)

  
URL = "https://api.stackexchange.com/2.2/search/advanced?order=desc&sort=activity&site=stackoverflow"
  

PARAMS = {'title':error_type+": "+error_msg,
          'tagged':'python', 'accepted':'true'} 
  
r = requests.get(url = URL, params = PARAMS) 
  
data = r.json()

for i in range(5):
    webbrowser.open_new_tab(data['items'][random.randint(5,len(data['items']))]['link'])

