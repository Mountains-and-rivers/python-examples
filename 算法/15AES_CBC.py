import contextlib
import socket
import os

BS = 32  # Bytes


def pad(s):
    """填充要加密的文本到 BS 的倍数。
    填充内容见一下算法。
    """

    return s + (BS - len(s) % BS) * chr(BS - len(s) % BS).encode('utf-8')


def upad(s):
    """剔除填充的内容"""

    return s[0:-s[-1]]


@contextlib.contextmanager
def create_alg(typ, name):
    s = socket.socket(socket.AF_ALG, socket.SOCK_SEQPACKET, 0)
    try:
        s.bind((typ, name))
        yield s
    finally:
        s.close()


def encrypt(plaintext, key, iv):
    ciphertext = None
    with create_alg('skcipher', 'cbc(aes)') as algo:
        algo.setsockopt(socket.SOL_ALG, socket.ALG_SET_KEY, key)
        op, _ = algo.accept()
        with op:
            plaintext = pad(plaintext)
            op.sendmsg_afalg([plaintext],
                             op=socket.ALG_OP_ENCRYPT,
                             iv=iv)
            ciphertext = op.recv(len(plaintext))

    return ciphertext


def decrypt(ciphertext, key, iv):
    plaintext = None
    with create_alg('skcipher', 'cbc(aes)') as algo:
        algo.setsockopt(socket.SOL_ALG, socket.ALG_SET_KEY, key)
        op, _ = algo.accept()
        with op:
            op.sendmsg_afalg([ciphertext],
                             op=socket.ALG_OP_DECRYPT,
                             iv=iv)
            plaintext = op.recv(len(ciphertext))

    return upad(plaintext)


def main() -> None:
    key = b'1234567812345678'
    iv = os.urandom(16)

    plaintext = b'Demo AF_ALG'
    ciphertext = encrypt(plaintext, key, iv)
    plaintext = decrypt(ciphertext, key, iv)

    print(ciphertext.hex())
    print(plaintext)


if __name__ == '__main__':
    main()
