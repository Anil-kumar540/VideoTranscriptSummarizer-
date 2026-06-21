<div align="center">
  <h1>🎬 Video Transcript Summarizer</h1>
  <p>
    <strong>A free, open-source video summarization tool powered by Hugging Face Transformers.</strong>
  </p>
  <p>
    Extract key information from YouTube videos instantly without relying on paid APIs like ChatGPT!
  </p>
</div>

<br />

<div align="center">
  <img src="screenshot.png" alt="Video Summarizer UI" width="800">
</div>

<br />

## 📖 About The Project

In today's fast-paced world, watching long videos to extract a few key points can be incredibly time-consuming. **Video Transcript Summarizer** is an AI-powered Streamlit web application designed to solve this problem. 

By feeding the app a standard YouTube link, it automatically fetches the video's closed captions and uses a state-of-the-art Deep Learning NLP model to generate a concise, highly readable summary—all processed locally on your machine for free.

## ✨ Key Features

- **Automated Transcript Extraction:** Instantly pulls caption data from YouTube without needing manual text entry.
- **Advanced NLP Summarization:** Utilizes the Hugging Face `BART` encoder-decoder architecture (`sshleifer/distilbart-cnn-12-6`) for high-quality, abstractive text summarization.
- **Rich, Interactive UI:** Built with Streamlit, featuring a clean layout, progress spinners, and custom styling.
- **Utility Tools Built-In:** One-click functionality to clear your session, copy the generated summary to your clipboard, or print the results to a PDF.
- **100% Free & Local:** No OpenAI API keys required. The model runs entirely on your local hardware.

## 💻 Technologies Used

This project was built using the following modern tech stack:

- **[Python](https://www.python.org/):** Core programming language.
- **[Streamlit](https://streamlit.io/):** For rapidly building the interactive web user interface.
- **[Hugging Face Transformers](https://huggingface.co/docs/transformers/index):** To load and execute the pre-trained NLP models.
- **[PyTorch](https://pytorch.org/):** The deep learning backend powering the model inference.
- **[youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/):** To scrape and parse closed captions directly from YouTube servers.
- **[BART](https://huggingface.co/sshleifer/distilbart-cnn-12-6):** Specifically, the `sshleifer/distilbart-cnn-12-6` encoder-decoder architecture for abstractive summarization.

## 🧠 How It Works (Technical Insights)

1. **Input:** The user provides a valid YouTube URL.
2. **Fetch:** The app parses the URL to extract the video ID and pings the `youtube-transcript-api` to retrieve the full spoken transcript.
3. **Tokenization:** The raw transcript is passed to the `AutoTokenizer`, which converts the text into PyTorch tensors (capped at 1024 tokens to manage memory and context limits).
4. **Generation:** The `AutoModelForSeq2SeqLM` (BART model) processes the tokens and outputs a highly condensed, abstractive summary (between 40 and 230 tokens).
5. **Display:** The summary is decoded back into human-readable text and displayed in a formatted, scrollable code block for easy reading and copying.

## 🚀 Getting Started

### Prerequisites
Make sure you have Python 3.8+ installed. You will also need `pip` to install the required packages.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/VideoTranscriptSummarizer.git
   cd VideoTranscriptSummarizer
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: Core dependencies include `streamlit`, `transformers`, `torch`, and `youtube-transcript-api`)*



> **Note on First Run:** The application will need to download the ~1.2GB `sshleifer/distilbart-cnn-12-6` model from Hugging Face during its first execution. Subsequent runs will be significantly faster as the model will be cached locally!

## 🛠️ Customization

The default model used is `"sshleifer/distilbart-cnn-12-6"`, which is highly optimized for news and generic article summarization. However, the code is entirely modular! You can swap this out for whichever Hugging Face Seq2Seq model suits your specific use case best.

---


