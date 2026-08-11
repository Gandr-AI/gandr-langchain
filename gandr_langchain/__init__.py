"""GandrText2SpeechTool: render text to speech with the Gandr TTS API from LangChain."""
import os
import tempfile
from typing import Optional, Type

from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field


class _TTSInput(BaseModel):
    text: str = Field(description="The text to speak out loud")


class GandrText2SpeechTool(BaseTool):
    """Render text to a WAV file with Gandr. Reads numbers, dates and order IDs
    correctly. One engine speaks 23 languages with six voices."""

    name: str = "gandr_text2speech"
    description: str = (
        "Render text to speech audio with the Gandr TTS API. "
        "Input is the text to speak. Output is the path of the generated WAV file. "
        "Use it when the agent must read numbers, dates, order IDs or addresses out loud."
    )
    args_schema: Type[BaseModel] = _TTSInput
    voice: str = "gandr-jenny"
    language: Optional[str] = None
    api_key: Optional[str] = None

    def _run(self, text: str) -> str:
        from gandr import Gandr

        key = self.api_key or os.environ.get("GANDR_API_KEY", "")
        if not key:
            raise ValueError("Gandr API key missing: pass api_key or set GANDR_API_KEY")
        g = Gandr(key)
        kwargs = {"voice": self.voice}
        if self.language:
            kwargs["language"] = self.language
        audio = g.say(text, **kwargs)
        path = os.path.join(tempfile.gettempdir(), "gandr_tts_output.wav")
        with open(path, "wb") as f:
            f.write(audio)
        return path
