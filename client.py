from socket import *

IP = "127.0.0.1"
PORT = 8080
SIZE = 1024
test_case = [
    {'url': '127.0.0.1/',
        'method': 'HEAD',
        'data': ''
    },
    {'url': '127.0.0.1/create',
        'method': 'POST',
        'data': '1:test1'
    },
    {'url': '127.0.0.1/create',
        'method': 'POST',
        'data': '2:test2'
    },
    {'url': '127.0.0.1/create',
        'method': 'PUT',
        'data': '3:test3'
    },
    {'url': '127.0.0.1/',
        'method': 'GET',
        'data': ''
    },
    {'url': '127.0.0.1/update',
        'method': 'PUT',
        'data': '1:test5'
    },
    {'url': '127.0.0.1/ComputerNetwork',
        'method': 'POST',
        'data': '6:test6'
    },
    {'url': '127.0.0.1/',
        'method': 'GET',
        'data': ''
    }
]

def request_formating(method, data, url):
    return f"{method} / HTTP/1.1\r\nHost: {url}\r\nConnection: keep-alive\r\nContent-Type: text/html\r\nContent-Length: {len(data)}\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit\r\n\n{data}"

for test in test_case:
    with socket(AF_INET, SOCK_STREAM) as client_socket: # 소켓 객체 생성
        client_socket.connect((IP, PORT))  # 생성한 소켓에 HOST와 PORT 연결
        method = test['method']
        url = test['url']
        data = test['data']
        request = request_formating(method, data, url)
        client_socket.send(request.encode('utf-8')) # 메세지 전송
        response = client_socket.recv(SIZE).decode('utf-8') # 클라이언트가 보낸 메세지 수신 대기
        print(response) # 수신 받은 문자 출력
        print('\n---------------------------------------\n')
        client_socket.close()