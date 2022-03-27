from socket import *
# 접속 정보 설정
IP = '127.0.0.1'
PORT = 8080
SIZE = 1024
ADDR = (IP, PORT)

# 클라이언트 소켓 설정
while True:
    with socket(AF_INET, SOCK_STREAM) as client_socket:
        client_socket.connect(ADDR)  # 서버에 접속
        text = input("Method(GET,HEAD,POST,PUT): ")
        url = input("URL: ")
        client_socket.send((text+" "+url).encode())  # 서버에 메시지 전송
        msg = client_socket.recv(SIZE).decode('utf-8')  # 서버로부터 응답받은 메시지 반환
        print("resp from server : {}".format(msg))  # 서버로부터 응답받은 메시지 출력
        client_socket.close()