import { createContext, useContext, useState } from 'react'

const WebcamContext = createContext()

export function WebcamProvider({ children }) {
  const [webcamOpen, setWebcamOpen] = useState(false)

  return (
    <WebcamContext.Provider value={{ webcamOpen, openWebcam: () => setWebcamOpen(true), closeWebcam: () => setWebcamOpen(false) }}>
      {children}
    </WebcamContext.Provider>
  )
}

export function useWebcam() {
  return useContext(WebcamContext)
}
