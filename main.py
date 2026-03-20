from langgraph.graph import StateGraph, START, END
from typing import TypedDict

class State(TypedDict):
    video_file: str
    audio_file: str
    transcript: str


