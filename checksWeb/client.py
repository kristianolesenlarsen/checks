#!/usr/bin/python           # This is client.py file


import requests 

if __name__ == '__main__':
    requests.post('http://localhost:8081/', data = {'kuid': 'asd123', 'problem': 1, 'status': True})