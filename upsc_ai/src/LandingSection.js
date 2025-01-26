import React from "react";
import { Avatar, Heading, VStack } from "@chakra-ui/react";
import FullScreenSection from "./FullScreenSection";
import { Link, LinkOverlay, LinkBox, Stack, Text, Button } from "@chakra-ui/react";

const greeting = "Important resources";
const bio1 = "Tech assisted learning";
const bio2 = "Site is Under Development";

const LandingSection = () => (
  <FullScreenSection
    justifyContent="center"
    alignItems="center"
    isDarkBackground
    backgroundColor="#01352c"
  >
    <VStack spacing={16} align = 'left'>
      <VStack spacing={16} alignItems="left">
        <VStack spacing={16} alignItems="left">
          <Heading as="h2" size="md" noOfLines={1} fontFamily="Times">
            {greeting}
          </Heading>

          {/* First Link */}
          <LinkBox>
            <Heading size="sm" noOfLines={1}>
              <LinkOverlay href="https://upsc.gov.in/sites/default/files/Notif-CSP-24-engl-140224.pdf">
                <Button
                  color="teal.500"
                  fontSize="xl"
                  _hover={{ color: "teal.300", textDecoration: "none" }}
                  _focus={{ outline: "none", textDecoration: "none" }}
                >
                  SYLLABUS
                </Button>
              </LinkOverlay>
            </Heading>
          </LinkBox>

          {/* Second Link */}
          <LinkBox>
            <Heading size="sm" noOfLines={1}>
              <LinkOverlay href="https://ncert.nic.in/textbook.php">
                <Button
                  color="teal.500"
                  fontSize="xl"
                  _hover={{ color: "teal.300", textDecoration: "none" }}
                  _focus={{ outline: "none", textDecoration: "none" }}
                >
                  NCERT
                </Button>
              </LinkOverlay>
            </Heading>
          </LinkBox>

          <LinkBox>
            <Heading size="sm" noOfLines={1}>
              <LinkOverlay href="https://www.thehindu.com/">
                <Button
                  color="teal.500"
                  fontSize="xl"
                  _hover={{ color: "teal.300", textDecoration: "none" }}
                  _focus={{ outline: "none", textDecoration: "none" }}
                >
                 THE HINDU NEWSPAPER
                </Button>
              </LinkOverlay>
            </Heading>
          </LinkBox>
          <LinkBox>
            <Heading size="sm" noOfLines={1}>
              <LinkOverlay href="https://www.indiabudget.gov.in/economicsurvey/">
                <Button
                  color="teal.500"
                  fontSize="xl"
                  _hover={{ color: "teal.300", textDecoration: "none" }}
                  _focus={{ outline: "none", textDecoration: "none" }}
                >
ECONOMIC SURVEY
                </Button>
              </LinkOverlay>
            </Heading>
          </LinkBox>


        </VStack>
      </VStack>


      {/* Bio Section */}
      <VStack spacing={6}>
        <Heading as="h2" size="md" noOfLines={1} fontFamily="Times">
          {bio1}
        </Heading>
        <Heading as="h2" size="md" noOfLines={2} fontFamily="Times">
          {bio2}
        </Heading>
      </VStack>
    </VStack>
  </FullScreenSection>
);

export default LandingSection;
