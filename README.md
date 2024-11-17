# Chat with PDF - README

## Overview

**Chat with PDF** is a Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and engage in interactive chat sessions to query information from the documents. This tool leverages AI techniques to parse and understand the content of PDFs, enabling seamless and precise information retrieval.

---

## Features

- **PDF Upload:** Upload single or multiple PDF files.
- **Interactive Chat:** Ask questions about the content of the uploaded PDFs and receive concise, AI-generated answers.
- **Context-Aware Retrieval:** Combines the power of natural language processing with vector-based search for accurate results.
- **User-Friendly Interface:** Intuitive design built with Streamlit for ease of use.

---

## Prerequisites

Before starting, ensure you have the following installed:

- Python (>= 3.8)
- Virtual Environment tool (e.g., `venv`)

---

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Vjay15/chat-with-pdf.git
    cd chat-with-pdf
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv myvenv
    myvenv\Scripts\activate  # Windows
    source myvenv/bin/activate  # macOS/Linux
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

---

## Running the Application

1. Start the Streamlit application:

    ```bash
    streamlit run app.py
    ```

2. Open the application in your browser using the URL provided in the terminal, typically `http://localhost:8501`.

---

## Usage

1. **Upload a PDF:** Click on the upload button and select your PDF files.
2. **Ask Questions:** Enter your questions in the text input field.
3. **Get Answers:** The AI model retrieves and summarizes relevant content from the uploaded PDFs.

---

## Technology Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **NLP:** Large Language Models (LLMs) for question answering
- **Search Engine:** Vector-based similarity search for document retrieval
- **Libraries:** 
  - PyPDF2 (or equivalent) for PDF parsing
  - FAISS (or equivalent) for vector search
  - OpenAI/LLM APIs for natural language understanding

---

## Limitations

- The application works best with text-based PDFs. Scanned or image-based PDFs may require OCR preprocessing.
- The accuracy of responses depends on the clarity and formatting of the PDF content.

---

## Future Enhancements

- Add support for more file formats.
- Implement multilingual question answering.
- Integrate advanced document summarization.
- Enhance the UI for a better user experience.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

---

## License

This project is licensed under the GPL-3.0 License. See the `LICENSE` file for more details.

