// Change this if your backend runs somewhere other than localhost:8000
const API_BASE = "https://interview-assistant-2wju.onrender.com";

let sessionId = null;

const messagesEl = document.getElementById("messages");
const inputEl = document.getElementById("userInput");
const sendBtn = document.getElementById("sendBtn");
const newChatBtn = document.getElementById("newChatBtn");
const jdFileEl = document.getElementById("jdFile");
const jdStatusEl = document.getElementById("jdStatus");

function addMessage(text, role) {
  const div = document.createElement("div");
  div.className = "message " + role;
  div.textContent = text;
  messagesEl.appendChild(div);
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

async function createSession() {
  const res = await fetch(`${API_BASE}/session`, { method: "POST" });
  if (!res.ok) throw new Error("Failed to create session");
  const data = await res.json();
  sessionId = data.session_id;
}

async function sendMessage() {
  const text = inputEl.value.trim();
  if (!text) return;

  if (!sessionId) {
    try {
      await createSession();
    } catch (e) {
      addMessage("Could not connect to the server. Is the backend running?", "system");
      return;
    }
  }

  addMessage(text, "user");
  inputEl.value = "";
  sendBtn.disabled = true;

  try {
    const res = await fetch(`${API_BASE}/session/${sessionId}/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text }),
    });

    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      addMessage(err.detail || "Something went wrong.", "system");
      return;
    }

    const data = await res.json();
    addMessage(data.reply, "assistant");
  } catch (e) {
    addMessage("Could not reach the server.", "system");
  } finally {
    sendBtn.disabled = false;
  }
}

async function uploadJD(file) {
  if (!sessionId) {
    try {
      await createSession();
    } catch (e) {
      jdStatusEl.textContent = "Could not connect to the server.";
      return;
    }
  }

  jdStatusEl.textContent = "Uploading...";

  const formData = new FormData();
  formData.append("file", file);

  try {
    const res = await fetch(`${API_BASE}/session/${sessionId}/upload-jd`, {
      method: "POST",
      body: formData,
    });

    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      jdStatusEl.textContent = err.detail || "Upload failed.";
      return;
    }

    const data = await res.json();
    jdStatusEl.textContent = data.message;
    addMessage(data.message, "system");
  } catch (e) {
    jdStatusEl.textContent = "Could not reach the server.";
  }
}

sendBtn.addEventListener("click", sendMessage);

inputEl.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
});

newChatBtn.addEventListener("click", async () => {
  messagesEl.innerHTML = "";
  jdStatusEl.textContent = "";
  sessionId = null;
  await createSession();
  addMessage("New interview started. Ask me anything about Aditya's background.", "assistant");
});

jdFileEl.addEventListener("change", () => {
  const file = jdFileEl.files[0];
  if (file) uploadJD(file);
});

// Start a session as soon as the page loads
createSession().catch(() => {
  addMessage("Could not connect to the server. Make sure the backend is running on " + API_BASE, "system");
});
