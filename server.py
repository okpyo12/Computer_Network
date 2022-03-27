from socket import *

#통신정보 설정
SERVER_IP = '' #IP는 client에서 127.0.0.1로 지정
SERVER_PORT = 8080 #PORT번호 8080 지정
SERVER_SIZE = 1024 #SIZE 1024 지정
SERVER_URL = 'www.20181704.com'
SERVER_ADDR = (SERVER_IP, SERVER_PORT)
# 서버 소켓 설정
with socket(AF_INET, SOCK_STREAM) as server_socket:
    server_socket.bind(SERVER_ADDR)  # 주소 바인딩
    server_socket.listen(1)  # 클라이언트의 요청을 받을 준비
    # 무한루프 진입
    while True:
        client_socket, client_addr = server_socket.accept()  # 수신대기, 접속한 클라이언트 정보 (소켓, 주소) 반환
        msg = client_socket.recv(SERVER_SIZE).decode('utf-8').split(' ')  # 클라이언트가 보낸 메시지 반환
        method, url = msg[0], msg[1]
        print("Cilent가" + url + "에" + "[" + method + "]" + "Method를 요청했습니다")
        if method == "GET":
            if SERVER_URL == url:
                client_socket.send("GET-200 HTTP/200 OK".encode())  # 클라이언트에게 응답
            else:
                client_socket.send("GET-400 HTTP/400 BAD REQQUEST".encode())
        elif method == "HEAD":
            if SERVER_URL == url:
                client_socket.send("HEAD-200 HTTP/200 OK".encode())  # 클라이언트에게 응답
            else:
                client_socket.send("HEAD-400 HTTP/400 BAD REQQUEST".encode())
        elif method == "POST":
            if SERVER_URL == url:
                client_socket.send("POST-200 HTTP/200 OK".encode())  # 클라이언트에게 응답
            else:
                client_socket.send("POST-400 HTTP/400 BAD REQQUEST".encode())
        elif method == "PUT":
            if SERVER_URL == url:
                client_socket.send("PUT-200 HTTP/200 OK".encode())  # 클라이언트에게 응답
            else:
                client_socket.send("PUT-400 HTTP/400 BAD REQQUEST".encode())
        else:
            client_socket.send("USE CORRECT METHOD".encode())
        client_socket.close()  # 클라이언트 소켓 종료