import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { fetchEvents, groupEventsForUpcoming } from '../services/api'
import wellnessImage from '../assets/images/www_v4.jpg'
import biathlonPdf from '../assets/2026EasternRegional2INVITATIONforMarch.pdf'

const staticEvents = [
  {
    id: 'static-biathlon-2026',
    title: '2026 Eastern Regional Biathlon Cup #2',
    description: 'Two days of competitive biathlon racing — Sprint on Saturday, Mass Start on Sunday. Open to all USBA and Biathlon Canada members.',
    category: { name: 'Races & Competitions' },
    flyerUrl: biathlonPdf,
    link: '/eastern-regional-biathlon',
    dates: [
      { date: 'March 27, 2026', time: '12:00 PM - 4:00 PM', rawDate: '2026-03-27' },
      { date: 'March 28, 2026', time: '8:00 AM - 12:00 PM', rawDate: '2026-03-28' },
      { date: 'March 29, 2026', time: '8:00 AM - 12:00 PM', rawDate: '2026-03-29' },
    ],
  },
]

const PdfIcon = () => (
  <svg className="pdf-icon" viewBox="0 0 384 512" fill="currentColor">
    <path d="M181.9 256.1c-5-16-4.9-46.9-2-46.9 8.4 0 7.6 36.9 2 46.9zm-1.7 47.2c-7.7 20.2-17.3 43.3-28.4 62.7 18.3-7 39-17.2 62.9-21.9-12.7-9.6-24.9-23.4-34.5-40.8zM86.1 428.1c0 .8 13.2-5.4 34.9-40.2-6.7 6.3-29.1 24.5-34.9 40.2zM248 160h136v328c0 13.3-10.7 24-24 24H24c-13.3 0-24-10.7-24-24V24C0 10.7 10.7 0 24 0h200v136c0 13.2 10.8 24 24 24zm-8 171.8c-20-12.2-33.3-29-42.7-53.8 4.5-18.5 11.6-46.6 6.2-64.2-4.7-29.4-42.4-26.5-47.8-6.8-5 18.3-.4 44.1 8.1 77-11.6 27.6-28.7 64.6-40.8 85.8-.1 0-.1.1-.2.1-27.1 13.9-73.6 44.5-54.5 68 5.6 6.9 16 10 21.5 10 17.9 0 35.7-18 61.1-61.8 25.8-8.5 54.1-19.1 79-23.2 21.7 11.8 47.1 19.5 64 19.5 29.2 0 31.2-32 19.7-43.4-13.9-13.6-54.3-9.7-73.6-7.2zM377 105L279 7c-4.5-4.5-10.6-7-17-7h-6v128h128v-6.1c0-6.3-2.5-12.4-7-16.9zm-74.1 255.3c4.1-2.7-2.5-11.9-42.8-9 37.1 15.8 42.8 9 42.8 9z"/>
  </svg>
)

