import React, { useEffect } from "react";
import FullScreenSection from "./FullScreenSection";
import { Box, Center, Heading, OrderedList, ListItem } from "@chakra-ui/react"; // Import OrderedList and ListItem
import Card from "./Card";
import { motion, useAnimation } from "framer-motion";
import { useInView } from "react-intersection-observer";

const AnimatedBox = motion(Box);

const projects = [
  {
    title:
      "Market Intelligence Nexus: An Optimized Multi-Agent System for Elastic Pricing Strategy",
    description: [
      "Engineered a sophisticated Multi-Agent System that performs comprehensive stochastic analysis and market research.",
      "Correlated external events impacting product performance and recommends strategic pricing based on Price Elasticity theory.",
      "Implemented a custom deterministic message exchange protocol between agents, optimizing communication flow while reducing token consumption by 30%.",
    ],
    getImageSrc: () => require("../images/agents.jpeg"),
    url: "https://github.com/Raman369AI/pretiumnova",
  },
  {
    title:
      "QuizForge: A Custom RAG Engine for Educational Assessment Generation",
    description: [
      "Architected a ground-up Retrieval-Augmented Generation system that creates tailored multiple-choice questions for student assessment, bypassing conventional abstractions for maximum customization.",
      "Enhanced the system question generation capabilities by fine-tuning T5-Small with LoRA techniques on the SQuAD v2 dataset.",
      "Currently developing this into a comprehensive open-source library to democratize advanced educational assessment tools for educators worldwide.",
    ],
    getImageSrc: () => require("../images/wer.jpeg"),
    url: "https://github.com/Raman369AI/research",
  },
  {
    title: "Customer Behavior Analysis for Healthcare Engagement",
    description: [
      "Designed predictive models to analyze and influence customer behavior, aiming to increase primary care physician (PCP) visit rates, enhancing preventive healthcare engagement.",
      "Ranked 11th in the Case Competition by employing ensemble models and causal inference to deliver actionable recommendations and accurate predictions.",
      "Code and data can't be disclosed due to NDA.",
    ],
    getImageSrc: () => require("../images/photo5.jpg"),
  },
  {
    title:
      "End-to-End Predictive Modeling for Mushroom Toxicity Classification",
    description: [
      "Engineered a high-precision toxicity detection system for mushroom species classification leveraging LightGBM's gradient boosting framework.",
      "Achieved exceptional discrimination with a 0.98 AUC score that secured competitive ranking on Kaggle's leaderboard.",
      "Seamlessly transitioned from model development to production by leveraging FastAPI, containerizing the solution with Docker and deploying using Azure App service.",
    ],
    getImageSrc: () => require("../images/photo1.jpg"),
    url: "https://github.com/Raman369AI/GitHub/tree/master/poisnous_mushrooms",
  },

  {
    title: "Data4Good, AI-Powered Survivor Journey Mapping for TAPS",
    description: [
      "Developed an AI-powered system to classify survey responses into predefined epochs or stages of the survivor journey.",
      "Used natural language processing (NLP) techniques to analyze qualitative survey data and match responses with appropriate resources and support strategies.",
      "Enhanced efficiency by reducing manual effort and improving accuracy in connecting survivors with relevant care.",
    ],
    getImageSrc: () => require("../images/photo3.jpg"),
    url: "https://github.com/Raman369AI/GitHub/tree/master/data4good",
  },
  {
    title:
      "Santa2024, Untangling Words - Minimizing Perplexity in Scrambled Texts with AI",
    description: [
      "This project applies memetic algorithms—a combination of  Genetic Algorithm (GA) and Simulated Annealing (SA)—to reconstruct scrambled Christmas stories into coherent narratives.",
    ],
    getImageSrc: () => require("../images/photo4.jpg"),
    url: "https://github.com/Raman369AI/GitHub/tree/master/santa_2024",
  },
  {
    title:
      "Evaluating Open-Source LLMs for Summarizing Product Reviews: Insights and Perplexity Analysis",
    description: [
      "This project explored the capability of open-source large language models (LLMs) to summarize Amazon product reviews effectively.",
      "Focused on perplexity as a key evaluation metric.",
      "The study aimed to determine whether open-source LLMs can match or approach the performance of proprietary models in generating coherent, concise, and meaningful summaries from customer feedback.",
    ],
    getImageSrc: () => require("../images/photo2.jpg"),
    url: "https://github.com/Raman369AI/GitHub/tree/master/NLP",
  },
];

const ProjectsSection = () => {
  const controls = useAnimation();
  const { ref, inView } = useInView();

  useEffect(() => {
    if (inView) {
      controls.start("visible");
    }
    if (!inView) {
      controls.start("hidden");
    }
  }, [controls, inView]);
  const boxVariants = {
    hidden: { opacity: 0, y: 50 },
    visible: {
      opacity: 1,
      y: 0,
      transition: {
        duration: 0.5,
        when: "beforeChildren",
        staggerChildren: 0.2,
      },
    },
  };
  const cardVariants = {
    hidden: { opacity: 0, y: 50 },
    visible: { opacity: 1, y: 0 },
  };
  return (
    <FullScreenSection
      backgroundColor="#9896f1"
      isDarkBackground
      p={8}
      alignItems="center"
      spacing={12}
    >
      <AnimatedBox
        ref={ref}
        variants={boxVariants}
        initial="hidden"
        animate={controls}
      >
        <Center w="100%">
          <Heading as="h1" id="projects-section">
            Featured Projects
          </Heading>
        </Center>
        <Box
          display="grid"
          gridTemplateColumns="repeat(2,minmax(0,1fr))"
          gridGap={6}
        >
          {projects.map((project) => (
            <AnimatedBox variants={cardVariants} key={project.title}>
            <Card
              title={project.title}
              description={project.description} // Pass the array of strings
              url={project.url}
              imageSrc={project.getImageSrc()}
            />
          </AnimatedBox>
          ))}
        </Box>
      </AnimatedBox>
    </FullScreenSection>
  );
};

export default ProjectsSection;
