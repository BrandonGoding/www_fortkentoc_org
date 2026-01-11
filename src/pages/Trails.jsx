import luciSkiing from '../assets/images/home/luci-skiing.png'

// Map thumbnails
import snowshoeMapThumb from '../assets/images/trails/maps-thumbnails/snowshoe-map.jpg'
import mtbikeMapThumb from '../assets/images/trails/maps-thumbnails/mtbike-trails.jpg'
import discGolfMapThumb from '../assets/images/trails/maps-thumbnails/disc-golf.jpg'
import nordicMapThumb from '../assets/images/trails/maps-thumbnails/nordic-ski.jpg'
import biathlon25kmThumb from '../assets/images/trails/maps/map-13.jpg'
import biathlon4kmThumb from '../assets/images/trails/maps-thumbnails/biathlon-4km.jpg'
import biathlon2kmThumb from '../assets/images/trails/maps-thumbnails/biathlon-2km.jpg'
import biathlon3kmThumb from '../assets/images/trails/maps-thumbnails/biathlon-3km.jpg'
import biathlon33kmThumb from '../assets/images/trails/maps-thumbnails/biathlon-3-3km.jpg'
import biathlon15kmThumb from '../assets/images/trails/maps-thumbnails/biathlon-1-5km.jpg'
import biathlonCompositeThumb from '../assets/images/trails/maps-thumbnails/biathlon-composite.jpg'
import biathlon1kmThumb from '../assets/images/trails/maps-thumbnails/biathlon-1km.jpg'

// Map full size
import snowshoeMapFull from '../assets/images/trails/maps-original/snowshoe-map.jpeg'
import mtbikeMapFull from '../assets/images/trails/maps-original/mtbike-trails.jpg'
import discGolfMapFull from '../assets/images/trails/maps-original/disc-golf.jpg'
import nordicMapFull from '../assets/images/trails/maps-original/nordic-ski.jpg'
import biathlon25kmFull from '../assets/images/trails/maps-original/biathlon-2-5km.jpg'
import biathlon4kmFull from '../assets/images/trails/maps-original/biathlon-4km.jpg'
import biathlon2kmFull from '../assets/images/trails/maps-original/biathlon-2km.jpg'
import biathlon3kmFull from '../assets/images/trails/maps-original/biathlon-3km.jpg'
import biathlon33kmFull from '../assets/images/trails/maps-original/biathlon-3-3km.jpg'
import biathlon15kmFull from '../assets/images/trails/maps-original/biathlon-1-5km.jpg'
import biathlonCompositeFull from '../assets/images/trails/maps-original/biathlon-composite.jpg'
import biathlon1kmFull from '../assets/images/trails/maps-original/biathlon-1km.jpg'

const Icons = {
  Apple: () => (
    <svg className="app-icon" aria-hidden="true" viewBox="0 0 384 512">
      <path fill="currentColor" d="M318.7 268.7c-.2-36.7 16.4-64.4 50-84.8-18.8-26.9-47.2-41.7-84.7-44.6-35.5-2.8-74.3 20.7-88.5 20.7-15 0-49.4-19.7-76.4-19.7C63.3 141.2 4 184.8 4 273.5q0 39.3 14.4 81.2c12.8 36.7 59 126.7 107.2 125.2 25.2-.6 43-17.9 75.8-17.9 31.8 0 48.3 17.9 76.4 17.9 48.6-.7 90.4-82.5 102.6-119.3-65.2-30.7-61.7-90-61.7-91.9zm-56.6-164.2c27.3-32.4 24.8-61.9 24-72.5-24.1 1.4-52 16.4-67.9 34.9-17.5 19.8-27.8 44.3-25.6 71.9 26.1 2 49.9-11.4 69.5-34.3z" />
    </svg>
  ),
  GooglePlay: () => (
    <svg className="app-icon" aria-hidden="true" viewBox="0 0 512 512">
      <path fill="currentColor" d="M325.3 234.3L104.6 13l280.8 161.2-60.1 60.1zM47 0C34 6.8 25.3 19.2 25.3 35.3v441.3c0 16.1 8.7 28.5 21.7 35.3l256.6-256L47 0zm425.2 225.6l-58.9-34.1-65.7 64.5 65.7 64.5 60.1-34.1c18-14.3 18-46.5-1.2-60.8zM104.6 499l280.8-161.2-60.1-60.1L104.6 499z" />
    </svg>
  ),
}

