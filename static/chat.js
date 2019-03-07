// See: https://socket.io/docs/client-api/#With-custom-path
const socket = io("/chat", { path: "/sio/socket.io" });

socket.on("connect", () => {
  console.log("A user is connected!");
});
socket.on("disconnect", () => {
  console.log("User has disconnected.");
});
