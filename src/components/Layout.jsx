import { useEffect } from 'react'
import { useLocation } from 'react-router-dom'
import { Outlet } from 'react-router-dom'
import Header from './Header'
import Footer from './Footer'
import { WebcamProvider, useWebcam } from './WebcamContext'

const CloseIcon = () => (
  <svg className="icon-close" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
    <path d="M18 6L6 18M6 6l12 12" />
  </svg>
)

function WebcamModal() {
  const { webcamOpen, closeWebcam } = useWebcam()

  if (!webcamOpen) return null

  return (
    <div className="modal-overlay" onClick={closeWebcam}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <button
          type="button"
          className="modal-close-btn"
          onClick={closeWebcam}
          aria-label="Close modal"
        >
          <CloseIcon />
        </button>
        <img
          src="https://www.fortkentoc.org/webcam/image.jpg"
          alt="FKOC webcam view of the stadium - full size"
          className="modal-image"
        />
        <p className="modal-caption">Stadium webcam - Updated every minute</p>
      </div>
    </div>
  )
}

function LayoutInner() {
  const location = useLocation()

  useEffect(() => {
    // Check if there's a hash in the URL
    if (location.hash) {
      // Remove the # symbol
      const elementId = location.hash.substring(1)
      const element = document.getElementById(elementId)

      if (element) {
        // Small delay to ensure the page has rendered
        setTimeout(() => {
          element.scrollIntoView({ behavior: 'smooth', block: 'start' })
        }, 100)
      }
    } else {
      // If no hash, scroll to top of page
      window.scrollTo({ top: 0, behavior: 'smooth' })
    }
  }, [location])

  return (
    <div className="app">
      <Header />
      <main className="main-content">
        <Outlet />
      </main>
      <Footer />
      <WebcamModal />
    </div>
  )
}

function Layout() {
  return (
    <WebcamProvider>
      <LayoutInner />
    </WebcamProvider>
  )
}

export default Layout
