#!/usr/bin/python3

import sys
import os
from urllib.parse import parse_qs

qString = os.environ['QUERY_STRING']


qVal = parse_qs(qString)
name = qVal['name'][0]
id = qVal['id'][0]
password = qVal['password'][0]

responseBody = f'<HTML><HEAD><META charset="utf-8"></HEAD>'\
               f'<BODY><H1> Complete Login <BR><BR><BR> Name is {name}'\
               f'<BR> Your ID is {id}'\
               f'<BR> Your password is {password} </H1><BR>'\
               f'<a href="index.html"> Home </a> <BR> </BODY></HTML>'
print(responseBody)