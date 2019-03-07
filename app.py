import socketio
from bocadillo import App, Templates, static

app = App()
templates = Templates(app)

# Create a socket.io async server.
# NOTE: use the asgi driver, as described in:
# https://python-socketio.readthedocs.io/en/latest/server.html#uvicorn-daphne-and-other-asgi-servers
sio = socketio.AsyncServer(async_mode="asgi")

# Create an ASGI-compliant app out of the socket.io server,
# and mount it under the root app.
# NOTE: "socket.io" is the default for `socketio_path`. We only add it
# here for the sake of being explicit.
# As a result, the client can connect at `/sio/socket.io`.
app.mount("/sio", socketio.ASGIApp(sio, socketio_path="socket.io"))

# Server static files for the socket.io client.
# See: https://github.com/socketio/socket.io-client
# NOTE: alternatively, the socket.io client could be served from
# a CDN if you don't have npm/Node.js available in your runtime.
# If so, static files would be linked to in the HTML page, and we wouldn't
# need this line.
# See: https://socket.io/docs/#Javascript-Client
app.mount("/socket.io", static("node_modules/socket.io-client/dist"))


@app.route("/")
async def index(req, res):
    res.html = await templates.render("index.html")


# Event handler for the "message" event.
# See: https://python-socketio.readthedocs.io/en/latest/server.html#defining-event-handlers
@sio.on("message")
async def handle_message(sid, data: str):
    print("message:", data)
    # Broadcast the received message to all connected clients.
    # See: https://python-socketio.readthedocs.io/en/latest/server.html#emitting-events
    await sio.emit("response", data)


if __name__ == "__main__":
    app.run()