const generalMaps = [
  {
    title: 'Snowshoe Trails',
    thumbnail: snowshoeMapThumb,
    fullSize: snowshoeMapFull,
    alt: '2025 Snowshoe Map'
  },
  {
    title: 'Mountain Bike Trails',
    thumbnail: mtbikeMapThumb,
    fullSize: mtbikeMapFull,
    alt: 'Mountain Bike Trails Map'
  },
  {
    title: 'Disc Golf',
    thumbnail: discGolfMapThumb,
    fullSize: discGolfMapFull,
    alt: '2024 FKOC Disc Golf Map'
  }
]

const nordicMaps = [
  {
    title: 'FKOC Nordic Ski Map',
    thumbnail: nordicMapThumb,
    fullSize: nordicMapFull,
    alt: '2024 FKOC Trail Map'
  }
]

const biathlonMaps = [
  {
    title: '2.5 Km Biathlon Course',
    thumbnail: biathlon25kmThumb,
    fullSize: biathlon25kmFull,
    alt: '2.5 Km Biathlon Course'
  },
  {
    title: '4.0 Km Biathlon Course',
    thumbnail: biathlon4kmThumb,
    fullSize: biathlon4kmFull,
    alt: '4.0 Km Biathlon Course'
  },
  {
    title: '2.0 Biathlon Course',
    thumbnail: biathlon2kmThumb,
    fullSize: biathlon2kmFull,
    alt: '2.0 Biathlon Course'
  },
  {
    title: '3.0 Km Biathlon Course',
    thumbnail: biathlon3kmThumb,
    fullSize: biathlon3kmFull,
    alt: '3.0 Km Biathlon Course'
  },
  {
    title: '3.3 Biathlon Course',
    thumbnail: biathlon33kmThumb,
    fullSize: biathlon33kmFull,
    alt: '3.3 Biathlon Course'
  },
  {
    title: '1.5 Km Biathlon Course',
    thumbnail: biathlon15kmThumb,
    fullSize: biathlon15kmFull,
    alt: '1.5 Km Biathlon Course'
  },
  {
    title: 'Composite Biathlon Course',
    thumbnail: biathlonCompositeThumb,
    fullSize: biathlonCompositeFull,
    alt: 'Composite Biathlon Course'
  },
  {
    title: '1.0Km Biathlon Course',
    thumbnail: biathlon1kmThumb,
    fullSize: biathlon1kmFull,
    alt: '1.0Km Biathlon Course'
  }
]

function MapCard({ title, thumbnail, fullSize, alt }) {
  return (
    <a
      href={fullSize}
      target="_blank"
      rel="noopener noreferrer"
      className="map-card"
    >
      <img src={thumbnail} alt={alt} />
      <h3>{title}</h3>
    </a>
  )
}

