import { useState } from 'react'
import { Link } from 'react-router-dom'

import endowmentImage from '../assets/images/home/endowment.png'

// Icon components
const Icons = {
  Close: () => (
    <svg className="icon-close" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
      <path d="M18 6L6 18M6 6l12 12" />
    </svg>
  ),
  ArrowRight: () => (
    <svg className="icon-arrow" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
      <path fillRule="evenodd" clipRule="evenodd" d="M10.293 3.293a1 1 0 0 1 1.414 0l6 6a1 1 0 0 1 0 1.414l-6 6a1 1 0 0 1-1.414-1.414L14.586 11H3a1 1 0 1 1 0-2h11.586l-4.293-4.293a1 1 0 0 1 0-1.414z" />
    </svg>
  ),
  Info: () => (
    <svg className="icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0z" />
    </svg>
  ),
  Heart: () => (
    <svg className="icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" />
    </svg>
  ),
  Facebook: () => (
    <svg className="icon-sm" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
      <path d="M22 12.06C22 6.51 17.52 2 12 2S2 6.51 2 12.06c0 5.02 3.66 9.19 8.44 9.94v-7.03H7.9v-2.91h2.54V9.41c0-2.5 1.49-3.89 3.77-3.89 1.09 0 2.23.2 2.23.2v2.46h-1.26c-1.24 0-1.63.77-1.63 1.56v1.88h2.78l-.44 2.91h-2.34V22c4.78-.75 8.44-4.92 8.44-9.94Z" />
    </svg>
  ),
  Map: () => (
    <svg className="icon-sm" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
      <path d="M9 3 3 5.5v15L9 18l6 2.5 6-2.5v-15L15 5.5 9 3Zm6 4.118 4-1.667v12.431l-4 1.667V7.118ZM5 7.385l4-1.667v12.431l-4 1.667V7.385Z" />
    </svg>
  ),
  Cloud: () => (
    <svg className="icon-sm" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
      <path d="M6 13a6 6 0 1 1 11.31 3.145A4.5 4.5 0 1 1 14.5 22H8a5 5 0 0 1-2-9.6c0-.134 0-.268.003-.4Z" />
    </svg>
  ),
  Ticket: () => (
    <svg className="icon-sm" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
      <path d="M3 8a3 3 0 0 1 3-3h12a3 3 0 0 1 3 3v2a2 2 0 1 0 0 4v2a3 3 0 0 1-3 3H6a3 3 0 0 1-3-3v-2a2 2 0 1 0 0-4V8Zm6 1h6v6H9V9Z" />
    </svg>
  ),
  Clipboard: () => (
    <svg className="icon-sm" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
      <path d="M9 2a2 2 0 0 0-2 2H5a3 3 0 0 0-3 3v11a3 3 0 0 0 3 3h14a3 3 0 0 0 3-3V7a3 3 0 0 0-3-3h-2a2 2 0 0 0-2-2H9Zm0 2h6v2H9V4Zm3.707 6.293-3.5 3.5 1.414 1.414 2.086-2.086 3.672 3.672 1.414-1.414-5.086-5.086Z" />
    </svg>
  ),
  MapPin: () => (
    <svg className="icon-sm" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
      <path d="M12 2a7 7 0 0 0-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7Zm0 9.5a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5Z" />
    </svg>
  ),
  Expand: () => (
    <svg className="icon-xs" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
      <path d="M12.9 3H17v4.1l-1.6-1.6-4.6 4.6-1.9-1.9 4.6-4.6L12.9 3ZM7 6h2v2H7V6Zm-2 4h4v2H5v-2Zm-2 4h8v2H3v-2Z" />
    </svg>
  ),
}

