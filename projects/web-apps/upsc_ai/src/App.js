import './App.css';
import Nav from './Nav.js'
import { Routes, Route } from 'react-router-dom';
import Quiz from './Quiz.js';
import Header from './Header.js';
import { useLocation } from 'react-router-dom';
import image from './image.png';
import { ChakraProvider, HStack, defaultSystem, Image, Heading, Container,DecorativeBox } from '@chakra-ui/react';
import Footer from './Footer.js';
import FullScreenSection from './FullScreenSection'
import LandingSection from './LandingSection'
function App() {
  const location = useLocation();
  const isHomePage = location.pathname === "/";
  return (
    <ChakraProvider value={defaultSystem}>
      <Container centerContent fluid mb="24">
        <Header />
        {isHomePage && <HomeContent />}
        <Container centerContent fluid mt="8">
          <Nav />
        </Container>
        <Routes>
          <Route path="/" element={<></>} />
          <Route path="/Modern-History" element={<Quiz />} />
        </Routes>
<Container maxW = 'span'mt = '100px'> 
  <LandingSection />
  </Container>
       
<FullScreenSection />

      </Container>
      <Footer />

    </ChakraProvider> );   
}

function HomeContent() {
  return (

      <Container centerContent = 'true' fluid = 'true'>
        <HStack>
<Image src={image} alt="UAI" boxSize = "150px" borderRadius = 'full' />
<Heading 
  id="description" 
  color="#3152c" 
  textAlign="center" 
  width="50%" // Adjust width to control wrapping
  fontSize="xl" // Adjust font size for better fit
  lineHeight="2" // Adjust line height for readability
>
  Empowering UPSC aspirants
</Heading>
    </HStack>

    </Container>
  );
}
document.title = "UAI";

export default App;
