# Repository for an Emotion Detection AI Tool

Made using NLP library for Emotion Analysis function of the WatsonAI NLP Library

## Sequence Diagram:

```mermaid

sequenceDiagram
    participant User
    participant FlaskApp
    participant WatsonNLP_API
    
    User->>FlaskApp: Submit text to analyze
    FlaskApp->>WatsonNLP_API: Send text for emotion detection
    WatsonNLP_API-->>FlaskApp: Return emotion analysis result
    FlaskApp-->>User: Display detected emotions and dominant emotion
