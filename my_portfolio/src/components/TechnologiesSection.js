import React from "react";
import { Box, Heading, VStack, Text, SimpleGrid, HStack } from "@chakra-ui/react";
import { FaPython, FaJsSquare, FaRProject, FaDatabase, FaDocker } from "react-icons/fa";
import { SiKeras, SiPytorch, SiFastapi, SiHuggingface, SiApachespark, SiLinux } from "react-icons/si";

const technologies = [
  {
    category: "Programming Languages",
    items: [
      { name: "SQL", icon: <FaDatabase /> },
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
      { name: "Excel", icon: <FaDatabase /> },
      { name: "SAS", icon: <FaDatabase /> },
      { name: "Tableau", icon: <FaDatabase /> },
      { name: "Power BI", icon: <FaDatabase /> },
      { name: "SQL Server Management Studio (SSMS)", icon: <FaDatabase /> },
      { name: "MongoDB", icon: <FaDatabase /> },
      { name: "Looker Studio", icon: <FaDatabase /> },
    ],
  },
  {
    category: "Cloud & DevOps Platforms",
    items: [
      { name: "Azure", icon: <FaDatabase /> },
      { name: "Databricks", icon: <FaDatabase /> },
      { name: "Google Cloud Platform (GCP)", icon: <FaDatabase /> },
      { name: "Docker", icon: <FaDocker /> },
    ],
  },
  {
    category: "Other Expertise",
    items: [
      { name: "Machine Learning", icon: <SiLinux /> },
      { name: "Generative AI", icon: <SiLinux /> },
      { name: "Linux", icon: <SiLinux /> },
      { name: "Causal Machine Learning", icon: <SiLinux /> },
      { name: "ML-Ops", icon: <FaDocker /> },
      { name: "React.Js", icon: <FaJsSquare /> },
    ],
  },
];

const TechnologiesSection = () => {
  return (
    <Box p={8} backgroundColor="#f7fafc">
      <Heading as="h1" size="xl" textAlign="center" mb={8}>
        Technologies & Expertise
      </Heading>
      <SimpleGrid columns={[1, 2, 2]} spacing={8}>
        {technologies.map((tech) => (
          <Box
            key={tech.category}
            p={6}
            borderWidth="1px"
            borderRadius="lg"
            boxShadow="md"
            backgroundColor="white"
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
