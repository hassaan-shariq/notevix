#backend code
from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File
import base64


load_dotenv()

app = FastAPI(
    title="Notevix AI API",
    description="AI-powered study tool backend",
    version="2.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "llama-3.1-8b-instant"


class TextInput(BaseModel):
    text: str


def call_groq(system_prompt: str, user_text: str, max_tokens: int = 500) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_text}
        ],
        max_tokens=max_tokens,
        temperature=0.4
    )
    return response.choices[0].message.content


@app.get("/")
def home():
    return {"message": "Notevix AI API v2.0 is running"}


@app.post("/summarize")
def summarize(input: TextInput):
    result = call_groq(
        system_prompt="""You are an expert academic summarizer.
        Create a clear, concise summary of the provided text.
        
        Rules:
        - Write 3-5 sentences maximum
        - Capture the core message and most important points
        - Use clear, professional language
        - Do not use bullet points — write in flowing prose
        - Start directly with the summary, no preamble""",
        user_text=input.text,
        max_tokens=300
    )
    return {"summary": result}


@app.post("/detailed-summary")
def detailed_summary(input: TextInput):
    result = call_groq(
        system_prompt="""You are an expert academic writer.
        Create a comprehensive, detailed summary of the provided text.

        Structure your response as:
        
        📋 OVERVIEW
        [2-3 sentences capturing the big picture]
        
        📌 MAIN POINTS
        [Cover each major section or argument in detail]
        
        💡 KEY INSIGHTS
        [What makes this content important or unique]
        
        📝 CONCLUSION
        [Final takeaway in 1-2 sentences]
        
        Be thorough and preserve all important information.""",
        user_text=input.text,
        max_tokens=800
    )
    return {"detailed_summary": result}


@app.post("/bullet-summary")
def bullet_summary(input: TextInput):
    result = call_groq(
        system_prompt="""You are an expert at distilling information.
        Convert the provided text into clean, scannable bullet points.
        
        Rules:
        - Maximum 8 bullet points
        - Each bullet = one complete, standalone idea
        - Start each bullet with •
        - Order from most to least important
        - Each bullet should be 1-2 sentences maximum
        - Be specific — avoid vague statements
        - Do not add any intro or outro text""",
        user_text=input.text,
        max_tokens=500
    )
    return {"bullet_summary": result}


@app.post("/key-points")
def key_points(input: TextInput):
    result = call_groq(
        system_prompt="""You are an expert study assistant.
        Extract exactly 5 key points from the provided text.
        
        Format each point as:
        🔑 Key Point [number]: [Bold title]
        [2-3 sentence explanation of why this point matters]
        
        Rules:
        - Focus on concepts that would appear in an exam
        - Prioritize understanding over memorization
        - Be specific with facts, numbers, and names
        - Do not add intro or conclusion text""",
        user_text=input.text,
        max_tokens=600
    )
    return {"key_points": result}


@app.post("/flashcards")
def flashcards(input: TextInput):
    result = call_groq(
        system_prompt="""You are an expert educator creating study flashcards.
        Generate exactly 5 high-quality flashcards from the provided text.
        
        Format each flashcard exactly as:
        
        ━━━━━━━━━━━━━━━━━━
        🃏 CARD [number]
        Q: [Clear, specific question]
        A: [Complete, accurate answer in 1-3 sentences]
        ━━━━━━━━━━━━━━━━━━
        
        Rules:
        - Questions should test understanding, not just memory
        - Answers should be complete and self-explanatory
        - Cover different aspects of the text
        - Avoid yes/no questions""",
        user_text=input.text,
        max_tokens=700
    )
    return {"flashcards": result}


@app.post("/quiz")
def quiz(input: TextInput):
    result = call_groq(
        system_prompt="""You are an expert exam creator.
        Create exactly 4 multiple choice questions from the provided text.
        
        Format each question exactly as:
        
        ❓ Question [number]:
        [Clear, specific question]
        
        A) [Option]
        B) [Option]
        C) [Option]
        D) [Option]
        
        ✅ Correct Answer: [Letter]) [Brief explanation of why this is correct]
        
        ─────────────────
        
        Rules:
        - Questions must be answerable from the text only
        - All 4 options must be plausible
        - Only one correct answer per question
        - Explanations should reinforce learning""",
        user_text=input.text,
        max_tokens=800
    )
    return {"quiz": result}


@app.post("/eli5")
def eli5(input: TextInput):
    result = call_groq(
        system_prompt="""You are a brilliant teacher who can explain anything simply.
        Explain the provided text as if talking to a curious 10-year-old.
        
        Structure:
        🌟 THE SIMPLE VERSION
        [2-3 sentences in the simplest possible language]
        
        🔍 BREAKING IT DOWN
        [Explain the 3 most important ideas using everyday analogies and examples]
        
        💬 IN ONE SENTENCE
        [Summarize everything in a single, memorable sentence]
        
        Rules:
        - No jargon or technical terms
        - Use real-life examples and comparisons
        - Be engaging and conversational
        - If you must use a technical term, immediately explain it""",
        user_text=input.text,
        max_tokens=600
    )
    return {"eli5": result}


