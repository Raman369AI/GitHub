import React from "react";
import { Box, Heading, VStack, Text, SimpleGrid, HStack } from "@chakra-ui/react";
import { FaPython, FaJsSquare, FaRProject, FaDatabase, FaDocker, FaFileExcel,FaRegFileExcel,FaMicrosoft } from "react-icons/fa";
import { SiKeras, SiPytorch, SiFastapi, SiHuggingface, SiApachespark, SiLinux,SiLangchain,SiOllama,SiReact,SiTableau,SiMongodb,SiLooker,SiDatabricks } from "react-icons/si";
import { TbSql } from "react-icons/tb";
import { VscAzure } from "react-icons/vsc";
import { AiOutlineOpenAI } from "react-icons/ai";
import { SiGooglecloud, SiMlflow } from "react-icons/si";
const technologies = [
  {
    category: "Programming Languages",
    items: [
      { name: "Python", icon: <FaPython /> },
      { name: "R", icon: <FaRProject /> },
      { name: "JavaScript", icon: <FaJsSquare /> },
    ],
  },
  {
    category: "Machine Learning Frameworks & Libraries",
    items: [
      { name: "Keras", icon: <SiKeras /> },
      { name: "PyTorch", icon: <SiPytorch /> },
      { name: "FastAPI", icon: <SiFastapi /> },
      { name: "Hugging Face", icon: <SiHuggingface /> },
      { name: "Apache Spark", icon: <SiApachespark /> },
    ],
  },
  {
    category: "Data Analysis & Visualization Tools",
    items: [
      { name: "SQL", icon: <FaDatabase /> },
      { name: "Excel", icon: <FaFileExcel /> },
      { name: "SAS", icon: <FaDatabase /> },
      { name: "Tableau", icon: <SiTableau /> },
      { name: "Power BI", icon: <FaRegFileExcel /> },
      { name: "SQL Server Management Studio (SSMS)", icon: <TbSql /> },
      { name: "MongoDB", icon: <SiMongodb /> },
      { name: "Looker Studio", icon: <SiLooker /> },
    ],
  },
  {
    category: "Cloud & DevOps Platforms",
    items: [
      { name: "Azure", icon: <VscAzure /> },
      { name: "Databricks", icon: <SiDatabricks /> },
      { name: "Google Cloud Platform (GCP)", icon: <SiGooglecloud /> },
      { name: "Docker", icon: <FaDocker /> },
      { name: "ML flow", icon: <SiMlflow /> },
    ],
  },
  {
    category: "Agentic AI & RAG",
    items: [
      { name: "AutoGen 0.4", icon: <FaMicrosoft /> },
      { name: "SmolAgents", icon: <SiHuggingface /> },
      { name: "Langgraph & LangChain", icon: <SiLangchain /> },
      { name: "LlamaIndex", icon: <SiOllama /> },
      { name: "DSPy", icon: <SiOllama /> },
      { name: "Agentic Development Kit , Google", icon: <AiOutlineOpenAI /> },

    ],
  },
  {
    category: "Other Expertise",
    items: [
      { name: "Causal Machine Learning", icon: <AiOutlineOpenAI /> },
      { name: "React.Js", icon: <SiReact /> },
    ],
  },
];

const TechnologiesSection = () => {
  return (
    <Box p={8} backgroundColor="#d59bf6">
      <Heading as="h1" size="xl" textAlign="center" mb={8}>
        Technologies & Expertise
      </Heading>
      <SimpleGrid columns={[2, 2, 2]} spacing={8}>
        {technologies.map((tech) => (
          <Box
            key={tech.category}
            p={6}
            borderWidth="1px"
            borderRadius="lg"
            boxShadow="md"
            backgroundColor="#9896f1"
          >
            {/* Category Heading */}
            <Heading as="h2" size="md" mb={4}>
              {tech.category}
            </Heading>
            {/* List of Items */}
            <VStack alignItems="flex-start" spacing={2}>
              {tech.items.map((item) => (
                <HStack key={item.name} spacing={3}>
                  {/* Render Icon without custom color */}
                  <Box as="span">
                    {item.icon}
                  </Box>
                  {/* Render Technology Name */}
                  <Text fontSize="lg">{item.name}</Text>
                </HStack>
              ))}
            </VStack>
          </Box>
        ))}
      </SimpleGrid>
    </Box>
  );
};

export default TechnologiesSection;
