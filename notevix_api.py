from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


class TextInput(BaseModel):
    text: str


@app.get("/")
def home():
    return {"message": "Notevix API is running"}


@app.post("/summarize")  
def summarize(input: TextInput):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "Summarize the following text concisely."
            },
            {
                "role": "user",
                "content": input.text
            }
        ],
        max_tokens=200
    )
    return {"summary": response.choices[0].message.content}


@app.post("/key-points")
def key_points(input: TextInput):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "Extract 5 key points from this text as bullet points."
            },
            {
                "role": "user",
                "content": input.text
            }
        ],
        max_tokens=200
    )
    return {"key_points": response.choices[0].message.content}

@app.post("/flashcards")
def flashcards(input: TextInput):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "Create 5 flashcards from this text. Each flashcard should have a question and an answer."
            },
            {
                "role": "user",
                "content": input.text
            }
        ],
        max_tokens=300
    )
    return {"flashcards": response.choices[0].message.content}

@app.post("/quiz")
def quiz(input: TextInput):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": """Create 3 multiple choice questions from this text.
                Format each as:
                Q: [question]
                A) [option]
                B) [option]
                C) [option]
                D) [option]
                Answer: [correct letter]"""
            },
            {
                "role": "user",
                "content": input.text
            }

        ],
        max_tokens=400
    )
    return {"quiz": response.choices[0].message.content}

@app.post("/eli5")
def eli5(input: TextInput):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "Explain this text like I'm 5 years old. Simple words, short sentences."
            },
            {
                "role": "user",
                "content": input.text
            }
        ],
        max_tokens=200
    )
    return {"eli5": response.choices[0].message.content}


@app.post("/exam-notes")
def exam_notes(input: TextInput):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": """Create concise exam revision notes from this text.
                Format as:
                📌 Topic: [main topic]
                Key facts to remember:
                • [fact 1]
                • [fact 2]
                • [fact 3]
                Important terms: [list them]
                One line summary: [summary]"""
            },
            {
                "role": "user",
                "content": input.text
            }
        ],
        max_tokens=300
    )
    return {"exam_notes": response.choices[0].message.content}


@app.post("/important-terms")
def important_terms(input: TextInput):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": """Extract important terms and definitions from this text.
                Format each as:
                Term: [term]
                Definition: [clear definition]"""
            },
            {
                "role": "user",
                "content": input.text
            }
        ],
        max_tokens=300
    )
    return {"important_terms": response.choices[0].message.content}


@app.post("/action-items")
def action_items(input: TextInput):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": """Extract all action items and tasks from this text.
                Format as a numbered list:
                1. [action item]
                2. [action item]
                If no action items exist, suggest 3 study actions based on the content."""
            },
            {
                "role": "user",
                "content": input.text
            }
        ],
        max_tokens=200
    )
    return {"action_items": response.choices[0].message.content}

@app.post("/faq")
def faq(input: TextInput):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": """Generate 5 frequently asked questions 
                with answers based on this text.
                Format each as:
                Q: [question]
                A: [answer]"""
            },
            {
                "role": "user",
                "content": input.text
            }
        ],
        max_tokens=400
    )
    return {"faq": response.choices[0].message.content}


@app.post("/bullet-summary")
def bullet_summary(input: TextInput):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": """Convert this text into clean bullet points.
                Each bullet should be one clear, complete idea.
                Maximum 8 bullets.
                Start each with •"""
            },
            {
                "role": "user",
                "content": input.text
            }
        ],
        max_tokens=300
    )
    return {"bullet_summary": response.choices[0].message.content}