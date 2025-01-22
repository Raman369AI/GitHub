import './App.css';
import Nav from './Nav.js'
import { Routes, Route } from 'react-router-dom';
import Quiz from './Quiz.js';
import Header from './Header.js';
import { useLocation } from 'react-router-dom';
import image from './image.png';
import { ChakraProvider, HStack, defaultSystem, Image, Heading, Container } from '@chakra-ui/react';


function App() {
  const location = useLocation();
  const isHomePage = location.pathname === "/";

  return (
    isHomePage?<ChakraProvider value={defaultSystem}><Container centerContent = 'true' fluid = 'true' mb = "24">
      <Header />
      <HomeContent />
      <Routes>
      <Route path="/" element={<></>} />
      <Route path="/Modern-History" element={<Quiz />} />
     </Routes>
     <Container centerContent = 'true' fluid = 'true' mt="24"> <Nav /></Container>
        </Container>
        </ChakraProvider>:<ChakraProvider value={defaultSystem}>
   <Container centerContent = 'true' fluid = 'true'>
      <Header />
      <HomeContent />
      <Container centerContent = 'true' fluid = 'true'> <Nav /></Container>
      <Routes>
      <Route path="/" element={<></>} />
      <Route path="/Modern-History" element={<Quiz />} />
     </Routes>
     </Container>
   </ChakraProvider>  );   
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

export default App;