function Home() {
  const [webcamModalOpen, setWebcamModalOpen] = useState(false)

  return (
    <div className="home-page">
      {/* Hero Section */}
      <section className="hero-section">
        <div className="hero-overlay">
          <div className="container">
            <div className="hero-content-wrapper">
              <h1 className="hero-title">Fort Kent Outdoor Center</h1>
              <p className="hero-text">
                The Fort Kent Outdoor Center promotes healthy outdoor lifestyles by providing a first-rate facility,
                outdoor trail system, and recreational activities for members, athletes, and visitors.
              </p>
              <div className="hero-buttons">
                <Link to="/about-us" className="btn btn-primary-light">Learn More</Link>
                <Link to="/memberships" className="btn btn-outline-light">Become a Member</Link>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Endowment Section */}
      <section className="section section-gradient">
        <div className="container">
          <div className="two-col-grid">
            <div className="content-col">
              <div className="badge badge-success">
                <span className="badge-dot"></span>
                Endowment Fund
              </div>
              <h2 className="section-title">Securing the Future of FKOC</h2>
              <div className="content-text">
                <p>
                  In 2024, with the transition away from Libra Foundation support, the Fort Kent Outdoor Center
                  launched an <strong>endowment fund</strong> with the Maine Community Foundation.
                </p>
                <p>
                  Our goal is to raise <strong>$2.4 million</strong> to sustain year-round operations, athlete
                  development, and community programs. Thanks to generous donors, we've already secured over
                  <strong> 58% of the goal</strong>.
                </p>
                <p>Join us in keeping this community gem thriving for generations to come.</p>
              </div>
              <div className="button-group">
                <Link to="/endowment" className="btn btn-primary">
                  <Icons.Info />
                  Learn More
                </Link>
                <a
                  href="https://buy.stripe.com/9AQ3g1dXm5cc1m83ch"
                  className="btn btn-outline"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  <Icons.Heart />
                  Donate Now
                </a>
              </div>
            </div>
            <div className="image-col">
              <div className="image-card">
                <img
                  src={endowmentImage}
                  alt="Scenic winter trail representing FKOC Endowment"
                  loading="lazy"
                />
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Facebook Section */}
      <section className="section section-dark">
        <div className="container">
          <div className="two-col-grid">
            <div className="content-col">
              <div className="badge badge-success-dark">
                <span className="badge-dot"></span>
                Stay in the loop
              </div>
              <h2 className="section-title text-inverse">
                Follow us for the latest trail conditions &amp; updates
              </h2>
              <p className="content-text text-light">
                We post day-of updates, event reminders, photos, and more. Tap below to visit our page and give us a follow.
              </p>
              <div className="button-group">
                <a
                  href="https://www.facebook.com/FortKentOutdoorCenter/"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="btn btn-primary-light"
                >
                  <Icons.Facebook />
                  Visit us on Facebook
                </a>
              </div>
            </div>
            <div className="image-col">
              <div className="facebook-card">
                <div className="facebook-embed-placeholder">
                  <Icons.Facebook />
                  <p>Visit our Facebook page for the latest updates</p>
                  <a
                    href="https://www.facebook.com/FortKentOutdoorCenter/"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="btn btn-outline btn-sm"
                  >
                    Visit our Facebook
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Webcam/Conditions Section */}
      <section className="section">
        <div className="container">
          <div className="two-col-grid">
            <div className="content-col">
              <div className="badge badge-success">
                <span className="badge-dot"></span>
                Live updates
              </div>
              <h2 className="section-title">Stadium Conditions</h2>
              <p className="content-text">
                Keep up to date on current weather and snow conditions via our stadium webcam.
                A new image is posted every minute.
              </p>
              <div className="info-card">
                <h3>Trail Conditions</h3>
                <p>We use GPS reporting to publish the most recent trail conditions directly from our groomer.</p>
                <Link to="/trails" className="btn btn-primary">
                  Trail Report
                  <Icons.ArrowRight />
                </Link>
              </div>
            </div>
            <div className="image-col">
              <button
                type="button"
                className="webcam-card"
                onClick={() => setWebcamModalOpen(true)}
              >
                <div className="webcam-image-wrapper">
                  <img
                    src="https://www.fortkentoc.org/webcam/image-small.jpg"
                    alt="FKOC webcam view of the stadium"
                    loading="lazy"
                  />
                  <span className="webcam-badge">Updated every minute</span>
                </div>
                <div className="webcam-footer">
                  <span>View full size image</span>
                  <Icons.Expand />
                </div>
              </button>
            </div>
          </div>
        </div>
      </section>

      {/* Trails CTA Section */}
      <section className="section section-dark">
        <div className="container">
          <div className="cta-content">
            <div className="badge badge-success-dark">
              <span className="badge-dot"></span>
              Trail Status &amp; Info
            </div>
            <h2 className="section-title text-inverse">Hoping to hit the trails today?</h2>
            <p className="content-text text-light">
              We have a dedicated group of volunteers who keep our trails in great condition year-round.
              Before you head out, be sure to check our updated trail maps and current conditions.
            </p>

            <ul className="feature-list">
              <li>
                <Icons.Map />
                Regularly updated trail maps
              </li>
              <li>
                <Icons.Cloud />
                Current conditions posted daily
              </li>
            </ul>

            <div className="button-group">
              <Link to="/day-passes" className="btn btn-primary">
                <Icons.Ticket />
                View day pass prices
              </Link>
              <Link to="/trails" className="btn btn-outline-light">
                <Icons.Clipboard />
                Trail conditions
              </Link>
              <Link to="/trails" className="btn btn-outline-light">
                <Icons.MapPin />
                Trail maps
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* Webcam Modal */}
      {webcamModalOpen && (
        <div className="modal-overlay" onClick={() => setWebcamModalOpen(false)}>
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <button
              type="button"
              className="modal-close-btn"
              onClick={() => setWebcamModalOpen(false)}
              aria-label="Close modal"
            >
              <Icons.Close />
            </button>
            <img
              src="https://www.fortkentoc.org/webcam/image.jpg"
              alt="FKOC webcam view of the stadium - full size"
              className="modal-image"
            />
            <p className="modal-caption">Stadium webcam - Updated every minute</p>
          </div>
        </div>
      )}
    </div>
  )
}

export default Home
