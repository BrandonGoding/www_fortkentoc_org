import biathlonImage from '../assets/images/programs/east-region-biathlon.jpg'
import biathlonPdf from '../assets/2026EasternRegional2INVITATIONforMarch.pdf'

const CheckIcon = () => (
  <svg className="benefit-icon" viewBox="0 0 20 20" fill="currentColor">
    <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
  </svg>
)

const schedule = [
  {
    day: 'Friday, March 27',
    items: [
      { time: '12:00 – 4:00 PM', activity: 'Official Training' },
      { time: '4:30 PM', activity: 'Team Captain\'s Meeting', details: 'Main Lodge (Zoom link for registered coaches)' }
    ]
  },
  {
    day: 'Saturday, March 28 — Sprint',
    items: [
      { time: '8:00 AM', activity: 'Competition Office opens for bib pick-up' },
      { time: '8:00', activity: 'Equipment Check' },
      { time: '9:00', activity: 'Zero' },
      { time: '10:00 AM', activity: 'Race Start — Sprint' },
      { time: '12:00 PM', activity: 'Awards in Stadium' }
    ]
  },
  {
    day: 'Sunday, March 29 — Mass Start',
    items: [
      { time: '8:00 AM', activity: 'Competition Office opens for bib pick-up' },
      { time: '9:00', activity: 'Zero (all classes)' },
      { time: '10:00 AM', activity: 'Race Start — Mass Start (IBU Classes)' },
      { time: '11:30 AM', activity: 'Mass Start Masters & U13/15 (if needed)' },
      { time: '12:00 PM', activity: 'Awards in Stadium' }
    ]
  }
]

const included = [
  'Open to all USBA and Biathlon Canada members in good standing',
  'Sprint race on Saturday, Mass Start on Sunday',
  'Official training on Friday',
  'Wax rooms available ($75/day — reserve during registration)',
  'Trail passes for unofficial training ($15/day)',
  'Start lists and results posted on Zone4'
]

const contacts = [
  { name: 'Pat Theriault', role: 'Logistics', email: 'theriault.pat@gmail.com', phone: '207-436-1298' },
  { name: 'Laura Audibert', role: 'Logistics', email: 'la4568@roadrunner.com', phone: '207-231-0048' },
  { name: 'Carl Theriault', role: 'Technical Questions', email: 'carlther17@gmail.com' },
  { name: 'Dona Saucier', role: 'Housing / Hotels', email: 'dona.saucier@gmail.com' }
]

