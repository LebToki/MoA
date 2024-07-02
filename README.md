# MoA Chatbot

Welcome to the MoA (Mixture-of-Agents) Chatbot repository! This project leverages the collective strengths of multiple Large Language Models (LLMs) to enhance performance, achieving state-of-the-art results. MoA uses a layered architecture where each layer comprises several LLM agents, significantly outperforming traditional models.

## Overview

The MoA Chatbot utilizes a combination of open-source models to generate high-quality responses. This repository includes modifications that enable the MoA Chatbot to work with Groq, making it incredibly fast for local LLM inference.

![Light Mode](https://github.com/LebToki/MoA/assets/957618/aac6e231-c131-4313-a9ea-4043c2e32218)
![Dark Mode](https://github.com/LebToki/MoA/assets/957618/0486aa70-da5a-45a7-90e5-285c8c1b7e9a)
![persistant chat and topics](https://github.com/LebToki/MoA/assets/957618/6e2a5739-b775-4500-be7a-17e4266bafdb)

This was done on the quick, obviously can be styled further and enhanced but for the proof of concept it works just fine!

## Features

- **Multi-Model Integration**: Combines outputs from several models to produce the best possible response.
- **Interactive Web Interface**: Provides a user-friendly web interface for interaction.
- **High Performance**: Optimized for speed and efficiency with Groq.
- **Flexible Configuration**: Easily configurable via environment variables and settings.
- **Persistent Conversations**: Stores conversation data in an SQLite database for ongoing interactions.
- **Light/Dark Mode**: Switch between light and dark themes for better usability.2. **Install Dependencies**:

   ## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)
- Flask

### Installation

1. **Clone the Repository**:

    ```sh
    git clone https://github.com/LebToki/MoA.git
    cd MoA
    ```

2. **Install Dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**:

    Create a `.env` file in the root directory and add your API keys:

    ```
    GROQ_API_KEY=your_groq_api_key
    OPENAI_API_KEY=your_openai_api_key
    DEBUG=0
    ```

### Running the Application

    Open your web browser and go to `http://127.0.0.1:5000/`.

### Usage

- **Model**: Specify the model you want to use (default is `llama3-70b-8192`).
- **Temperature**: Control the randomness of the output (default is `0.7`).
- **Max Tokens**: Set the maximum number of tokens for the response (default is `2048`).
- **Create your topics**: Enter your topics names in the text field.
- **Choose your topic of choice**: by clicking on it and then the chat interface would load on your right.
- **Instruction**: Enter your prompt or instruction in the text area.
- **Theme Toggle**: Use the "Switch to Dark Mode" button to toggle between light and dark themes.

Submit the form to get a response from the MoA Grog Chatbot. 
The response will be displayed on the same page. You can create new conversation topics or reset all conversations from the sidebar.

## File Structure

- **MoA/**
  - `app.py` - Flask application
  - `bot.py` - Main chatbot logic
  - `utils.py` - Utility functions
  - `requirements.txt` - Python dependencies
  - **templates/**
    - `index.html` - HTML template for the web interface
    - `chat.html` - HTML template for the chat interface
  - **static/**
    - `style.css` - CSS styles for the web interface
    - `script.css` - JavaScript for theme switching and UI enhancements


## Acknowledgements

- **Original Creator**: Special thanks to the original creator of this amazing project. [togethercomputer](https://github.com/togethercomputer/MoA)
- **Matthew Berman**: A special thanks to [Matthew Berman](https://www.youtube.com/@matthew_berman) for showcasing this project and providing valuable insights.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

We welcome contributions! Please read the [CONTRIBUTING](CONTRIBUTING.md) guidelines before submitting a pull request.

## Contact

For any questions or feedback, please open an issue in this repository.

---

Thank you for using MoA Chatbot! 
We hope you find it useful and look forward to your contributions.

