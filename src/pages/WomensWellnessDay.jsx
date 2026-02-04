import { useEffect } from 'react'
import wellnessFlyer from '../assets/images/www_v3.png'

const CheckIcon = () => (
  <svg className="benefit-icon" viewBox="0 0 20 20" fill="currentColor">
    <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
  </svg>
)

const activities = [
  { name: 'Nordic Skiing', icon: '⛷️' },
  { name: 'Art', icon: '🎨' },
  { name: 'Snowshoeing', icon: '🥾' },
  { name: 'Socializing', icon: '☕' }
]

const included = [
  'Lunch and snacks provided',
  'Trail passes included',
  'All equipment provided (or bring your own)',
  'No prior ski or snowshoe experience required',
  'All abilities welcome and celebrated'
]

// Placeholder - Laura will send detailed schedule
const schedule = [
  { time: '8:30 AM', activity: 'Check-in & Welcome' },
  { time: '9:00 AM', activity: 'Morning Activities Begin' },
  { time: '12:00 PM', activity: 'Lunch' },
  { time: '1:00 PM', activity: 'Afternoon Activities' },
  { time: '3:30 PM', activity: 'Event Concludes' }
]

// Placeholder - Laura will send detailed list
const collectionItems = [
  'Personal care items',
  'Hygiene products',
  'Additional items TBA'
]

function WomensWellnessDay() {
  useEffect(() => {
    // Load Stripe pricing table script
    const script = document.createElement('script')
    script.src = 'https://js.stripe.com/v3/pricing-table.js'
    script.async = true
    document.body.appendChild(script)

    return () => {
      const existingScript = document.querySelector('script[src="https://js.stripe.com/v3/pricing-table.js"]')
      if (existingScript) {
        document.body.removeChild(existingScript)
      }
    }
  }, [])

  return (
    <div className="wellness-page">
      {/* Hero Section */}
      <section className="wellness-hero">
        <div className="hero-overlay">
          <div className="container">
            <div className="wellness-hero-content">
              <h1>Women's Winter Wellness Day</h1>
              <p className="hero-subtitle">
                Join us for skiing, art, snowshoeing, and socializing!
              </p>
              <div className="hero-details">
                <span className="hero-date">Saturday, March 7, 2026</span>
                <span className="hero-time">8:30 AM - 3:30 PM</span>
              </div>
              <a href="#register" className="btn btn-primary btn-lg">
                Register Now
              </a>
            </div>
          </div>
        </div>
      </section>

      {/* Event Overview */}
      <section className="section">
        <div className="container">
          <div className="two-col-grid">
            <div className="content-col">
              <h2 className="section-title">About the Event</h2>
              <p className="section-intro">
                Fort Kent Outdoor Center invites all women 18+ to our annual Women's Winter
                Wellness Day. Whether you're an experienced skier or trying snowshoeing for
                the first time, this day is designed for you to enjoy the outdoors, try new
                activities, and connect with other women in our community.
              </p>

              {/* Activities Grid */}
              <div className="activities-grid">
                {activities.map((activity, index) => (
                  <div key={index} className="activity-badge">
                    <span className="activity-icon">{activity.icon}</span>
                    <span className="activity-name">{activity.name}</span>
                  </div>
                ))}
              </div>
            </div>
            <div className="image-col">
              <img
                src={wellnessFlyer}
                alt="Women's Winter Wellness Day Flyer"
                className="wellness-flyer-image"
              />
            </div>
          </div>
        </div>
      </section>

      {/* What's Included */}
      <section className="section section-alt">
        <div className="container">
          <h2 className="section-title text-center">What's Included</h2>
          <div className="benefits-centered">
            <ul className="benefits-list">
              {included.map((item, index) => (
                <li key={index} className="benefit-item">
                  <CheckIcon />
                  <span>{item}</span>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </section>

      {/* Pricing Section */}
      <section className="section">
        <div className="container">
          <h2 className="section-title text-center">Registration</h2>
          <div className="pricing-grid">
            <div className="pricing-card pricing-featured">
              <div className="pricing-badge">Early Bird</div>
              <div className="pricing-amount">$40</div>
              <div className="pricing-deadline">Register by February 28</div>
            </div>
            <div className="pricing-card">
              <div className="pricing-amount">$45</div>
              <div className="pricing-deadline">March 1 - 7</div>
            </div>
          </div>
        </div>
      </section>

      {/* Schedule Section */}
      <section className="section section-alt">
        <div className="container">
          <h2 className="section-title text-center">Schedule</h2>
          <p className="section-intro text-center">
            Detailed schedule coming soon!
          </p>
          <div className="schedule-list">
            {schedule.map((item, index) => (
              <div key={index} className="schedule-item">
                <span className="schedule-time">{item.time}</span>
                <span className="schedule-activity">{item.activity}</span>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Hope & Justice Collection */}
      <section className="section">
        <div className="container">
          <div className="collection-section">
            <h2 className="section-title text-center">Hope & Justice Collection</h2>
            <p className="section-intro text-center">
              We will be collecting donations of personal care items for our Local Hope & Justice
              project. Your generosity helps support those in need in our community.
            </p>
            <div className="collection-items">
              <h3>Suggested Items:</h3>
              <ul className="collection-list">
                {collectionItems.map((item, index) => (
                  <li key={index}>{item}</li>
                ))}
              </ul>
              <p className="collection-note">
                <em>Detailed list of needed items coming soon!</em>
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Registration/Payment Section */}
      <section className="section section-dark" id="register">
        <div className="container">
          <div className="section-header text-center">
            <h2 className="section-title text-inverse">Complete Your Registration</h2>
            <p className="section-intro text-inverse">
              Secure your spot for Women's Winter Wellness Day.
              Payment processing powered by Stripe.
            </p>
          </div>
          <div className="stripe-container">
            <stripe-pricing-table
              pricing-table-id="prctbl_1Sx8w0CNUZB7PvDyLe8MG74y"
              publishable-key="pk_live_51K7Op9CNUZB7PvDyrt4Y4E7RoduQLDdUa8S0qfc2fZKdyHLcBbYXUAXAvS5UAzTWjGkIaCuxiTBLqFXYi01Xyb8N00CqrkdT6e">
            </stripe-pricing-table>
          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section className="section">
        <div className="container">
          <div className="centered-content text-center">
            <h2 className="section-title">Questions?</h2>
            <p className="content-text">
              For more information about Women's Winter Wellness Day, please contact us.
            </p>
            <div className="contact-links">
              <a href="https://www.fortkentoc.org" target="_blank" rel="noopener noreferrer" className="btn btn-outline">
                Visit fortkentoc.org
              </a>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}

export default WomensWellnessDay