function EasternRegionalBiathlon() {
  return (
    <div className="wellness-page">
      {/* Hero Section */}
      <section className="events-hero">
        <div className="hero-overlay">
          <div className="container">
            <div className="wellness-hero-content">
              <h1>2026 Eastern Regional Biathlon Cup #2</h1>
              <p className="hero-subtitle">
                Two days of competitive biathlon racing at Fort Kent Outdoor Center
              </p>
              <div className="hero-details">
                <span className="hero-date">March 28–29, 2026</span>
                <span className="hero-time">Fort Kent, Maine</span>
              </div>
              <a
                href="https://zone4.ca/event/2026/BiathlonCup2"
                className="btn btn-primary btn-lg"
                target="_blank"
                rel="noopener noreferrer"
              >
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
                The Fort Kent Outdoor Center is proud to host the 2026 Eastern Regional Biathlon
                Cup #2, featuring Sprint races on Saturday and Mass Start races on Sunday. The event
                is open to all members of USBA or Biathlon Canada in good standing. Please have your
                current registration card or number available at check-in.
              </p>
              <p className="content-text">
                Competition timing and schedule are subject to change based on registration numbers.
                A detailed program will be provided at the Team Captain's Meeting on Friday afternoon.
                Current IBU event and competition rules will be in effect.
              </p>
            </div>
            <div className="image-col">
              <a href={biathlonPdf} target="_blank" rel="noopener noreferrer">
                <img
                  src={biathlonImage}
                  alt="Eastern Regional Biathlon Cup at Fort Kent Outdoor Center"
                  className="wellness-flyer-image"
                />
              </a>
              <p className="flyer-download-text">
                <a href={biathlonPdf} target="_blank" rel="noopener noreferrer">
                  Download the full event invitation (PDF)
                </a>
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* What's Included */}
      <section className="section section-alt">
        <div className="container">
          <h2 className="section-title text-center">Event Details</h2>
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

      {/* Registration / Pricing */}
      <section className="section">
        <div className="container">
          <h2 className="section-title text-center">Registration & Entry Fees</h2>
          <div className="pricing-grid">
            <div className="pricing-card pricing-featured">
              <div className="pricing-badge">U13 / U15</div>
              <div className="pricing-amount">$30</div>
              <div className="pricing-deadline">Per race</div>
            </div>
            <div className="pricing-card pricing-featured">
              <div className="pricing-badge">All Other Classes</div>
              <div className="pricing-amount">$40</div>
              <div className="pricing-deadline">Per race</div>
            </div>
            <div className="pricing-card">
              <div className="pricing-badge">Late Fee</div>
              <div className="pricing-amount">+$20</div>
              <div className="pricing-deadline">March 23–25</div>
            </div>
          </div>
          <div className="centered-content text-center" style={{ marginTop: 'var(--space-xl)' }}>
            <p className="content-text">
              <strong>Registration deadline:</strong> Wednesday, March 25 at 7:00 PM EST
            </p>
            <a
              href="https://zone4.ca/event/2026/BiathlonCup2"
              className="btn btn-primary btn-lg"
              target="_blank"
              rel="noopener noreferrer"
            >
              Register on Zone4
            </a>
          </div>
        </div>
      </section>

      {/* Competition Schedule */}
      <section className="section section-alt">
        <div className="container">
          <h2 className="section-title text-center">Competition Schedule</h2>
          {schedule.map((day, dayIndex) => (
            <div key={dayIndex} style={{ marginBottom: 'var(--space-2xl)' }}>
              <h3 className="text-center" style={{ marginBottom: 'var(--space-lg)' }}>{day.day}</h3>
              <div className="schedule-list">
                {day.items.map((item, index) => (
                  <div key={index} className="schedule-item">
                    <span className="schedule-time">{item.time}</span>
                    <div className="schedule-activity">
                      <span className="schedule-activity-title">{item.activity}</span>
                      {item.details && (
                        <ul className="schedule-details">
                          <li>{item.details}</li>
                        </ul>
                      )}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Competition Classes */}
      <section className="section">
        <div className="container">
          <h2 className="section-title text-center">Competition Classes</h2>
          <p className="content-text text-center" style={{ marginBottom: 'var(--space-xl)' }}>
            Full class details including distances, loop lengths, targets, and rifle requirements
            are available in the{' '}
            <a href={biathlonPdf} target="_blank" rel="noopener noreferrer">
              event invitation PDF
            </a>.
          </p>

          <div className="collection-section">
            <h3>Sprint — Saturday, March 28</h3>
            <div className="biathlon-classes-table" style={{ overflowX: 'auto' }}>
              <table className="classes-table">
                <thead>
                  <tr>
                    <th>Class</th>
                    <th>Distance</th>
                    <th>Loop</th>
                    <th>Targets</th>
                  </tr>
                </thead>
                <tbody>
                  <tr><td>SR Men</td><td>10 km</td><td>3.3 km</td><td>P-S</td></tr>
                  <tr><td>SR Women</td><td>7.5 km</td><td>2.5 km</td><td>P-S</td></tr>
                  <tr><td>U21 / Junior M</td><td>10 km</td><td>3.3 km</td><td>P-S</td></tr>
                  <tr><td>U21 / Junior W</td><td>7.5 km</td><td>2.5 km</td><td>P-S</td></tr>
                  <tr><td>U19 / Youth M</td><td>7.5 km</td><td>2.5 km</td><td>P-S</td></tr>
                  <tr><td>U19 / Youth W</td><td>6 km</td><td>2 km</td><td>P-S</td></tr>
                  <tr><td>U17 M/W</td><td>6 km</td><td>2 km</td><td>P-S</td></tr>
                  <tr><td>Master 30–70</td><td>4.5–7.5 km</td><td>1.5–2.5 km</td><td>P-S</td></tr>
                  <tr><td>U15 B/G</td><td>4.5 km</td><td>1.5 km</td><td>P-P</td></tr>
                  <tr><td>U13 B/G</td><td>3 km</td><td>1 km</td><td>P-P</td></tr>
                </tbody>
              </table>
            </div>
          </div>

          <div className="collection-section" style={{ marginTop: 'var(--space-2xl)' }}>
            <h3>Mass Start — Sunday, March 29</h3>
            <div className="biathlon-classes-table" style={{ overflowX: 'auto' }}>
              <table className="classes-table">
                <thead>
                  <tr>
                    <th>Class</th>
                    <th>Distance</th>
                    <th>Loop</th>
                    <th>Targets</th>
                  </tr>
                </thead>
                <tbody>
                  <tr><td>SR Men</td><td>15 km</td><td>2.5 km</td><td>P-P-S-S</td></tr>
                  <tr><td>SR Women</td><td>12 km</td><td>2 km</td><td>P-P-S-S</td></tr>
                  <tr><td>U21 / Junior M</td><td>12 km</td><td>2 km</td><td>P-P-S-S</td></tr>
                  <tr><td>U21 / Junior W</td><td>9 km</td><td>1.5 km</td><td>P-P-S-S</td></tr>
                  <tr><td>U19 / Youth M</td><td>12 km</td><td>2 km</td><td>P-P-S-S</td></tr>
                  <tr><td>U19 / Youth W</td><td>9 km</td><td>1.5 km</td><td>P-P-S-S</td></tr>
                  <tr><td>U17 M/W</td><td>9 km</td><td>1.5 km</td><td>P-P-S-S</td></tr>
                  <tr><td>Master 30–70</td><td>6–12 km</td><td>1–2 km</td><td>P-P-S-S</td></tr>
                  <tr><td>U15 B/G</td><td>5 km</td><td>1 km</td><td>P-S-S</td></tr>
                  <tr><td>U13 B/G</td><td>5 km</td><td>1 km</td><td>P-S-S</td></tr>
                </tbody>
              </table>
            </div>
            <p className="content-text" style={{ marginTop: 'var(--space-md)', fontSize: 'var(--text-sm)' }}>
              Mass Start day will be configured as a Mass Start 60. Final groupings decided after
              registration closes March 25. Start seeding determined by Sprint results.
            </p>
          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section className="section section-dark">
        <div className="container">
          <div className="centered-content text-center">
            <h2 className="section-title text-inverse">Contact Information</h2>
            <p className="content-text text-light" style={{ marginBottom: 'var(--space-xl)' }}>
              Have questions about the event? Reach out to the organizing team.
            </p>
            <div className="contact-grid">
              {contacts.map((contact, index) => (
                <div key={index} className="contact-card">
                  <h3 className="contact-name">{contact.name}</h3>
                  <p className="contact-role">{contact.role}</p>
                  <a href={`mailto:${contact.email}`} className="contact-email">{contact.email}</a>
                  {contact.phone && <p className="contact-phone">{contact.phone}</p>}
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}

export default EasternRegionalBiathlon
