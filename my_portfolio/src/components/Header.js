import React, { useEffect, useRef } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faEnvelope } from "@fortawesome/free-solid-svg-icons";
import {
  faGithub,
  faLinkedin,
  faMedium,
  faStackOverflow,
} from "@fortawesome/free-brands-svg-icons";
import { Box, HStack, Card } from "@chakra-ui/react";
import ProjectsSection from "./ProjectsSection";
const socials = [
  {
    icon: faEnvelope,
    url: "mailto: bvenkat@okstate.edu",
  },
  {
    icon: faGithub,
    url: "https://github.com/Raman369AI/GitHub",
  },
  {
    icon: faLinkedin,
    url: "https://www.linkedin.com/in/raman-raj-botta/",
  },
  {
    icon: faMedium,
    url: "https://medium.com/@botta.raman",
  },
 
];

const Header = () => {
  const handleClick = (anchor) => () => {
    const id = `${anchor}-section`;
    const element = document.getElementById(id);
    if (element) {
      element.scrollIntoView({
        behavior: "smooth",
        block: "start",
      });
    }
  };

  return (
    <Box
      position="fixed"
      top={0}
      left={0}
      right={0}
      translateY={0}
      transitionProperty="transform"
      transitionDuration=".3s"
      transitionTimingFunction="ease-in-out"
      backgroundColor="#18181b"
    >
      <Box color="white" maxWidth="1280px" margin="0 auto">
        <HStack
          px={16}
          py={4}
          justifyContent="space-between"
          alignItems="center"
        >
          <nav>
            <HStack spacing={4}>
    {socials.map((social, index) => (
      <a key={index} href={social.url} target="_blank" rel="noopener noreferrer">
        <FontAwesomeIcon icon={social.icon} size="1x" />
      </a>
    ))}
  </HStack>
          </nav>
          <nav>
            <HStack spacing={4}>
              <a href="/#projects" onClick={handleClick('projects')}>Projects</a>
        <a href="/#contact-me" onClick={handleClick('contactme')}>Contact Me</a>
            </HStack>
          </nav>
        </HStack>
      </Box>
    </Box>
  );
};
export default Header;
