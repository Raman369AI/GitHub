import React, { useState } from "react";
import { VStack, Heading, Input, Textarea, Button, Box, Select } from "@chakra-ui/react";
import FullScreenSection from "./FullScreenSection";

const LandingSection = () => {
  const [textInput, setTextInput] = useState("");
  const [videoUrl, setVideoUrl] = useState("");
  const [difficulty, setDifficulty] = useState("1");
  const [questionType, setQuestionType] = useState("Regular");

  const handleGenerateQuiz = () => {
    console.log("Text:", textInput);
    console.log("Video URL:", videoUrl);
    console.log("Difficulty:", difficulty);
    console.log("Question Type:", questionType);
    // Later you can call your backend API here
  };

  return (
    <FullScreenSection
      justifyContent="center"
      alignItems="center"
      isDarkBackground
      backgroundColor="#001a1a"
    >
      <Box
        bg="white"
        p={8}
        rounded="2xl"
        boxShadow="lg"
        width="90%"
        maxWidth="600px"
      >
        <VStack spacing={6} align="stretch">
          {/* Title */}
          <Heading
            as="h2"
            size="xl"
            fontFamily="Georgia"
            color="teal.700"
            textAlign="center"
          >
            AI-Powered Quiz Generator
          </Heading>

          {/* Text Input */}
          <VStack align="stretch" spacing={1}>
            <Heading as="h3" size="sm" color="teal.600">
              Paste Text (Article / Notes)
            </Heading>
            <Textarea
              placeholder="Enter text content here..."
              value={textInput}
              onChange={(e) => setTextInput(e.target.value)}
              bg="white"
              color="black"
              _placeholder={{ color: "gray.500" }}
              focusBorderColor="teal.400"
              borderRadius="md"
              minH="120px"
            />
          </VStack>

          {/* OR Separator */}
          <Heading as="h3" size="sm" color="teal.500" textAlign="center">
            — OR —
          </Heading>

          {/* Video URL Input */}
          <VStack align="stretch" spacing={1}>
            <Heading as="h3" size="sm" color="teal.600">
              Video URL (optional)
            </Heading>
            <Input
              placeholder="Paste YouTube or video link here..."
              value={videoUrl}
              onChange={(e) => setVideoUrl(e.target.value)}
              bg="white"
              color="black"
              _placeholder={{ color: "gray.500" }}
              focusBorderColor="teal.400"
              borderRadius="md"
            />
          </VStack>

          {/* Difficulty Dropdown */}
          <VStack align="stretch" spacing={1}>
            <Heading as="h3" size="sm" color="teal.600">
              Select Difficulty (1 = Easy, 5 = Hard)
            </Heading>
            <Select.Root value={difficulty} onValueChange={setDifficulty}>
              <Select.HiddenSelect />
              <Select.Control>
                <Select.Trigger>
                  <Select.ValueText placeholder="Select Difficulty" />
                </Select.Trigger>
                <Select.IndicatorGroup>
                  <Select.Indicator />
                  <Select.ClearTrigger />
                </Select.IndicatorGroup>
              </Select.Control>
              <Select.Positioner>
                <Select.Content>
                  <Select.Item value="1">1 - Very Easy</Select.Item>
                  <Select.Item value="2">2 - Easy</Select.Item>
                  <Select.Item value="3">3 - Medium</Select.Item>
                  <Select.Item value="4">4 - Hard</Select.Item>
                  <Select.Item value="5">5 - Very Hard</Select.Item>
                </Select.Content>
              </Select.Positioner>
            </Select.Root>
          </VStack>

          {/* Question Type Dropdown */}
          <VStack align="stretch" spacing={1}>
            <Heading as="h3" size="sm" color="teal.600">
              Type of Questions
            </Heading>
            <Select.Root value={questionType} onValueChange={setQuestionType}>
              <Select.HiddenSelect />
              <Select.Control>
                <Select.Trigger>
                  <Select.ValueText placeholder="Select Type" />
                </Select.Trigger>
                <Select.IndicatorGroup>
                  <Select.Indicator />
                  <Select.ClearTrigger />
                </Select.IndicatorGroup>
              </Select.Control>
              <Select.Positioner>
                <Select.Content>
                  <Select.Item value="Regular">Regular</Select.Item>
                  <Select.Item value="MCQ">MCQ (Single Correct)</Select.Item>
                  <Select.Item value="MultiSelect">MultiSelect (Multiple Correct)</Select.Item>
                  <Select.Item value="TrueFalse">True or False</Select.Item>
                </Select.Content>
              </Select.Positioner>
            </Select.Root>
          </VStack>

          {/* Generate Quiz Button */}
          <Button
            colorScheme="teal"
            size="lg"
            onClick={handleGenerateQuiz}
            bgGradient="linear(to-r, teal.400, teal.500)"
            _hover={{
              bgGradient: "linear(to-r, teal.500, teal.600)",
              boxShadow: "xl",
            }}
            borderRadius="full"
          >
            Generate Quiz
          </Button>
        </VStack>
      </Box>
    </FullScreenSection>
  );
};

export default LandingSection;
