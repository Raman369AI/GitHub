import { useState } from 'react';
import React from 'react';
import Button from 'react-bootstrap/Button';
import Badge from 'react-bootstrap/Button';
import { Container, Box, ChakraProvider, HStack, VStack, defaultSystem, Card, Image , Heading, Highlight} from '@chakra-ui/react';
import image from './image.png';
import {
  DialogActionTrigger,
  DialogBody,
  DialogCloseTrigger,
  DialogContent,
  DialogFooter,
  DialogHeader,
  DialogRoot,
  DialogTitle,
  DialogTrigger,
} from '@chakra-ui/react'
// Then use it as React.useState in your component
const quizData = [{'question': 'Who burned foreign cloth?', 'correctAnswer': 'Gandhi', 'options': ['Shashi Tharoor', 'Ambedkar', 'Manusmriti', 'Gandhi']}, 
{'question': 'Who burned Manusmriti?', 'correctAnswer': 'Ambedkar', 'options': ['Rafi-ud-Daula', 'Gandhi', 'Savarkar', 'Ambedkar']},
{'question': 'Who was the Rohilla chief?', 'correctAnswer': 'Najib- ud-Daula', 'options': ['A.H. Ghuznavi', 'Aga Khan III', 'Muhammad Zafarullah Khan', 'Najib- ud-Daula']}, 
{'question': "Who was the personal 'supreme agent' of Abdali?", 'correctAnswer': 'Najib- ud-Daula', 'options': ['Abdur Rehman', 'Abdali', 'Mir Bakhshi', 'Najib- ud-Daula']}, 
{'question': 'Who joined Mulraj?', 'correctAnswer': 'Sher Singh', 'options': ['Mulraj', 'N.G. Chandavarkar', 'Sher Singh', 'R.G. Bhandarkar']}, 
{'question': 'What led to a mass uprising in Multan?', 'correctAnswer': 'Both Mulraj and Sher Singh', 'options': ['Both Mulraj and Sher Singh', 'Sher Singh', 'Mulraj', 'Birsa Munda']}]



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
  
  
  return (
    <ChakraProvider value={defaultSystem}>
      {showResult? (
   
   <DialogRoot  placement = "bottom" >
    <DialogTrigger placement = "center">
    <Button
  variant="elevate"
  style={{
    position: "relative",
    top: "-52px",      // Adjust vertical position
    right: "-250px",    // Adjust horizontal position
  }}
>
  Check results
</Button>

    </DialogTrigger>
    <DialogContent>
      <DialogHeader>
        <DialogTitle>Dialog Title</DialogTitle>
      </DialogHeader>
      <DialogBody>
      <Heading size = 'sm' color = "#1352c">Score: {result.score}</Heading>
      <Heading size = 'sm'>Correct Answers: {result.correctAnswers}</Heading>
      <Heading size = 'sm'>Wrong Answers: {result.wrongAnswers}</Heading>
      </DialogBody>
      <DialogFooter>
        <DialogActionTrigger asChild>
          <Button variant="outline">Close</Button>
        </DialogActionTrigger>
     
      </DialogFooter>
      <DialogCloseTrigger />
    </DialogContent>
  </DialogRoot>)
  :
      (<Box bg = "#e1eacd" color = "#01352c" borderRadius = "md" data-state="open"
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
        </Box>)}


    </ChakraProvider>

  );
};

export default Quiz