@app.post("/exam-notes")
def exam_notes(input: TextInput):
    result = call_groq(
        system_prompt="""You are an expert at creating exam revision notes.
        Create comprehensive, exam-ready notes from the provided text.
        
        Format exactly as:
        
        📚 EXAM NOTES
        
        📌 TOPIC: [Main subject]
        📖 SUBTOPICS: [List related topics]
        
        ⭐ MUST-KNOW FACTS:
        1. [Critical fact]
        2. [Critical fact]
        3. [Critical fact]
        4. [Critical fact]
        5. [Critical fact]
        
        📝 KEY DEFINITIONS:
        • [Term]: [Definition]
        • [Term]: [Definition]
        
        ⚡ QUICK RECALL:
        [3 bullet points — the absolute minimum to remember]
        
        🎯 LIKELY EXAM QUESTIONS:
        1. [Probable exam question]
        2. [Probable exam question]
        
        💡 ONE-LINE SUMMARY:
        [The entire topic in one sentence]""",
        user_text=input.text,
        max_tokens=800
    )
    return {"exam_notes": result}


@app.post("/important-terms")
def important_terms(input: TextInput):
    result = call_groq(
        system_prompt="""You are an expert lexicographer and educator.
        Extract all important terms and concepts from the provided text.
        
        Format each term as:
        
        📖 [TERM NAME]
        Definition: [Clear, accurate definition]
        Context: [How it's used in this specific text]
        Remember: [One memorable way to remember this term]
        
        ─────────────────
        
        Rules:
        - Include 5-8 most important terms
        - Prioritize terms that would appear in exams
        - Definitions should be standalone and complete
        - Context should reference the source material""",
        user_text=input.text,
        max_tokens=700
    )
    return {"important_terms": result}


@app.post("/action-items")
def action_items(input: TextInput):
    result = call_groq(
        system_prompt="""You are an expert productivity consultant.
        Extract all explicit and implicit action items from the provided text.
        
        Format your response as:
        
        ✅ ACTION ITEMS
        
        🔴 IMMEDIATE ACTIONS (Do Today):
        1. [Specific, concrete action]
        2. [Specific, concrete action]
        
        🟡 SHORT-TERM ACTIONS (This Week):
        1. [Specific action with clear outcome]
        2. [Specific action with clear outcome]
        
        🟢 LONG-TERM ACTIONS (Ongoing):
        1. [Strategic action]
        2. [Strategic action]
        
        💡 KEY INSIGHT:
        [One sentence capturing the most important takeaway]
        
        Rules:
        - Every action must start with a verb (Build, Create, Learn, etc.)
        - Be specific — avoid vague advice
        - If text has no explicit actions, derive them from the content's lessons
        - Each action should be independently actionable""",
        user_text=input.text,
        max_tokens=700
    )
    return {"action_items": result}


@app.post("/faq")
def faq(input: TextInput):
    result = call_groq(
        system_prompt="""You are an expert at anticipating questions learners have.
        Generate 5 frequently asked questions with detailed answers.
        
        Format each as:
        
        ❓ Q[number]: [Question a student would genuinely ask]
        
        💬 A[number]: [Comprehensive answer that fully addresses the question]
        
        ─────────────────
        
        Rules:
        - Questions should reflect genuine confusion points
        - Answers must be complete — no "see above" references
        - Range from basic to advanced questions
        - Ground all answers in the provided text
        - Last question should be the most thought-provoking""",
        user_text=input.text,
        max_tokens=800
    )
    return {"faq": result}



@app.post("/extract-from-image")
async def extract_from_image(file: UploadFile = File(...)):
    # Read image file
    image_data = await file.read()
    base64_image = base64.b64encode(image_data).decode('utf-8')
    
    # Determine image type
    content_type = file.content_type or "image/jpeg"
    
    try:
        response = client.chat.completions.create(
            model="qwen/qwen3.6-27b",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:{content_type};base64,{base64_image}"
                            }
                        },
                        {
                            "type": "text",
                            "text": """Extract ALL text from this image completely and accurately.
                            If it's a textbook page, extract every word.
                            If it's handwritten notes, transcribe exactly.
                            If it's a whiteboard, capture everything.
                            Return only the extracted text, nothing else."""
                        }
                    ]
                }
            ],
            max_tokens=1000
        )
        
        extracted_text = response.choices[0].message.content
        return {
            "extracted_text": extracted_text,
            "message": "Text extracted successfully. You can now use this text with any Notevix feature."
        }
        
    except Exception as e:
        return {"error": f"Image processing failed: {str(e)}"}