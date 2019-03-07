from bocadillo import App, Templates
import socketio

app = App()
templates = Templates(app)

sio = socketio.AsyncServer()
app.mount("/sio", sio)


@app.route("/")
async def index(req, res):
    res.html = await templates.render("index.html")


if __name__ == "__main__":
    app.run(debug=True)
