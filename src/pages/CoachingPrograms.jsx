// Coach images
import coachBenParadis from '../assets/images/coaches/ben-paradis.png'
import coachCarlTheriault from '../assets/images/coaches/carl-theriault.jpg'
import coachMattMichaud from '../assets/images/coaches/matt-michaud.jpg'
import coachSarahAshley from '../assets/images/coaches/sarah-ashley.jpg'
import coachTorinLaliberte from '../assets/images/coaches/torin-laliberte.jpg'

// Jalbert House images
import jalbertHouse1 from '../assets/images/jalbert-house/jalbert-house-1.jpg'
import jalbertHouse2 from '../assets/images/jalbert-house/jalbert-house-2.jpg'
import jalbertHouse3 from '../assets/images/jalbert-house/jalbert-house-3.jpg'
import jalbertHouse4 from '../assets/images/jalbert-house/jalbert-house-4.jpg'
import jalbertHouse5 from '../assets/images/jalbert-house/jalbert-house-5.jpg'
import jalbertHouse6 from '../assets/images/jalbert-house/jalbert-house-6.jpg'
import jalbertHouse7 from '../assets/images/jalbert-house/jalbert-house-7.jpg'
import jalbertHouse8 from '../assets/images/jalbert-house/jalbert-house-8.jpg'

// Program images
import jalbertSnowplow from '../assets/images/programs/jalbert-snowplow.jpg'
import jalbertClass from '../assets/images/programs/jalbert-class.jpg'
import jalbertBiathlon from '../assets/images/programs/jalbert-biathlon.jpg'
import eastRegionBiathlon from '../assets/images/programs/east-region-biathlon.jpg'

const CheckIcon = () => (
  <svg className="check-icon" viewBox="0 0 20 20" fill="currentColor">
    <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
  </svg>
)

const VideoIcon = () => (
  <svg className="btn-icon" fill="currentColor" viewBox="0 0 20 20">
    <path d="M2 6a2 2 0 012-2h6a2 2 0 012 2v8a2 2 0 01-2 2H4a2 2 0 01-2-2V6zM14.553 7.106A1 1 0 0014 8v4a1 1 0 00.553.894l2 1A1 1 0 0018 13V7a1 1 0 00-1.447-.894l-2 1z" />
  </svg>
)

const coaches = [
  {
    name: 'Ben Paradis',
    role: 'Youth and Masters Nordic Coach',
    image: coachBenParadis,
    bio: 'Ben Paradis has been coaching Nordic skiing for over 30 years and has never had a bad day skiing. No matter what, skiing puts a smile on his face. Ben is especially adept at analyzing and explaining technique to all age levels, and you will surely come back from a refreshing ski in the brisk air with a smile on your face!'
  },
  {
    name: 'Carl Theriault',
    role: 'Program Director',
    image: coachCarlTheriault,
    bio: 'Carl has been involved with coaching skiing and biathlon for the past 23 years, and is a life long lover of anything you can do on skis! Coordinating training programs, range activities, FKOC development, and the local High School Nordic team fill most his days. When he is not working on ski programs and activities, you can find Carl out traveling, or riding horses, bicycles, and motorcycles.'
  },
  {
    name: 'Matt Michaud',
    role: 'Youth and Masters Biathlon Coach',
    image: coachMattMichaud,
    bio: 'An active skier all his life, Matt spent several years as part of the National Guard Biathlon team, and now focuses on volunteering to help us coach our youth and masters biathletes. Two of his boys are currently active in our programs and you can find Matt occasionally jumping in to a biathlon event demonstrating skills he learned during his years with the guard.'
  },
  {
    name: 'Sarah Ashley',
    role: 'Nordic Coach',
    image: coachSarahAshley,
    bio: 'Sarah Ashley is our wonderful middle school and ladies night coach who is an alumni of our high school ski team and she always finds a way to instill and have fun out in the ski trails with a smile on her face!'
  },
  {
    name: 'Torin La Liberté',
    role: 'Venue Manager/Nordic Coach',
    image: coachTorinLaliberte,
    bio: "Torin La Liberte comes to us after 6 years as the head coach of the Clarkson University Cross Country and Nordic Ski teams. While at Clarkson, Torin's teams tallied two USCSA National Championship titles, an NCAA Skiing Championship appearance, and were a perennial powerhouse in the USCSA. When there's not snow on the ground, you can usually find Torin riding his bike or obsessing over ski wax!"
  }
]

const pgPricing = [
  { title: 'Housing $300/Month', detail: 'Utilities and internet included.' },
  { title: 'Coaching/Training $200/Month', detail: 'Includes: Daily training, Race support, Wax supplies, and Team FKOC Uniforms.' },
  { title: 'Ammunition $50/Month', detail: 'Biathletes only' },
  { title: 'Training Camps/Events - In Region', detail: 'We will provide transport/housing/food. You will cover the registration costs.' },
  { title: 'Training Camps/Events - Out of Region', detail: 'We will provide housing and food, you must cover your airfare and registration fees' }
]

