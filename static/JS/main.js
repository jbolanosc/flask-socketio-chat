let chatForm = "";
let chatMessages = "";
let roomName = "";
let userList = "";
let leaveBtn = "";

const socket = io();

const { id, username, room } = user;

window.onload = () => {
  roomName = document.getElementById("room-name");
  userList = document.getElementById("users");
  chatForm = document.getElementById("chat-form");
  chatMessages = document.querySelector(".chat-messages");
  leaveBtn = document.getElementById("btnLeave");
  socket.emit("join", { id: id, username: username, room: parseInt(room) });

  createChatListener();
  leaveListener();
};

const leaveListener = () => {
  //Listen to leave button click
  leaveBtn.addEventListener("click", (e) => {
    socket.emit("leave", { room: parseInt(room) });
  });
};

const createChatListener = () => {
  //Submit message
  chatForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const msg = e.target.elements.msg.value;
    //emit msg to server
    socket.emit("new_message", msg);

    // Clear input
    e.target.elements.msg.value = "";
    e.target.elements.msg.focus();
  });
};

socket.on("roomUsers", ({ room, users }) => {
  outputRoomName(room);
  outputUsers(users);
});

//Get message
socket.on("Message", (message) => {
  outputMessage(message);

  chatMessages.scrollTop = chatMessages.scrollHeight;
});

//output Message
function outputMessage(message) {
  const div = document.createElement("div");

  div.classList.add("message");
  div.innerHTML = `<p class="meta">${message.username} <span>${message.time}</span></p>
    <p class="text">
      ${message.text}
    </p>`;
  document.querySelector(".chat-messages").appendChild(div);
}

//Output room name
function outputRoomName(room) {
  roomName.innerText = room;
}

//Output connected users
function outputUsers(users) {
  userList.innerHTML = `${users
    .map((user) => `<li>${user.username}</li>`)
    .join("")}`;
}
