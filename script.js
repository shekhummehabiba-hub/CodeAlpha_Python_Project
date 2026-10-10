const input = document.getElementById("userInput");
const chatBox = document.getElementById("chatBox");


// --------------------------------
// Send message
// --------------------------------

async function sendMessage() {

    const message = input.value.trim();

    if (message === "") {
        return;
    }


    // Show user message

    addMessage(message, "user");


    // Clear input

    input.value = "";


    try {

        // Call Python API

        const response = await fetch("/api/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });


        const data = await response.json();


        if (!response.ok) {

            addMessage(
                data.error || "Something went wrong.",
                "bot"
            );

            return;
        }


        // Show bot response

        addMessage(
            data.bot_message,
            "bot"
        );

    }

    catch (error) {

        console.error(error);

        addMessage(
            "Unable to connect to the server.",
            "bot"
        );

    }

}


// --------------------------------
// Add message to chat
// --------------------------------

function addMessage(message, sender) {

    const messageDiv =
        document.createElement("div");


    messageDiv.classList.add(
        "message"
    );


    if (sender === "user") {

        messageDiv.classList.add(
            "user-message"
        );

    }

    else {

        messageDiv.classList.add(
            "bot-message"
        );

    }


    const avatar =
        document.createElement("div");


    avatar.classList.add("avatar");


    if (sender === "user") {

        avatar.textContent = "👤";

    }

    else {

        avatar.textContent = "🤖";

    }


    const content =
        document.createElement("div");


    content.classList.add(
        "message-content"
    );


    content.textContent = message;


    if (sender === "user") {

        messageDiv.appendChild(content);

        messageDiv.appendChild(avatar);

    }

    else {

        messageDiv.appendChild(avatar);

        messageDiv.appendChild(content);

    }


    chatBox.appendChild(messageDiv);


    // Scroll to bottom

    chatBox.scrollTop =
        chatBox.scrollHeight;

}


// --------------------------------
// Enter key
// --------------------------------

input.addEventListener(
    "keypress",
    function(event) {

        if (event.key === "Enter") {

            sendMessage();

        }

    }
);


// --------------------------------
// Clear chat
// --------------------------------

function clearChat() {

    chatBox.innerHTML = "";

    addMessage(
        "Hello! 👋 I am PyBot. How can I help you?",
        "bot"
    );

}