# AskMe

## About Project
This project is a Retrieval-Augmented Generation (RAG) based application that allows users to upload a textual image and input a prompt (question) related to the image. The system, powered by the Gemini LLM (`gemini-1.5-flash`), processes the image and the prompt to generate relevant responses.

## Features:

- Upload a textual image and ask questions about it
- Uses Gemini LLM for intelligent response generation
- Simple and user-friendly interface
- Fully automated setup with `setup.py`

## Installation & Setup:
1. Clone the Repository
```
git clone https://github.com/milad818/askme.git
cd askme
```

2. Create Environment (Optional):
You can create and activate an isolate environment to keep dependencies in check.
```
conda create -n askme python=3.10 -y
conda activate askme
```

3. Install Dependencies
Make sure you have Python installed (>= 3.8). Then, run:

```
python setup.py install
```
This installs all required dependencies, including local ones.

4. Run the Application

```
python app.py
```

This starts the application locally. You can then access it via the local host at your terminal after execution. At times, it automatically opens the browser.

Hope you enjoy the experience!

