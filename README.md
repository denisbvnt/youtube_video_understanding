# 📺 YouTube Video Understanding

**YouTube Video Understanding** is a Python-based application that enables users to interact with YouTube video content through a conversational interface. Utilizing **Streamlit** for the user interface and **Large Language Models (LLMs)** for natural language understanding, this tool allows for efficient querying and summarization of video content.

## 📁 Project Structure

- `main.py`: Launches the Streamlit application.
- `models.py`: Handles the loading and management of LLMs.
- `templates.py`: Contains prompt templates and processes user input for the models.
- `tasks.py`: Implements specific tasks the assistant can perform.
- `requirements.txt`: Lists all project dependencies.

## 🚀 How to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/denisbvnt/youtube_video_understanding.git
   cd youtube_video_understanding
   ```

2. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app:**

   ```bash
   streamlit run main.py
   ```

4. The application will automatically open in your default browser (usually at `http://localhost:8501`).

## 🧠 Features

- Interactive interface built with Streamlit.
- Natural language processing powered by LLMs.
- Dynamic prompt generation based on user input.
- Execution of document-related tasks through conversational commands.

## 🛠️ Technologies Used

- **Python** – Core programming language.
- **Streamlit** – Framework for building the web interface.
- **LangChain** – Framework for developing applications powered by LLMs.
- **Hugging Face Transformers** – Access to pre-trained LLMs for text processing.
- **LLMs** – Used for understanding and generating human-like text.
- Additional libraries listed in `requirements.txt`.

## 📷 Screenshot

![image](https://github.com/user-attachments/assets/97930720-d01c-4ea0-8ea3-c90508b41852)


## 📄 License

This project is licensed under the [MIT License](LICENSE).
