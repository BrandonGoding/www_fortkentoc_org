import {useState, useCallback, useMemo} from 'react'
import { Link } from 'react-router-dom'
import FullCalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid'
import { fetchCalendarSessions, transformToCalendarEvents } from '../services/api'

/**
 * Format a datetime string for display.
 */
function formatDateTime(dateTimeStr) {
  if (!dateTimeStr) return null
  const date = new Date(dateTimeStr)
  return {
    date: date.toLocaleDateString('en-US', {
      weekday: 'long',
      year: 'numeric',
      month: 'long',
      day: 'numeric',
    }),
    time: date.toLocaleTimeString('en-US', {
      hour: 'numeric',
      minute: '2-digit',
      hour12: true,
    }),
  }
}

/**
 * Event Detail Modal Component
 */
function EventModal({ event, onClose }) {
  if (!event) return null

  const { title, extendedProps, start, end } = event
  const { description, categoryName } = extendedProps || {}

  const startFormatted = formatDateTime(start)
  const endFormatted = formatDateTime(end)

  // Close on escape key
  const handleKeyDown = (e) => {
    if (e.key === 'Escape') onClose()
  }

  // Close on backdrop click
  const handleBackdropClick = (e) => {
    if (e.target === e.currentTarget) onClose()
  }

  return (
    <div
      className="modal-backdrop"
      onClick={handleBackdropClick}
      onKeyDown={handleKeyDown}
      role="dialog"
      aria-modal="true"
      aria-labelledby="event-modal-title"
    >
      <div className="modal-content event-modal">
        <button
          className="modal-close"
          onClick={onClose}
          aria-label="Close modal"
        >
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M18 6L6 18M6 6l12 12" />
          </svg>
        </button>

        <div className="event-modal-header">
          {categoryName && (
            <span className="event-category-badge">{categoryName}</span>
          )}
          <h2 id="event-modal-title" className="event-modal-title">{title}</h2>
        </div>

        <div className="event-modal-body">
          <div className="event-modal-datetime">
            <div className="event-modal-icon">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <rect x="3" y="4" width="18" height="18" rx="2" ry="2" />
                <line x1="16" y1="2" x2="16" y2="6" />
                <line x1="8" y1="2" x2="8" y2="6" />
                <line x1="3" y1="10" x2="21" y2="10" />
              </svg>
            </div>
            <div className="event-modal-datetime-text">
              {startFormatted && (
                <div className="event-modal-date">{startFormatted.date}</div>
              )}
              <div className="event-modal-time">
                {startFormatted?.time}
                {endFormatted?.time && ` - ${endFormatted.time}`}
              </div>
            </div>
          </div>

          {description && (
            <div className="event-modal-description">
              <p>{description}</p>
            </div>
          )}
        </div>

        <div className="event-modal-footer">
          <Link
            to="/upcoming-events"
            className="btn btn-primary"
            onClick={onClose}
          >
            View All Events
          </Link>
          <button className="btn btn-secondary" onClick={onClose}>
            Close
          </button>
        </div>
      </div>
    </div>
  )
}

function EventCalendar() {
  const [events, setEvents] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [selectedEvent, setSelectedEvent] = useState(null)



  /**
   * Fetch events when the calendar date range changes.
   */
  const handleDatesSet = useCallback(async (dateInfo) => {
    try {
      setLoading(true)
      setError(null)

      const start = dateInfo.startStr.split('T')[0]
      const end = dateInfo.endStr.split('T')[0]

      const sessions = await fetchCalendarSessions({ start, end })
      const calendarEvents = transformToCalendarEvents(sessions)
      setEvents(calendarEvents)
    } catch (err) {
      console.error('Failed to fetch calendar events:', err)
      setError('Failed to load events. Please try again later.')
    } finally {
      setLoading(false)
    }
  }, [])

  /**
   * Handle click on calendar event.
   */
  const handleEventClick = useCallback((clickInfo) => {
    setSelectedEvent(clickInfo.event)
  }, [])

  /**
   * Close the event modal.
   */
  const handleCloseModal = useCallback(() => {
    setSelectedEvent(null)
  }, [])

  return (
    <div className="calendar-page">
      {/* Hero Section */}
      <section className="calendar-hero">
        <div className="hero-overlay">
          <div className="container">
            <div className="calendar-hero-content">
              <h1>Events Calendar</h1>
            </div>
          </div>
        </div>
      </section>

      {/* Calendar Section */}
      <section className="section">
        <div className="container">
          <div className="calendar-wrapper">
            {error && (
              <div className="alert alert-warning" style={{ marginBottom: '1rem' }}>
                {error}
              </div>
            )}

            {loading && events.length === 0 && (
              <div className="calendar-loading" style={{ textAlign: 'center', padding: '2rem' }}>
                <p>Loading events...</p>
              </div>
            )}

            <FullCalendar
              plugins={[dayGridPlugin]}
              initialView="dayGridMonth"
              events={async (info, successCallback, failureCallback) => {
                const start = info.startStr.split('T')[0]
                const end = info.endStr.split('T')[0]

                try {
                  const sessions = await fetchCalendarSessions({
                    start: start,
                    end: end,
                  })

                  successCallback(transformToCalendarEvents(sessions))
                } catch (err) {
                  failureCallback(err)
                }
              }}
              datesSet={handleDatesSet}
              eventClick={handleEventClick}
              headerToolbar={{
                left: 'title',
                center: '',
                right: 'today prev,next'
              }}
              height="auto"
              eventDisplay="block"
              dayMaxEvents={3}
              eventClassNames="calendar-event-clickable"
            />
          </div>
        </div>
      </section>

      {/* Upcoming Events CTA */}
      <section className="section section-alt">
        <div className="container">
          <div className="centered-content text-center">
            <h2 className="section-title">Want More Details?</h2>
            <p className="content-text">
              Check out our upcoming events page for detailed information about
              each event, registration links, and more.
            </p>
            <Link to="/upcoming-events" className="btn btn-primary">
              View Upcoming Events
            </Link>
          </div>
        </div>
      </section>

      {/* Event Detail Modal */}
      {selectedEvent && (
        <EventModal event={selectedEvent} onClose={handleCloseModal} />
      )}
    </div>
  )
}

export default EventCalendar
