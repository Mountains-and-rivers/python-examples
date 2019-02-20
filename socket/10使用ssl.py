import socket
import ssl


def client():
    hostname = 'www.baidu.com'
    sock = socket.socket()
    sock.setblocking(False)
    # context = ssl.create_default_context()
    # ssock = context.wrap_socket(sock)
    ssock = ssl.wrap_socket(sock)
    ssock.setblocking(False)
    try:
        ssock.connect((hostname, 443))
    except BlockingIOError:
        pass

    # with socket.create_connection((hostname, 443)) as sock:
    #     with context.wrap_socket(sock, server_hostname=hostname) as ssock:
    #         # 获取对方地址
    #         print(ssock.getpeername())


def server():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('/path/to/certchain.pem', '/path/to/private.key')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
        sock.bind(('127.0.0.1', 8443))
        sock.listen(5)
        with context.wrap_socket(sock, server_side=True) as ssock:
            conn, addr = ssock.accept()
            # ...


if __name__ == '__main__':
    client()
