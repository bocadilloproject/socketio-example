from bocadillo import App, Templates, static
import socketio

app = App()
templates = Templates(app)

sio = socketio.AsyncServer(async_mode="asgi")
app.mount("/sio", socketio.ASGIApp(sio))
app.mount("/socket.io", static("node_modules/socket.io-client/dist"))


@app.route("/")
async def index(req, res):
    res.html = await templates.render("index.html")


class EchoChatNamespace(socketio.AsyncNamespace):
    def on_connect(self, sid, environ):
        pass

    def on_disconnect(self, sid):
        pass

    async def on_message(self, sid, data):
        print("message:", data)
        await self.emit("response", data)


sio.register_namespace(EchoChatNamespace("/chat"))


if __name__ == "__main__":
    app.run()
