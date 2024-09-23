import socket
import threading

# 클라이언트가 서버에 접속할 때 실행되는 함수
def handle_client(client_socket, client_address):
    print(f"[{client_address}] 클라이언트 연결됨.")
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"[{client_address}] {message}")
            client_socket.send(f"ECHO: {message}".encode('utf-8'))
    finally:
        print(f"[{client_address}] 클라이언트 연결 종료.")
        client_socket.close()

# 서버 시작 함수
def start_server():
    server_ip = '0.0.0.0'
    server_port = 9999
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, server_port))
    server.listen(5)
    print(f"[서버 시작] {server_ip}:{server_port}에서 대기 중...")

    while True:
        client_socket, client_address = server.accept()
        client_handler = threading.Thread(
            target=handle_client, args=(client_socket, client_address)
        )
        client_handler.start()

if __name__ == "__main__":
    start_server()
