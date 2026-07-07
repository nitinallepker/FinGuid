import { useState } from "react";
import axios from "axios";

import ChatWindow from "./components/ChatWindow";
import ChatInput from "./components/ChatInput";

function App() {
  const [loading, setLoading] = useState(false);

  const [messages, setMessages] = useState([
    {
      sender: "ai",
      text:
        "Welcome to FinGuid.\n\n" +
        "I help you explore financial paths based on your goals, timeline, income and financial situation.\n\n" +
        "What financial goal are you trying to achieve?\n\n" +
        "Examples:\n" +
        "• Buy a House\n" +
        "• Buy a Car\n" +
        "• Marriage\n" +
        "• Retirement\n" +
        "• Start a Business",
    },
  ]);

  const sendMessage = async (message) => {

    setMessages((prev) => [
      ...prev,
      {
        sender: "user",
        text: message,
      },
    ]);

    setLoading(true);

    try {

      const response = await axios.post(
        "https://finguid-backend.onrender.com",
        {
          message,
        }
      );

      const data = response.data;

      const newMessages = [];

      if (data.answer) {
        newMessages.push({
          sender: "ai",
          text: data.answer,
        });
      }

      if (data.question && data.question.trim() !== "") {
        newMessages.push({
          sender: "ai",
          text: data.question,
        });
      }

      setMessages((prev) => [...prev, ...newMessages]);

    } catch (error) {

      console.error(error);

      setMessages((prev) => [
        ...prev,
        {
          sender: "ai",
          text: "Error contacting server.",
        },
      ]);

    } finally {

      setLoading(false);

    }
  };

  return (
    <div className="app">

      <h1>FinGuid</h1>

      <p className="tagline">
        Turn financial goals into actionable plans.
      </p>

      <ChatWindow
        messages={messages}
        loading={loading}
      />

      <ChatInput onSend={sendMessage} />

    </div>
  );
}

export default App;