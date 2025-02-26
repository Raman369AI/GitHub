import React from "react"; 
import { Avatar, Heading, VStack, Box } from "@chakra-ui/react"; 
import FullScreenSection from "./FullScreenSection"; 
 
const greeting = "Hello, I am Raman!"; 
const bio1 = "an experienced Data Scientist"; 
const bio2 = "Code lover, problem solver and a Data Scientist who thrives on tough challenges and never stops learning new skills"; 
const rt = require("../images/IMGL9741.jpg");
const LandingSection = () => ( 
 <FullScreenSection 
   justifyContent="center" 
   alignItems="center" 
   isDarkBackground 
   backgroundColor="#9896f1" 
 > 
   <VStack spacing={4}> 
     <VStack spacing={2} alignItems="center"> 

     <Box
          borderRadius="full"
          overflow="hidden"
          //boxSize={{ base: "150px", md: "200px", lg: "200px" }}
          boxSize="400px"
        >       <Avatar 
         src={rt}
         size="full" 
         name="Raman" 
         overflow="hidden"
       /> 
       </Box>
       <Heading as="h1" size="xl" noOfLines={1} color = 'black'> 
         {greeting} 
       </Heading> 
     </VStack> 
     <VStack spacing={2}> 
       
       <Heading as="h1" size="md" noOfLines={1}> 
         {bio2} 
       </Heading> 
     </VStack> 
   </VStack> 
 </FullScreenSection> 
); 
 
export default LandingSection;