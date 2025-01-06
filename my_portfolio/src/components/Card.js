import { Box, Heading, HStack, Image, Text, VStack } from "@chakra-ui/react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowRight } from "@fortawesome/free-solid-svg-icons";
import React from "react";

const Card = ({ title, description, imageSrc }) => {
  
  // Implement the UI for the Card component according to the instructions.
  // You should be able to implement the component with the elements imported above.
  // Feel free to import other UI components from Chakra UI if you wish to.
  return (
  <Box borderWidth="1px" borderRadius="lg" overflow="hidden" bg="white">
      <Image src={imageSrc} />
          <VStack align="start" p={4} spacing={3}>
        <Heading size="md">{title}</Heading>
        <Text color="gray.600">{description}</Text>
        <HStack>
          <Text color="blue.500">Learn more</Text>
          <FontAwesomeIcon icon={faArrowRight} size="1x" color="#3182CE" />
        </HStack>
      </VStack>
      </Box>
  );
};

export default Card;
