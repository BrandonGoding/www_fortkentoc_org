const InfoIcon = () => (
  <svg className="info-icon" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 16h-1v-4h-1m1-4h.01M21 12c0 4.97-4.03 9-9 9s-9-4.03-9-9 4.03-9 9-9 9 4.03 9 9z" />
  </svg>
)

const contributionLevels = [
  { tier: 'Gold Contributors', range: 'Over $50,000', colorClass: 'tier-gold' },
  { tier: 'Silver Contributors', range: '$10,000 – $50,000', colorClass: 'tier-silver' },
  { tier: 'Bronze Contributors', range: '$5,000 – $10,000', colorClass: 'tier-bronze' },
  { tier: 'Blue Contributors', range: '< $5,000', colorClass: 'tier-blue' }
]

const annualAmounts = ['$50', '$100', '$150', '$200', '$500', '$1,000', '$5,000', '$10,000']

const whyItMatters = [
  'Maintain world-class trails and facilities.',
  'Offer year-round outdoor programs and events.',
  'Support aspiring athletes and community recreation.',
  'Sustain a vital community asset in the St. John Valley.'
]

function Endowment() {
  return (
    <div className="endowment-page">
      {/* Hero Section */}
      <section className="endowment-hero">
        <div className="container">
          <div className="endowment-hero-content">
            <h1>Fort Kent Outdoor Center Endowment</h1>
            <p>Securing the future of year-round outdoor recreation in the St. John Valley.</p>
          </div>
        </div>
      </section>

      {/* Background Section */}
      <section className="section endowment-background">
        <div className="container">
          <div className="endowment-card">
            <h2>Background</h2>
            <div className="endowment-text">
              <p>
                Since the venue's creation in 1998 as the Maine Winter Sports Center, the Libra
                Foundation in Portland, Maine has been the primary funder of operations in Fort Kent
                and at the Nordic Heritage Center in Presque Isle.
              </p>
              <p>
                In 2024 Libra concluded its direct operational support. At that time, the assets
                belonging to the Fort Kent Outdoor Center were formally gifted to our operating Board
                of Directors. For fifteen years, Libra's support helped cover capital improvements,
                maintenance, taxes, insurance, and half of the venue manager's salary. That support
                has now ended, making it increasingly difficult to maintain our daily operations and
                programming.
              </p>
              <p>
                To meet this challenge, FKOC has created an <strong>endowment fund</strong> with the
                Maine Community Foundation to generate annual interest and replace the former
                contributions. Long-time supporter <strong>Phyllis Jalbert</strong> has endorsed the
                initiative and provided the largest contribution to date.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Goal & Progress Section */}
      <section className="section">
        <div className="container">
          <div className="goal-grid">
            {/* Our Goal Card */}
            <div className="endowment-card">
              <h3>Our Goal</h3>
              <p className="goal-text">
                We are seeking to raise <strong>$2.4 million</strong> for the endowment.
              </p>
              <div className="progress-cards">
                <div className="progress-card">
                  <div className="progress-label">Pledged</div>
                  <div className="progress-amount">$1.4M</div>
                  <div className="progress-bar">
                    <div className="progress-fill progress-fill-green" style={{ width: '65%' }} />
                  </div>
                  <div className="progress-percent">65% of goal</div>
                </div>
                <div className="progress-card">
                  <div className="progress-label">Deposited</div>
                  <div className="progress-amount">$1.0M</div>
                  <div className="progress-bar">
                    <div className="progress-fill progress-fill-blue" style={{ width: '40%' }} />
                  </div>
                  <div className="progress-percent">40% of goal (on account)</div>
                </div>
              </div>
              <p className="goal-note">
                Gifts may be made as one-time donations, multi-year pledges, or via transfers of
                stock or property with favorable tax benefits.
              </p>
            </div>

            {/* Why It Matters Card */}
            <div className="endowment-card">
              <h3>Why It Matters</h3>
              <ul className="matters-list">
                {whyItMatters.map((item, index) => (
                  <li key={index}>
                    <span className="bullet" />
                    {item}
                  </li>
                ))}
              </ul>
              <div className="card-cta">
                <a href="mailto:info@fortkentoc.org" className="btn btn-accent">
                  Ask about giving &amp; pledges
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Contribution Levels Section */}
      <section className="section section-alt">
        <div className="container">
          <h2 className="section-title">Methods to Contribute</h2>
          <div className="tiers-grid">
            {contributionLevels.map((level, index) => (
              <div key={index} className={`tier-card ${level.colorClass}`}>
                <div className="tier-name">{level.tier}</div>
                <div className="tier-range">{level.range}</div>
              </div>
            ))}
          </div>

          <div className="endowment-card contribution-details">
            <h3>Annual Contributions</h3>
            <div className="amount-tags">
              {annualAmounts.map((amount, index) => (
                <span key={index} className="amount-tag">{amount}</span>
              ))}
            </div>

            <div className="contribution-grid">
              <div className="contribution-box">
                <h4>Other Ways to Give</h4>
                <ul>
                  <li><span className="small-bullet" /> Stock transfers</li>
                  <li><span className="small-bullet" /> Property transfers</li>
                  <li><span className="small-bullet" /> One-time gifts or multi-year pledges</li>
                </ul>
              </div>
              <div className="contribution-box">
                <h4>Tax Benefits</h4>
                <p>
                  Fort Kent Outdoor Center is a <strong>501(c)(3)</strong> non-profit organization.
                  All donations are fully tax-deductible. Transfers of stock or property may allow
                  donors to avoid capital gains tax.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Contact / CTA Section */}
      <section className="section">
        <div className="container">
          <div className="cta-card">
            <p className="cta-message">
              Thank you for supporting this community gem. Your gift sustains outdoor recreation for
              everyone, year-round.
            </p>
            <div className="cta-buttons">
              <a href="mailto:info@fortkentoc.org" className="btn btn-accent">
                Email: info@fortkentoc.org
              </a>
              <a
                href="https://buy.stripe.com/9AQ3g1dXm5cc1m83ch"
                target="_blank"
                rel="noopener noreferrer"
                className="btn btn-outline-accent"
              >
                Make a One-Time Donation Today!
              </a>
            </div>

            {/* Preferred Donation Method Notice */}
            <div className="donation-notice">
              <div className="notice-icon">
                <InfoIcon />
              </div>
              <div className="notice-content">
                <h4>Preferred Donation Method</h4>
                <div className="notice-text">
                  <p>
                    To help us avoid the 3% credit card processing fee, we kindly encourage donations
                    by check whenever possible.
                  </p>
                  <p>
                    Please make checks payable to <strong>FKOC</strong> and mail to:
                  </p>
                  <address>
                    Fort Kent Outdoor Center<br />
                    P.O. Box 541<br />
                    Fort Kent, ME 04743
                  </address>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}

export default Endowment
