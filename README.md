## WebSocket with Flask

使用WebSocket实现实时信息更新，服务端使用Flask。

> WebSocket 是 HTML5 的新功能，它是一种 TCP 协议。当客户端和服务器完成握手，建立连接之后，ws 就如普通 socket 一样，在两者之间进行通信。
WS 是一种 TCP 协议，所以是语言无关的，用任何语言都可以实现服务器端的编程。

服务端：
- [Flask](https://github.com/pallets/flask)：轻量级Web框架
- [gevent](https://github.com/gevent/gevent) & [gevent-websocket](https://github.com/jgelens/gevent-websocket): 实现了websocket协议的Http服务器

功能：
前端实时输入信息，后端实时将详细返回并加上服务端时间




