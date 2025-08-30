import React, { useEffect, useRef } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faEnvelope } from "@fortawesome/free-solid-svg-icons";
import {
  faGithub,
  faLinkedin,
  faMedium,
  faStackOverflow, // You had this imported but not used, so I'm keeping it in case you plan to use it later
} from "@fortawesome/free-brands-svg-icons";
import { Box, HStack } from "@chakra-ui/react"; // Removed 'Card' as it's not used in the provided snippet

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
  const headerRef = useRef(null);

  useEffect(() => {
    let prevScrollPos = window.scrollY;

    const handleScroll = () => {
      const currentScrollPos = window.scrollY;
      const headerElement = headerRef.current;
      if (!headerElement) {
        return;
      }
      if (prevScrollPos > currentScrollPos) {
        headerElement.style.transform = "translateY(0)";
      } else {
        headerElement.style.transform = "translateY(-200px)";
      }
      prevScrollPos = currentScrollPos;
    };
    window.addEventListener("scroll", handleScroll);

    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

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

  // Replace this with the actual URL to your resume PDF
  const resumePdfUrl = "/resume_short.pdf"; // Example: "https://yourwebsite.com/resume.pdf" or "https://docs.google.com/document/d/123abc/export?format=pdf"

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
      backgroundColor="white"
      ref={headerRef}
    >
      <Box color="black" maxWidth="1280px" margin="0 auto">
        <HStack
          px={16}
          py={4}
          justifyContent="space-between"
          alignItems="center"
        >
          <nav>
            <HStack spacing={8}>
              {socials.map(({ icon, url }) => (
                <a
                  key={url}
                  href={url}
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  <FontAwesomeIcon icon={icon} size="2x" key={url} />
                </a>
              ))}
            </HStack>
          </nav>
          <nav>
            <HStack spacing={8}>
              <a
                href="#work-experience-section"
                onClick={handleClick("work-experience")}
              >
                Work Experience
              </a>
              <a href="#projects" onClick={handleClick("projects")}>
                Projects
              </a>
              <a href={resumePdfUrl} target="_blank" rel="noopener noreferrer">
                Resume
              </a>
            </HStack>
          </nav>
        </HStack>
      </Box>
    </Box>
  );
};

export default Header;