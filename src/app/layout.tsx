"use client";

import { useEffect, useState } from "react";
import "./globals.css";

export default function RootLayout() {  
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch("http://34.41.82.222:8000/")  
      .then((response) => response.json())
      .then((data) => setMessage(data.message));
  }, []);

  return (
    <html lang="en">
      <body className="bg-gray-100">
        <div className="text-5xl text-center mt-20">
          {message}
        </div>
      </body>
    </html>
  );
}
