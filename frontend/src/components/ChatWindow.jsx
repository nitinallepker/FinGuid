import ReactMarkdown from "react-markdown";
import { useEffect, useRef } from "react";

function ChatWindow({ messages, loading }) {

  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages, loading]);

  return (
    <div className="chat-window">

      {messages.map((msg, index) => (
        <div
          key={index}
          className={`message ${msg.sender}`}
        >
          <ReactMarkdown>
            {msg.text.replace(/\n{3,}/g, "\n\n")}
          </ReactMarkdown>
        </div>
      ))}

      {loading && (
        <div className="loading">
          <span></span>
          <span></span>
          <span></span>
        </div>
      )}

      <div ref={bottomRef}></div>

    </div>
  );
}

export default ChatWindow;