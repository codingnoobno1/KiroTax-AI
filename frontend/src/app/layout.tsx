import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'
import { Toaster } from 'sonner'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'KiroTax AI - AI CA Billing & GST Automation',
  description: 'AI-powered billing, GST automation, and tax filing platform for Viksit Bharat',
  keywords: ['GST', 'Billing', 'AI', 'Tax', 'India', 'MSME', 'CA'],
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        {children}
        <Toaster position="top-right" richColors />
      </body>
    </html>
  )
}
