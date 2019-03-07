from bocadillo import App, Templates, static
import socketio

app = App()
templates = Templates(app)

sio = socketio.AsyncServer()
app.mount("/sio", sio)
app.mount("/socket.io", static("node_modules/socket.io-client/dist"))


@app.route("/")
async def index(req, res):
    res.html = await templates.render("index.html")


if __name__ == "__main__":
    app.run(debug=True)
