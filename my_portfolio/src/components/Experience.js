import React from "react";
import {
  Box,
  Heading,
  VStack,
  Text,
  UnorderedList,
  ListItem,
  Divider,
} from "@chakra-ui/react";
import FullScreenSection from "./FullScreenSection";
import { motion, useAnimation } from "framer-motion";
import { useInView } from "react-intersection-observer";
import { useEffect } from "react";

const AnimatedBox = motion(Box);

const Experience = () => {
  const workExperienceData = [
    {
      id: "exp-1",
      company: "Oklahoma State University",
      title: "Graduate Teaching Assistant",
      dates: "2024 - Present",
      description: [
        "Engineered Python ETL pipeline leveraging Wayback Machine API and Beautiful Soup to analyse 2,200+ archived business websites to detect historical family-owned business and report their current status",
        "Built Tableau dashboards optimizing $500K+ annual funding allocation for Wings of Hope NGO for tracking 7+ KPI’s and the statistics associated with the clients",
      ],
    },
    {
      id: "exp-2",
      company: "GVMC, India",
      title: "Revenue Analyst",
      dates: "2019 - 2023",
      description: [
        "Developed a risk model prioritizing 18,000+ taxpayer accounts, communicated the insights to the executive team enabling 91% recovery rate through targeted interventions",
        "Pinpointed 6 blocks in 4 zones through revenue mapping with planning department data, driving 11% YoY growth via revised collection strategies and tracked 40 KPI’s across different revenue streams",
      ],
    },
    {
      id: "exp-3",
      company: "Chegg",
      title: "Sr Subject Matter Expert",
      dates: "2015 - 2019",
      description: [
        "Authored 300+ domain-expert solutions (statistics/Information Theory/MATLAB) incorporated into LLM training datasets, for an in-house LLM",
        "Content creation for Statistics, Information Theory and MATLAB",
      ],
    },
    // Add more experiences here
  ];

  const boxVariants = {
    hiddenLeft: { x: "-100%", opacity: 0 },
    hiddenRight: { x: "100%", opacity: 0 },
    visible: { x: "0%", opacity: 1, transition: { duration: 0.5 } },
  };

  return (
    <FullScreenSection
      backgroundColor="#d59bf6" // Dark background theme
      p={8}
      alignItems="center" // Center the items
      id="work-experience-section"
    >
      <VStack spacing={8} align="center" maxW="1200px">
        <Heading as="h1" size="2xl" color="black" mb={8}>
          Work Experience
        </Heading>
        <Divider borderColor="#d59bf6" />

        {workExperienceData.map((experience, index) => (
          <ExperienceItem
            key={experience.id}
            experience={experience}
            isLeft={index % 2 === 0} // Alternate sides
            variants={boxVariants} // pass the variants
          />
        ))}
      </VStack>
    </FullScreenSection>
  );
};
const ExperienceItem = ({ experience, isLeft, variants }) => {
  const controls = useAnimation();
  const { ref, inView } = useInView();

  useEffect(() => {
    if (inView) {
      controls.start("visible");
    }
    if (!inView){
        if (isLeft){
          controls.start("hiddenLeft");
        }else{
          controls.start("hiddenRight");
        }
    }
  }, [controls, inView, isLeft]);

  return (
    <AnimatedBox
      ref={ref}
      variants={isLeft ? variants : { ...variants, hiddenLeft: variants.hiddenRight, hiddenRight: variants.hiddenLeft }} // Alternate the animation
      initial={isLeft ? "hiddenLeft" : "hiddenRight"}
      animate={controls}
      p={6}
      borderWidth="1px"
      borderRadius="lg"
      bg="#9896f1" // Dark card background
      color="black"
      w="100%"
    >
      <Heading as="h2" size="lg">
        {experience.title}
      </Heading>
      <Text fontWeight="bold">{experience.company}</Text>
      <Text fontStyle="italic" mb={4}>
        {experience.dates}
      </Text>
      <UnorderedList pl={5}>
        {experience.description.map((item, idx) => (
          <ListItem key={idx}>{item}</ListItem>
        ))}
      </UnorderedList>
    </AnimatedBox>
  );
};

export default Experience;
