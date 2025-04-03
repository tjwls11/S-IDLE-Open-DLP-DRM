'use client'

import { useEffect, useState } from 'react'
import './globals.css'
import { useRouter } from 'next/navigation'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  const [message, setMessage] = useState('')
  const router = useRouter()

  useEffect(() => {
    fetch('http://127.0.0.1:8000/')
      .then((response) => response.json())
      .then((data) => setMessage(data.message))
  }, [])

  return (
    <html lang="en">
      <body className="bg-gray-100">
        <div className="text-5xl text-center mt-20 text-black">{message}</div>
        {children}
      </body>
    </html>
  )
}
