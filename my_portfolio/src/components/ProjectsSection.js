import React from "react";
import FullScreenSection from "./FullScreenSection";
import { Box, Heading } from "@chakra-ui/react";
import Card from "./Card";

const projects = [
  {
    title: "End-to-End Predictive Modeling for Mushroom Toxicity Classification",
    description:
      "Developed a comprehensive, end-to-end solution to identify toxic mushroom species using Lightgbm.",
    getImageSrc: () => require("../images/photo1.jpg"),
    url: "https://github.com/Raman369AI/GitHub/tree/master/poisnous_mushrooms",
  },
  {
    title: "Evaluating Open-Source LLMs for Summarizing Product Reviews: Insights and Perplexity Analysis",
    description:
      "This project explored the capability of open-source large language models (LLMs) to summarize Amazon product reviews effectively, focusing on perplexity as a key evaluation metric. The study aimed to determine whether open-source LLMs can match or approach the performance of proprietary models in generating coherent, concise, and meaningful summaries from customer feedback.",
    getImageSrc: () => require("../images/photo2.jpg"),
    url:"https://github.com/Raman369AI/GitHub/tree/master/NLP",
  },
  {
    title: "Data4Good, AI-Powered Survivor Journey Mapping for TAPS",
    description:
      "Developed an AI-powered system to classify survey responses into predefined epochs or stages of the survivor journey. Used natural language processing (NLP) techniques to analyze qualitative survey data and match responses with appropriate resources and support strategies. Enhanced efficiency by reducing manual effort and improving accuracy in connecting survivors with relevant care.",
    getImageSrc: () => require("../images/photo3.jpg"),
    url:"https://github.com/Raman369AI/GitHub/tree/master/data4good"
  },
  {
    title: "Santa2024, Untangling Words - Minimizing Perplexity in Scrambled Texts with AI",
    description:
      "This project applies memetic algorithms—a combination of  Genetic Algorithm (GA) and Simulated Annealing (SA)—to reconstruct scrambled Christmas stories into coherent narratives",
    getImageSrc: () => require("../images/photo4.jpg"),
    url:"https://github.com/Raman369AI/GitHub/tree/master/santa_2024"
  },
  {
    title: "Customer Behavior Analysis for Healthcare Engagement",
    description:
      "Designed predictive models to analyze and influence customer behavior, aiming to increase primary care physician (PCP) visit rates, enhancing preventive healthcare engagement.",
    getImageSrc: () => require("../images/photo5.jpg"),
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
            url= {project.url}
            imageSrc={project.getImageSrc()} 
          /> 
        ))} 
      </Box> 
    </FullScreenSection> 
  ); 
 }; 
  
 export default ProjectsSection;
