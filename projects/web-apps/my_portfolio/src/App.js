import React, { useEffect } from 'react'; // Import useEffect
import { ChakraProvider } from "@chakra-ui/react";
import Header from "./components/Header";
import LandingSection from "./components/LandingSection";
import ProjectsSection from "./components/ProjectsSection";
import ContactMeSection from "./components/ContactMeSection";
import TechnologiesSection from "./components/TechnologiesSection";
import Footer from "./components/Footer";
import { AlertProvider } from "./context/alertContext";
import Alert from "./components/Alert";
import Experience from "./components/Experience";
import ReactGA from 'react-ga4';

ReactGA.initialize('G-MVHQ19R0YZ');

function App() {
  useEffect(() => {
    // Send a pageview to Google Analytics when the App component mounts
    // This captures the initial visit.
    ReactGA.send({ hitType: "pageview", page: window.location.pathname + window.location.search, title: "Home Page" });
  }, []); // The empty dependency array ensures this runs only once on mount

  return (
    <ChakraProvider>
      <AlertProvider>
        <main>
          <Header />
          <LandingSection />
          <Experience />
          <ProjectsSection />
            <TechnologiesSection />
          <Footer />
          <Alert />
        </main>
      </AlertProvider>
    </ChakraProvider>
  );
}

export default App;
