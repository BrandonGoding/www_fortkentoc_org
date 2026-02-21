import { Routes, Route } from 'react-router-dom'
import './App.css'

import Layout from './components/Layout'
import Home from './pages/Home'
import AboutUs from './pages/AboutUs'
import Facilities from './pages/Facilities'
import Trails from './pages/Trails'
import Endowment from './pages/Endowment'
import PoliciesAndSafety from './pages/PoliciesAndSafety'
import CoachingPrograms from './pages/CoachingPrograms'
import DayPasses from './pages/DayPasses'
import Rentals from './pages/Rentals'
import Memberships from './pages/Memberships'
import EventCalendar from './pages/EventCalendar'
import UpcomingEvents from './pages/UpcomingEvents'
import WomensWellnessDay from './pages/WomensWellnessDay'
import EasternRegionalBiathlon from './pages/EasternRegionalBiathlon'
import Location from './pages/Location'

function App() {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Home />} />
        <Route path="about-us" element={<AboutUs />} />
        <Route path="facilities" element={<Facilities />} />
        <Route path="trails" element={<Trails />} />
        <Route path="endowment" element={<Endowment />} />
        <Route path="policies-and-safety" element={<PoliciesAndSafety />} />
        <Route path="coaching-programs" element={<CoachingPrograms />} />
        <Route path="day-passes" element={<DayPasses />} />
        <Route path="rentals" element={<Rentals />} />
        <Route path="memberships" element={<Memberships />} />
        <Route path="event-calendar" element={<EventCalendar />} />
        <Route path="upcoming-events" element={<UpcomingEvents />} />
        <Route path="womens-wellness-day" element={<WomensWellnessDay />} />
        <Route path="eastern-regional-biathlon" element={<EasternRegionalBiathlon />} />
        <Route path="location" element={<Location />} />
      </Route>
    </Routes>
  )
}

export default App