function UpcomingEvents() {
  const [events, setEvents] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    async function loadEvents() {
      let groupedEvents = []

      try {
        setLoading(true)
        setError(null)

        const data = await fetchEvents({ includePast: false })
        groupedEvents = groupEventsForUpcoming(data)
      } catch (err) {
        console.error('Failed to fetch events:', err)
        setError('Failed to load some events. Showing locally-listed events.')
      } finally {
        // Always merge static events, even if API failed
        const apiTitles = new Set(groupedEvents.map(e => e.title.toLowerCase()))
        const uniqueStatic = staticEvents.filter(
          e => !apiTitles.has(e.title.toLowerCase())
        )
        const allEvents = [...groupedEvents, ...uniqueStatic]

        allEvents.sort((a, b) => {
          const dateA = a.dates[0]?.rawDate || ''
          const dateB = b.dates[0]?.rawDate || ''
          return dateA.localeCompare(dateB)
        })

        setEvents(allEvents)
        setLoading(false)
      }
    }

    loadEvents()
  }, [])

  return (
    <div className="events-page">
      {/* Hero Section */}
      <section className="events-hero">
        <div className="hero-overlay">
          <div className="container">
            <div className="events-hero-content">
              <h1>Upcoming Events</h1>
              <p>
                The Fort Kent Outdoor Center promotes healthy outdoor lifestyles by providing
                a first-rate facility, outdoor trail system, and recreational activities for
                members, athletes, and visitors.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Featured Event */}
      <section className="section section-gradient">
        <div className="container">
          <div className="two-col-grid">
            <div className="image-col">
              <div className="image-card">
                <img
                  src={wellnessImage}
                  alt="Women's Winter Wellness Day"
                  loading="lazy"
                />
              </div>
            </div>
            <div className="content-col">
              <div className="badge badge-success">
                <span className="badge-dot"></span>
                Featured Event
              </div>
              <h2 className="section-title">Women's Winter Wellness Day</h2>
              <p className="content-text">
                Join us on <strong>Saturday, March 7th, 2026</strong> from <strong>8:30 AM - 3:30 PM</strong> for
                a day dedicated to wellness, community, and outdoor adventure at the Fort Kent Outdoor Center.
              </p>
              <div className="button-group">
                <Link to="/womens-wellness-day" className="btn btn-primary">
                  More Info
                </Link>
                <button
                  type="button"
                  className="btn btn-outline"
                  onClick={() => document.getElementById('events-list').scrollIntoView({ behavior: 'smooth' })}
                >
                  View All Events
                  <svg className="icon-arrow" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true" style={{ transform: 'rotate(90deg)' }}>
                    <path fillRule="evenodd" clipRule="evenodd" d="M10.293 3.293a1 1 0 0 1 1.414 0l6 6a1 1 0 0 1 0 1.414l-6 6a1 1 0 0 1-1.414-1.414L14.586 11H3a1 1 0 1 1 0-2h11.586l-4.293-4.293a1 1 0 0 1 0-1.414z" />
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Events Grid Section */}
      <section id="events-list" className="section">
        <div className="container">
          {error && (
            <div className="alert alert-warning" style={{ marginBottom: '2rem' }}>
              {error}
            </div>
          )}

          {loading && (
            <div className="loading-state" style={{ textAlign: 'center', padding: '3rem' }}>
              <p>Loading events...</p>
            </div>
          )}

          {!loading && events.length === 0 && !error && (
            <div className="empty-state" style={{ textAlign: 'center', padding: '3rem' }}>
              <h2>No Upcoming Events</h2>
              <p>Check back soon for new events!</p>
            </div>
          )}

          {!loading && events.length > 0 && (
            <div className="events-grid">
              {events.map((event) => (
                <article key={event.id} className="event-card">
                  <div className="event-category-badge">
                    {event.category?.name || 'Event'}
                  </div>
                  <h2 className="event-title">{event.title}</h2>
                  {event.description && (
                    <p className="event-description">{event.description}</p>
                  )}
                  <div className="event-dates">
                    <strong>Event Date(s):</strong>
                    {event.dates.map((dateInfo, idx) => (
                      <div key={idx} className="event-date-row">
                        <span className="event-date">{dateInfo.date}</span>
                        <span className="event-time">{dateInfo.time}</span>
                      </div>
                    ))}
                  </div>
                  {event.link && (
                    <Link to={event.link} className="btn btn-primary btn-sm" style={{ marginBottom: 'var(--space-sm)' }}>
                      More Info
                    </Link>
                  )}
                  {event.flyerUrl && (
                    <a
                      href={event.flyerUrl}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="event-flyer-link"
                      title="View Event Flyer"
                    >
                      <PdfIcon />
                      <span>View Event Flyer</span>
                    </a>
                  )}
                </article>
              ))}
            </div>
          )}
        </div>
      </section>
    </div>
  )
}

export default UpcomingEvents
