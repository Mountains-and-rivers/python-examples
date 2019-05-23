import asyncio


async def http_ok(r, w):
    head = b"HTTP/1.1 200 OK\r\n"
    head += b"Content-Type: text/html\r\n"
    head += b"\r\n"

    body = b"<html>"
    body += b"<body><h1>Hello world!</h1></body>"
    body += b"</html>"

    _ = await r.read(1024)
    w.write(head + body)
    await w.drain()
    w.close()


async def main():
    server = await asyncio.start_server(
        http_ok, "127.0.0.1", 8888
    )

    async with server:
        await server.serve_forever()


asyncio.run(main())