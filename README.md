# socket.io example

socket.io client/server example with [Bocadillo], [python-socketio] and [socket.io client][socketio-client].

This is a reproduction of the the [socket.io chat tutorial](https://socket.io/get-started/chat), but using:

- python-socketio instead of [socket.io][socketio-server] as a server-side socket.io backend.
- Bocadillo instead of Express as a web application server.

## Install

```bash
pip install bocadillo python-socketio
```

## Quick start

1. Fire off the server:

```bash
python app.py
```

2. Open up a web browser at http://localhost:8000, and start chatting!

## License

MIT

[bocadillo]: https://bocadilloproject.github.io
[python-socketio]: https://python-socketio.readthedocs.io
[socketio-client]: https://socket.io/docs/client-api/#Event-‘connect’
[socketio-server]: https://github.com/socketio/socket.io
