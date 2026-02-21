import { useState } from 'react'
import { Link } from 'react-router-dom'
import logo from '../assets/fkoc-logo.jpeg'
import { useWebcam } from './WebcamContext'

function Header() {
  const { openWebcam } = useWebcam()
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false)
  const [openDropdown, setOpenDropdown] = useState(null)

  const toggleDropdown = (name) => {
    setOpenDropdown(openDropdown === name ? null : name)
  }

  const closeAll = () => {
    setOpenDropdown(null)
    setMobileMenuOpen(false)
  }

  return (
    <nav className="nav-header">
      <div className="nav-container">
        <Link to="/" className="nav-logo" onClick={closeAll}>
          <img src={logo} className="nav-logo-img" alt="Fort Kent Outdoor Center Logo" />
          <span className="sr-only">Fort Kent Outdoor Center</span>
        </Link>

        <button
          className="mobile-menu-btn"
          onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
          aria-expanded={mobileMenuOpen}
          aria-controls="mobile-menu"
        >
          <span className="sr-only">Open main menu</span>
          {!mobileMenuOpen ? (
            <svg className="menu-icon" fill="currentColor" viewBox="0 0 20 20">
              <path fillRule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clipRule="evenodd" />
            </svg>
          ) : (
            <svg className="menu-icon" fill="currentColor" viewBox="0 0 20 20">
              <path fillRule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clipRule="evenodd" />
            </svg>
          )}
        </button>

        <div className={`nav-menu ${mobileMenuOpen ? 'nav-menu-open' : ''}`} id="mobile-menu">
          <ul className="nav-list">
            {/* About Us Dropdown */}
            <li className="nav-item nav-item-dropdown">
              <button
                className="nav-dropdown-btn"
                onClick={() => toggleDropdown('about')}
                aria-expanded={openDropdown === 'about'}
              >
                About Us
                <svg className="dropdown-arrow" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clipRule="evenodd" />
                </svg>
              </button>
              <div className={`nav-dropdown ${openDropdown === 'about' ? 'nav-dropdown-open' : ''}`}>
                <ul className="nav-dropdown-list">
                  <li><Link to="/about-us" onClick={closeAll}>Who we are</Link></li>
                  <li><Link to="/facilities" onClick={closeAll}>Facilities</Link></li>
                  <li><Link to="/trails" onClick={closeAll}>Trails</Link></li>
                  <li><Link to="/endowment" onClick={closeAll}>Endowment</Link></li>
                  <li><Link to="/policies-and-safety" onClick={closeAll}>Policies</Link></li>
                </ul>
              </div>
            </li>

            {/* Programs Dropdown */}
            <li className="nav-item nav-item-dropdown">
              <button
                className="nav-dropdown-btn"
                onClick={() => toggleDropdown('programs')}
                aria-expanded={openDropdown === 'programs'}
              >
                Programs
                <svg className="dropdown-arrow" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clipRule="evenodd" />
                </svg>
              </button>
              <div className={`nav-dropdown ${openDropdown === 'programs' ? 'nav-dropdown-open' : ''}`}>
                <ul className="nav-dropdown-list">
                  <li><Link to="/coaching-programs#fkoc-coaching" onClick={closeAll}>Coaches</Link></li>
                  <li><Link to="/coaching-programs#pg-training" onClick={closeAll}>(PG) Training Program</Link></li>
                  <li><Link to="/coaching-programs#residence" onClick={closeAll}>Jalbert Biathlon Residence</Link></li>
                  <li><Link to="/coaching-programs#ski-program" onClick={closeAll}>Jalbert Ski Program</Link></li>
                  <li><Link to="/coaching-programs#biathlon-program" onClick={closeAll}>Jalbert Biathlon Program</Link></li>
                </ul>
              </div>
            </li>

            {/* Trails/Fees Dropdown */}
            <li className="nav-item nav-item-dropdown">
              <button
                className="nav-dropdown-btn"
                onClick={() => toggleDropdown('trails')}
                aria-expanded={openDropdown === 'trails'}
              >
                Trails/Fees
                <svg className="dropdown-arrow" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clipRule="evenodd" />
                </svg>
              </button>
              <div className={`nav-dropdown ${openDropdown === 'trails' ? 'nav-dropdown-open' : ''}`}>
                <ul className="nav-dropdown-list">
                  <li><Link to="/trails" onClick={closeAll}>Trail Maps</Link></li>
                  <li><Link to="/day-passes" onClick={closeAll}>Day Passes</Link></li>
                  <li><Link to="/rentals" onClick={closeAll}>Rentals</Link></li>
                  <li><Link to="/memberships" onClick={closeAll}>Memberships</Link></li>
                </ul>
              </div>
            </li>

            {/* Events Dropdown */}
            <li className="nav-item nav-item-dropdown">
              <button
                className="nav-dropdown-btn"
                onClick={() => toggleDropdown('events')}
                aria-expanded={openDropdown === 'events'}
              >
                Events
                <svg className="dropdown-arrow" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clipRule="evenodd" />
                </svg>
              </button>
              <div className={`nav-dropdown ${openDropdown === 'events' ? 'nav-dropdown-open' : ''}`}>
                <ul className="nav-dropdown-list">
                  <li><Link to="/event-calendar" onClick={closeAll}>Calendar</Link></li>
                  <li><Link to="/upcoming-events" onClick={closeAll}>Upcoming Events</Link></li>
                  <li><Link to="/womens-wellness-day" onClick={closeAll}>Women's Wellness Day</Link></li>
                  <li><Link to="/eastern-regional-biathlon" onClick={closeAll}>Eastern Regional Biathlon</Link></li>
                </ul>
              </div>
            </li>

            {/* Location (no dropdown) */}
            <li className="nav-item">
              <Link to="/location" className="nav-link" onClick={closeAll}>Location</Link>
            </li>

            {/* Action buttons - mobile */}
            <li className="nav-item nav-item-donate-mobile">
              <button
                type="button"
                className="btn btn-webcam"
                onClick={() => { openWebcam(); closeAll() }}
              >
                Live Webcam
              </button>
              <a
                href="https://buy.stripe.com/9AQ3g1dXm5cc1m83ch"
                className="btn btn-donate"
                target="_blank"
                rel="noopener noreferrer"
              >
                Donate
              </a>
            </li>
          </ul>
        </div>

        {/* Action buttons - desktop */}
        <div className="nav-actions-desktop">
          <button
            type="button"
            className="btn btn-webcam-desktop"
            onClick={openWebcam}
          >
            Live Webcam
          </button>
          <a
            href="https://buy.stripe.com/9AQ3g1dXm5cc1m83ch"
            className="btn btn-accent"
            target="_blank"
            rel="noopener noreferrer"
          >
            Donate
          </a>
        </div>
      </div>
    </nav>
  )
}

export default Header
