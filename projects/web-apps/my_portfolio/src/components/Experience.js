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
      title: "Research Assistant",
      dates: "October 2023 - May 2025",
      description: [
        "Streamlined Wings of Hope’s CAP60 data ingestion into BigQuery by engineering robust, reusable, and efficient SQL stored procedures leveraging BigQuery's procedural language capabilities.",
        "Extracted critical insights to facilitate data-driven decision-making and support strategic initiatives by performing complex SQL analysis on large datasets.",
        "Enhanced operational visibility and decision-making for senior stakeholders by developing and deploying automated,interactive Tableau dashboards, which provided timely KPI insights via Tableau Server subscriptions and eliminated manual reporting efforts, resulting in significant time savings."
      ],
    },
    {
      id: "exp-2",
      company: "GVMC, India",
      title: "Data Scientist",
      dates: "2019 - 2023",
      description: [
        "Built a property tax delinquency prediction pipeline using ensemble ML models and validated behavioral patterns with logistic regression and chi-square tests; achieved 27% improvement in detection accuracy and reduced late payments by 10% through targeted interventions aligned with JLL's financial compliance framework",
        "Segmented 1.6M+ property owners using K-Means clustering based on property type, location, and payment history, validating cluster differentiation using post-hoc ANOVA and silhouette scores to enable hyper-targeted outreach",
        "Conducted Randomized Controlled Trials (RCT) measuring tax reminder intervention effects using difference-in-means testing and regression analysis, quantifying 28% increase in on-time compliance and 22% reduction in enforcement workload",
        "Automated daily operational reporting through SQL-driven Power BI dashboards, improving data visibility for stakeholders and reducing manual reporting time by 40%",
        "Delivered tailored insights for ad hoc requests by performing complex data extraction and analysis entirely in SQL, streamlining workflows and accelerating cross-departmental decision-making"
    ]
    ,
    },
    {
      id: "exp-3",
      company: "Chegg",
      title: "Data Scientist",
      dates: "2016 - 2019",
      description: [
        "Built customer lifetime value estimation models using purchase frequency, recency, and behavioral signals; applied clustering to group users by lifecycle stage, enabling marketing teams to prioritize retention/acquisition efforts and optimize Customer Acquisition Cost (CAC)",
        "Modeled churn risk and conversion likelihood through SQL-based funnel analytics and survival analysis, extracting time-to-churn metrics and cohort retention rates to improve Net Revenue Retention (NRR) via Tableau dashboards that informed monthly forecasting",
        "Designed A/B tests for product/pricing experiments using statistical testing (t-tests, regression) and causal inference methods, quantifying Uplift, Conversion Rate (CR), and Return on Investment (RoI) to guide feature adoption and pricing strategies",
        "Delivered quarterly acquisition/retention insights across product lines by creating Tableau dashboards tracking engagement trends, enabling data-driven decisions for Chegg's growth and product teams"
    ]
    ,
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
      bg="white" // Dark card background
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
