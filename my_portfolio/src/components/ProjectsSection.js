import React from "react";
import FullScreenSection from "./FullScreenSection";
import { Box, Heading } from "@chakra-ui/react";
import Card from "./Card";

const projects = [
  {
    title: "End-to-End Predictive Modeling for Mushroom Toxicity Classification",
    description:
      "Developed a comprehensive, end-to-end solution to identify toxic mushroom species.",
    getImageSrc: () => require("../images/photo1.jpg"),
  },
  {
    title: "Sentiment Analysis and Summarization of Amazon Reviews ",
    description:
      "summarize customer insights from product reviews, reproduce the Amazon summary using other NLP techniques and compare the same.",
    getImageSrc: () => require("../images/photo2.jpg"),
  },
  {
    title: "Customer Behavior Analysis for Healthcare Engagement",
    description:
      "Designed predictive models to analyze and influence customer behavior, aiming to increase primary care physician (PCP) visit rates, enhancing preventive healthcare engagement.",
    getImageSrc: () => require("../images/photo3.jpg"),
  },
  {
    title: "Event planner",
    description:
      "A mobile application for leisure seekers to discover unique events and activities in their city with a few taps",
    getImageSrc: () => require("../images/photo4.jpg"),
  },
];

const ProjectsSection = () => {
  return (
    <FullScreenSection
      backgroundColor="#14532d"
      isDarkBackground
      p={8}
      alignItems="flex-start"
      spacing={8}
    >
      <Heading as="h1" id="projects-section">
        Featured Projects
      </Heading>
      <Box
        display="grid"
        gridTemplateColumns="repeat(2,minmax(0,1fr))"
        gridGap={8}
      >
        {projects.map((project) => (
          <Card
            key={project.title}
            title={project.title}
            description={project.description}
            imageSrc={project.getImageSrc()}
          />
        ))}
      </Box>
    </FullScreenSection>
  );
};

export default ProjectsSection;
