# gandr-langchain

LangChain text to speech tool for the [Gandr TTS API](https://gandr.ai), built for voice agents.

- First audio byte in **146 ms over the open internet, 116 ms p50 first audio, server side warm**
- Reads numbers, dates, order IDs and addresses correctly
- One engine speaks **23 languages** with six voices
- **Every render watermarked** (imperceptible, detectable)
- **$10 a month for one million tokens**, or unlimited, unmetered stream plans from **$150/mo** (annual)

Free key starts at **100,000 tokens, no card**: [gandr.ai](https://gandr.ai)

## Install

```bash
pip install gandr-langchain
```

## Use

```python
from gandr_langchain import GandrText2SpeechTool

tool = GandrText2SpeechTool()          # reads GANDR_API_KEY from the environment
path = tool.run("Order number 4-2-7-1 ships on March 3rd.")
# path is a WAV file of the spoken line

# pick a voice or a language per tool instance
tool = GandrText2SpeechTool(voice="gandr-leo", language="es")
```

Drops into any LangChain agent as a standard tool: the model passes the text to speak,
gets back the audio file path.

Docs: [gandr.ai/docs](https://gandr.ai/docs) · Voices: `gandr-ava`, `gandr-dane`, `gandr-jenny`, `gandr-leo`, `gandr-lewis`, `gandr-mia`