function Trails() {
  return (
    <div className="trails-page">
      {/* Hero Section */}
      <section className="trails-hero">
        <div className="hero-overlay">
          <div className="container">
            <div className="trails-hero-content">
              <h1>Trails at Fort Kent Outdoor Center</h1>
              <p>
                Welcome to Fort Kent's Outdoor Center, where adventure awaits on our Nordic ski,
                snowshoe, mountain biking, and hiking trails. Explore the beauty of each season,
                from the thrill of winter sports to the tranquility of forested paths. Embrace the
                outdoors and discover the extraordinary landscapes that make our trails unforgettable.
              </p>
              <div className="hero-buttons">
                <a href="#interactive" className="btn btn-primary">Interactive Nordic Map</a>
                <a href="#downloadable" className="btn btn-primary">Downloadable Trail Maps</a>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Intro Section */}
      <section className="section">
        <div className="container">
          <div className="trails-intro">
            <h2 className="section-title">
              Embark on a journey through Fort Kent's premier Outdoor Center, where every trail
              unveils a unique adventure
            </h2>
            <p className="content-text">
              Welcome to the breathtaking outdoor trails of Fort Kent's premier Outdoor Center!
              Nestled in the heart of nature's splendor, our diverse trail system offers an
              adventure for every season and enthusiast. Whether you're an avid Nordic skier
              seeking the thrill of gliding through pristine snow, a snowshoer craving the
              tranquility of winter landscapes, a mountain biker ready to conquer challenging
              terrain, or a hiker yearning to explore the wonders of the great outdoors, our
              trails are your gateway to unforgettable experiences. With meticulously maintained
              paths winding through forests and meadows, each trail promises a unique journey that
              immerses you in the natural beauty of Fort Kent. Discover the joy of outdoor
              exploration at our Outdoor Center – where every step, pedal, or glide is a
              celebration of the extraordinary landscapes that define our region.
            </p>
          </div>
        </div>
      </section>

      {/* Nordic Pulse App Section */}
      <section className="section section-dark">
        <div className="container">
          <div className="two-col-grid">
            <div className="content-col">
              <h2 className="section-title text-inverse">
                Get The Latest Trail Conditions On Your Mobile Device
              </h2>
              <p className="content-text text-light">
                Search your favorite app store or use the links below to download the Nordic Pulse App
              </p>
              <div className="app-buttons">
                <a
                  href="https://apps.apple.com/us/app/nordic-pulse/id1625390785"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="app-store-btn"
                >
                  <Icons.Apple />
                  <span>App Store</span>
                </a>
                <a
                  href="https://play.google.com/store/apps/details?id=com.nordicpulse.skier"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="app-store-btn"
                >
                  <Icons.GooglePlay />
                  <span>Google Play</span>
                </a>
              </div>
            </div>
            <div className="image-col app-image-col">
              <img
                src={luciSkiing}
                alt="Dog skiing and looking at phone"
                className="app-promo-image"
              />
            </div>
          </div>
        </div>
      </section>

      {/* Trail Conditions Section */}
      <section className="section" id="conditions">
        <div className="container">
          <h2 className="section-title text-center">Trail Conditions</h2>
          <div className="iframe-container">
            <iframe
              src="https://nordic-pulse.com/ski-areas/US/ME/Fort-Kent-Outdoor-Center/trails?embed=true&header=false&footer=false&tab=abc"
              title="Trail Conditions"
              allowFullScreen
            />
          </div>
        </div>
      </section>

      {/* Interactive Nordic Map Section */}
      <section className="section section-dark" id="interactive">
        <div className="container">
          <h2 className="section-title text-inverse text-center">Interactive Nordic Map</h2>
          <div className="iframe-container">
            <iframe
              src="https://nordic-pulse.com/ski-areas/US/ME/Fort-Kent-Outdoor-Center/map?embed=true&header=false&footer=false"
              title="Interactive Nordic Map"
              allowFullScreen
            />
          </div>
        </div>
      </section>

      {/* General Maps Section */}
      <section className="section" id="downloadable">
        <div className="container">
          <h2 className="section-title text-center">General Maps</h2>
          <div className="maps-grid maps-grid-3">
            {generalMaps.map((map, index) => (
              <MapCard key={index} {...map} />
            ))}
          </div>
        </div>
      </section>

      {/* Nordic Trails Section */}
      <section className="section section-alt">
        <div className="container">
          <h2 className="section-title text-center">Nordic Trails</h2>
          <div className="maps-grid maps-grid-single">
            {nordicMaps.map((map, index) => (
              <MapCard key={index} {...map} />
            ))}
          </div>
        </div>
      </section>

      {/* Biathlon Courses Section */}
      <section className="section">
        <div className="container">
          <h2 className="section-title text-center">Biathlon Courses</h2>
          <div className="maps-grid maps-grid-4">
            {biathlonMaps.map((map, index) => (
              <MapCard key={index} {...map} />
            ))}
          </div>
        </div>
      </section>
    </div>
  )
}

export default Trails
