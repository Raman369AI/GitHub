import { useState } from 'react';
import React from 'react';
import Button from 'react-bootstrap/Button';
import Badge from 'react-bootstrap/Button';
import { Container, Box, ChakraProvider, HStack, VStack, defaultSystem, Card, Image , Heading, Highlight} from '@chakra-ui/react';
import image from './image.png';


// Then use it as React.useState in your component
const quizData = [
  {
    question: "What is the capital of France?",
    options: ["London", "Berlin", "Paris", "Madrid"],
    correctAnswer: "Paris"
  },{
    question: "What is the capital of France?",
    options: ["London", "Berlin", "Paris", "Madrid"],
    correctAnswer: "Paris"
  },
  // Add more questions...
];

const Quiz = () => {
  const [activeQuestion, setActiveQuestion] = useState(0)
  const [selectedAnswer, setSelectedAnswer] = useState('')
  const [result, setResult] = useState({
    score: 0,
    correctAnswers: 0,
    wrongAnswers: 0,
  })

  const [showResult, setShowResult] = useState(false);
  const handleAnswerSelection = (answer) =>{
    setSelectedAnswer(answer);
    if (answer === quizData[activeQuestion].correctAnswer) {
      setResult({
        ...result,
        score: result.score + 1,
        correctAnswers: result.correctAnswers + 1,
      })
    }
    else {
      setResult({
        ...result,
        wrongAnswers: result.wrongAnswers + 1,
      })
    }
  }
    
  const handleNextQuestion=() =>{
    if (activeQuestion < quizData.length - 1) {
      setActiveQuestion(activeQuestion + 1);
      setSelectedAnswer('');
    }
    else {
      setShowResult(true);
    }
  };
  
  if (showResult) {
    return (
      <Container centerContent = 'true' fluid = 'true' mt = "18" mb = "18">
      <Card.Root width = "500px" height = "500px" color = "teal" variant = "elevated" alignSelf={"center"}>
        <Card.Body gap = "2">
        <Card.Title>Quiz Results</Card.Title>
        <Heading size = 'sm' color = "#1352c">Score: {result.score}</Heading>
        <Heading size = 'sm'>Correct Answers: {result.correctAnswers}</Heading>
        <Heading size = 'sm'>Wrong Answers: {result.wrongAnswers}</Heading>
        </Card.Body>
      </Card.Root>
      </Container>
    );
  }

  return (
    <ChakraProvider value={defaultSystem}>
      <Box bg = "#e1eacd" color = "#01352c" borderRadius = "md" data-state="open"
  _open={{
    animation: "fade-in 300ms ease-out",
  }}
 >

    <Card.Root width = "700px" height = "700px" bg = "#e1eacd" color = "#01352c" variant = "elevated">
      <Card.Title><VStack>Quiz</VStack>Question <Badge bg="dark">{activeQuestion+1}</Badge></Card.Title>

      <h2>{quizData[activeQuestion].question}</h2>
      <Card.Body mt = "2" mb = "2">
      <VStack spacing={4} align="stretch">
      {quizData[activeQuestion].options.map((option, index) => (
        <Button
          key={index} 
          onClick={() => handleAnswerSelection(option)}
          disabled={selectedAnswer !== ''} colorPalette = "#01352c" variant = "elevated" mt = "4" mb = "4" bg = "#61b390" px = "0.5" py = "0.5" 
        >
          <Highlight query={selectedAnswer} bg = "#61b390" px = "0.5">{option}</Highlight>
        </Button>

      ))}        

<Button
  onClick={handleNextQuestion}
  disabled={selectedAnswer === ''}
  style={{
    backgroundColor: '#01352c',
    borderColor: '#61b390',
    color: '#bad8b6',
    marginTop: '24px',
  }}
>
  {activeQuestion < quizData.length - 1 ? 'Next Question' : 'Finish Quiz'}
</Button>

        </VStack>
        </Card.Body>

        </Card.Root>
        </Box>


    </ChakraProvider>

  );
};

export default Quiz

