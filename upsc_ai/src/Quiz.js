import { useState } from 'react';
import React from 'react';
import Button from 'react-bootstrap/Button';
import Badge from 'react-bootstrap/Button';


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
      <div class = "alert alert-success" role = 'alert'>
        <card>
        <alert>
        <h2>Quiz Results</h2>
        <p>Score: {result.score}</p>
        <p>Correct Answers: {result.correctAnswers}</p>
        <p>Wrong Answers: {result.wrongAnswers}</p>
        </alert>
        </card>
      </div>
    );
  }

  return (
    <div>
      <h1>Quiz</h1>
      <h3>Question <Badge bg="dark">{activeQuestion+1}</Badge></h3>
      <h2>{quizData[activeQuestion].question}</h2>
      {quizData[activeQuestion].options.map((option, index) => (
        <div class="card">
          <div class="card-body">
        <Button class = "btn btn-primary"
          key={index} 
          onClick={() => handleAnswerSelection(option)}
          disabled={selectedAnswer !== ''}
        >
          {option}
        </Button>
        </div>
        </div>
      ))}
        <button onClick={handleNextQuestion} 
        class = "btn btn-primary" 
        disabled={selectedAnswer === ''}>
                    {activeQuestion < quizData.length - 1 ? 'Next Question' : 'Finish Quiz'}
        </button>
    </div>
  );
};

export default Quiz

