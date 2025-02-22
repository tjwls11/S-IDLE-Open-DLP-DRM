import React from 'react'
import Link from 'next/link'

export default function Home() {
  return (
    <div>
      <Link
        href="/"
        className="fixed bottom-8 right-8 p-4 bg-green-300 rounded-full text-white text-2xl flex items-center justify-center"
      >
        🤖
      </Link>
    </div>
  )
}
