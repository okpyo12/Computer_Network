from socket import *
import time

HOST = "127.0.0.1"
PORT = 8080
SIZE = 1024

def find_method(method):
    method = method.split(' ')
    return method[0]

def find_url(url):
    url = url.split(' ')
    return url[1][0:-1]

def ManageDB(status, method, body):
    arr = []
    if ':' in body:
        key, value = body.split(':')
    if body != '':
        if status == 'CREATED':
            with open("DataBase.txt", "a") as f:
                f.write(f"{body}\n")
            return 'Created DB'
        elif status == 'OK':
            with open("DataBase.txt", "r") as f:
                lines = f.readlines()
            with open("DataBase.txt", "w") as f:
                for line in lines:
                    if line.rstrip()[0] != key:
                        f.write(line)
                    else:
                        f.write(f"{body}\n")
            return 'Update DataBase'
        elif status == 'BAD_REQUEST':
            return 'BAD_REQUEST'
        elif status == 'NOT_FOUND':
            return 'NOT_FOUND'
        else:
            return 'BAD_REQUEST'
    else:
        if status == 'OK':
            if method == 'GET':
                with open("DataBase.txt", "r") as f:
                    lines = f.readlines()
                    for line in lines:
                        arr.append(line.rstrip())
                    return arr
        elif status == 'CONTINUE':
            return ''
        else:
            return 'BAD_REQUEST'

def router(url, method, body):
    if '/' in url:
        host, path = url.split('/')
        if host == HOST:
            if method == 'HEAD': 
                return response('CONTINUE', method, body)
            if method == 'GET': return response('OK', method, body) 
            if method == 'POST': 
                if path == 'create': 
                    return response('CREATED', method, body) 
                else: return response('BAD_REQUEST', method, body) 
            elif method == 'PUT': 
                if path == 'update': return response('OK', method, body) 
                else: return response('BAD_REQUEST', method, body) 
            else: return response('NOT_FOUND', method, body)
        else:
            return ''
    else:
        return response('NOT_FOUND', method, body)

def response(status, method, body):
    date = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.localtime(time.time()))
    if status == 'CONTINUE':
        DBbody = ManageDB(status, method, body)
        return f"HTTP/1.1 100 CONTINUE\r\nDate: {date}\r\nContent-Type: text/html\r\nConnection: keep-alive\r\nContent-Length: {len(body)}\r\n\n{DBbody}"
    if status == 'OK':
        DBbody = ManageDB(status, method, body)
        return f"HTTP/1.1 200 OK\r\nDate: {date}\r\nContent-Type: text/html\r\nConnection: keep-alive\r\nContent-Length: {len(body)}\r\n\n{DBbody}"
    if status == 'CREATED':
        DBbody = ManageDB(status, method, body)
        return f"HTTP/1.1 201 CREATED\r\nDate: {date}\r\nContent-Type: text/html\r\nConnection: keep-alive\r\nContent-Length: {len(body)}\r\n\n{DBbody}"
    if status == 'BAD_REQUEST':
        DBbody = ManageDB(status, method, body)
        return f"HTTP/1.1 400 BAD_REQUEST\r\nDate: {date}\r\nContent-Type: text/html\r\nConnection: keep-alive\r\nContent-Length: {len(body)}\r\n\n{DBbody}"
    if status == 'NOT_FOUND':
        DBbody = ManageDB(status, method, body)
        return f"HTTP/1.1 404 NOT_FOUND\r\nDate: {date}\r\nContent-Type: text/html\r\nConnection: keep-alive\r\nContent-Length: {len(body)}\r\n\n{DBbody}"
    
with socket(AF_INET, SOCK_STREAM) as server_socket: # ?????? ?????? ??????
    server_socket.bind((HOST, PORT))  # ????????? ????????? HOST??? PORT ?????????
    server_socket.listen(1)  # ????????? ?????????????????? ????????? ??????

    while True:
        connectionsocket, client_addr = server_socket.accept()  # accept ???????????? ??????????????? ?????????????????? ???????????? ????????? ????????? ??????
        data = connectionsocket.recv(SIZE).decode('utf-8')  # client?????? ????????? ????????? ??????
        print(data)
        print('\n---------------------------------------\n')
        data = data.split('\n')
        method = find_method(data[0])
        url = find_url(data[1])
        body = data[-1]
        res_message = router(url, method, body)
        connectionsocket.send(res_message.encode('utf-8'))  # ????????? ??????????????? ?????????