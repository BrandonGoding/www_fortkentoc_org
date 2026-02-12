import { useEffect } from 'react'
import { useLocation } from 'react-router-dom'
import { Outlet } from 'react-router-dom'
import Header from './Header'
import Footer from './Footer'

function Layout() {
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
      <div className="announcement-banner">
        <div>Hosting 2026 Maine State High School Nordic Championship Feb 16–17</div>
        <div>Trail access and parking may be limited — please use Red Barn Trailhead for recreational skiing</div>
      </div>
      <main className="main-content">
        <Outlet />
      </main>
      <Footer />
    </div>
  )
}

export default Layout