const residencePhotos = [
  { src: jalbertHouse1, alt: 'Jalbert House front yard' },
  { src: jalbertHouse2, alt: 'Jalbert House bedroom' },
  { src: jalbertHouse3, alt: 'Jalbert House living space' },
  { src: jalbertHouse4, alt: 'Jalbert House dining area' },
  { src: jalbertHouse5, alt: 'Jalbert House kitchen' },
  { src: jalbertHouse6, alt: 'Jalbert House' },
  { src: jalbertHouse7, alt: 'Jalbert House sign' },
  { src: jalbertHouse8, alt: 'Jalbert House parking' }
]

function CoachingPrograms() {
  return (
    <div className="coaching-page">
      {/* Hero Section */}
      <section className="coaching-hero">
        <div className="hero-overlay">
          <div className="container">
            <div className="coaching-hero-content">
              <h1>Coaching Programs</h1>
              <p>
                Along with many community outings and events offered at the FKOC for our adult
                members, such as annual Welcome Winter evening in early December, and the Band
                and BBQ event in the fall, we also offer ongoing educational programming for youth.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Coaching Team Section */}
      <section className="section" id="fkoc-coaching">
        <div className="container">
          <div className="section-header text-center">
            <h2 className="section-title">The FKOC Coaching Team</h2>
            <p className="section-subtitle">
              Guiding Our Athlete's Outdoor Journey With Expertise and Passion!
            </p>
          </div>
          <div className="coaches-grid">
            {coaches.map((coach, index) => (
              <div key={index} className="coach-card">
                <img src={coach.image} alt={coach.name} className="coach-image" />
                <h3 className="coach-name">{coach.name}</h3>
                <span className="coach-role">{coach.role}</span>
                <p className="coach-bio">{coach.bio}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* PG Training Program Section */}
      <section className="section section-alt" id="pg-training">
        <div className="container">
          <h2 className="section-title text-center">POST GRADUATE (PG) Training PROGRAM</h2>

          <div className="pg-grid">
            <div className="pg-column">
              <div className="pg-block">
                <h3>Description</h3>
                <p>
                  The FKOC Post Graduate program is a high performance training program designed
                  to bring high school graduated Nordic skiers and Biathletes, aged 18-23, to the
                  next level of competitive performance with a dedicated annual full time training
                  program.
                </p>
              </div>
              <div className="pg-block">
                <h3>Coaches</h3>
                <p>
                  Coaching responsibilities are shared between Carl Theriault for biathlon specific
                  training and Charlie Cobb for ski technique, strength and endurance training.
                </p>
              </div>
              <div className="pg-block">
                <h3>Academics</h3>
                <p>
                  Athletes are encouraged to take courses at the{' '}
                  <a href="https://www.umfk.edu/" target="_blank" rel="noopener noreferrer">
                    University of Maine at Fort Kent
                  </a>{' '}
                  to stay intellectually stimulated while training and fulfill some early collegiate
                  course requirements. The University offers scholarship programs to all athletes
                  training with the FKOC Post Graduate Program.
                </p>
              </div>
            </div>
            <div className="pg-column">
              <div className="pg-block">
                <h3>Facility</h3>
                <p>
                  The training will take advantage of the excellent facilities at the Fort Kent
                  Outdoor Center. This includes a 3km paved roller skiing loop, a 30-point shooting
                  range, and 25km of excellent Nordic trails that are FIS and IBU homologated.
                  Fort Kent has the longest snow-covered season in the Northeast, usually starting
                  in early November and finishing in late April.
                </p>
              </div>
              <div className="pg-block">
                <h3>Housing</h3>
                <p>
                  We offer two housing options for our athletes, our lodge and the Jalbert Biathlon
                  Residence. While the coaches do check in frequently, the athletes are living
                  independently and are expected to maintain their space appropriately.
                </p>
              </div>
            </div>
          </div>

          {/* Pricing */}
          <div className="pg-pricing">
            <h3>Pricing</h3>
            <ul className="pricing-list">
              {pgPricing.map((item, index) => (
                <li key={index} className="pricing-item">
                  <CheckIcon />
                  <span className="pricing-text">
                    <strong>{item.title}</strong>
                    <small>{item.detail}</small>
                  </span>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </section>

      {/* PG Program CTA Section */}
      <section className="pg-cta-section">
        <div className="pg-cta">
          <div className="container">
            <h2>Space is Limited!</h2>
            <p>
              The PG Program will be limited to the first 5 athletes registered due to housing
              restrictions, so don't delay! Follow the link to download and submit your
              application today.
            </p>
            <div className="pg-cta-buttons">
              <a
                href="https://drive.google.com/file/d/17QBqvZnmy7SJ0w_Bzpmnjaaoml3_xr-F/view?usp=drive_web"
                target="_blank"
                rel="noopener noreferrer"
                className="btn btn-accent"
              >
                Program Application
              </a>
              <a
                href="https://drive.google.com/file/d/11mxe4Lqy_ASNxjiu9R74zEMNmluFcoXz/view?usp=drive_web"
                target="_blank"
                rel="noopener noreferrer"
                className="btn btn-outline"
              >
                <VideoIcon />
                Additional Information
              </a>
            </div>
          </div>
        </div>
      </section>

      {/* Jalbert Biathlon Residence Section */}
      <section className="section section-dark" id="residence">
        <div className="container">
          <div className="section-header text-center">
            <h2 className="section-title text-inverse">Jalbert Biathlon Residence</h2>
            <p className="content-text text-light residence-intro">
              The Post Graduate program is supported by the generous help of Phyllis Jalbert,
              who has provided us with the "Jalbert Biathlon Residence", located within walking
              distance of the FKOC. There are 5 bedrooms, a spacious living room/kitchen, and
              a common area in the basement at the location at 42 2nd Ave, about a mile from FKOC.
              Available to full time athletes on a first come first serve basis.
            </p>
          </div>
          <div className="residence-gallery">
            {residencePhotos.map((photo, index) => (
              <img key={index} src={photo.src} alt={photo.alt} className="residence-photo" />
            ))}
          </div>
        </div>
      </section>

      {/* Jalbert Ski Program Section */}
      <section className="section" id="ski-program">
        <div className="container">
          <div className="two-col-grid">
            <div className="content-col">
              <h2 className="section-title">Jalbert Ski Program</h2>
              <div className="content-text">
                <p>
                  The Jalbert Youth Ski Program is a great opportunity for children grades K-6
                  to get outside and learn to cross-country ski! This exciting winter program
                  hosted at the Fort Kent Outdoor Center (FKOC) offers trail passes, ski rentals,
                  and instruction at no cost thanks to Phyllis Jalbert who has supported the
                  program for many years. Sessions are typically held on Saturday afternoons
                  twice a month (January-March). Dates and details are posted each year once
                  the trails at the FKOC are skiable.
                </p>
                <p>
                  Whether your child ends up coming to just one session, or catches Ski Fever
                  and doesn't miss a single one, each week's session will incorporate most of
                  the necessary skills, including balance, glide and uphill and downhill
                  techniques into the activities and games.
                </p>
                <p>
                  A dedicated team of FKOC volunteers help coordinate ski rentals and provide
                  instruction to the participants according to their ability level and preferred
                  technique. While most participants are equipped with classic skis (fish-scales
                  on the base), some participants take advantage of the opportunity to try skate
                  skiing (no fish scales). Classic technique is the best choice for beginning skiers.
                </p>
                <p>
                  Participants who have rented complimentary ski packages through the Jalbert
                  Program will be asked to return their skis/boots/poles at the last session.
                </p>
                <p>
                  We are always looking for volunteers (ages 15+) to help out inside and outside.
                  Our indoor tasks include helping with registration and running the rental shop.
                  Our outdoor volunteers would be helping with instruction out on the snow.
                  If you are interested in helping out, please send us a message.
                </p>
              </div>
            </div>
            <div className="image-col">
              <div className="staggered-images">
                <img
                  src={jalbertSnowplow}
                  alt="Kid skiing"
                  className="staggered-img-1"
                />
                <img
                  src={jalbertClass}
                  alt="Kids taking a ski lesson"
                  className="staggered-img-2"
                />
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Jalbert Biathlon Program Section */}
      <section className="section section-dark" id="biathlon-program">
        <div className="container">
          <div className="two-col-grid">
            <div className="content-col">
              <h2 className="section-title text-inverse">Jalbert Biathlon Program</h2>
              <div className="content-text text-light">
                <p>
                  For youth ages 10+ interested in competing in biathlon, the Jalbert Biathlon
                  Program offers instruction at the same time as the Youth Ski Program. The
                  biathlon portion of the program extends beyond the winter months, however,
                  with training and events held throughout the summer for a nominal fee.
                </p>
                <p>
                  Since it began in 2011, the Jalbert Youth Ski & Biathlon Programs have been
                  funded by the generosity and enthusiasm of Fort Kent native, Mrs. Phyllis
                  Jalbert. Phyllis is happy to see cross-country skiing and biathlon thriving
                  in our community. The FKOC is very grateful for her ongoing support.
                </p>
              </div>
            </div>
            <div className="image-col">
              <div className="staggered-images">
                <img
                  src={jalbertBiathlon}
                  alt="Biathlon racer"
                  className="staggered-img-1"
                />
                <img
                  src={eastRegionBiathlon}
                  alt="Biathlon range"
                  className="staggered-img-2"
                />
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}

export default CoachingPrograms
