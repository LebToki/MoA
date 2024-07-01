# Mixture-of-Agents (MoA)
# MoA Chatbot

Welcome to the MoA (Mixture-of-Agents) Chatbot repository! This project leverages the collective strengths of multiple Large Language Models (LLMs) to enhance performance, achieving state-of-the-art results. MoA uses a layered architecture where each layer comprises several LLM agents, significantly outperforming traditional models.

## Overview

The MoA Chatbot utilizes a combination of open-source models to generate high-quality responses. This repository includes modifications that enable the MoA Chatbot to work with Groq, making it incredibly fast for local LLM inference.

![image](https://github.com/LebToki/MoA/assets/957618/2ecc95fb-2197-4767-befd-a27974d30dcc)
This was done on the quick, obviously can be styled further and enhanced but for the proof of concept it works just fine!

## Features

- **Multi-Model Integration**: Combines outputs from several models to produce the best possible response.
- **Interactive Web Interface**: Provides a user-friendly web interface for interaction.
- **High Performance**: Optimized for speed and efficiency with Groq.
- **Flexible Configuration**: Easily configurable via environment variables and settings.

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
    GROQ_API_KEY="your_groq_api_key"
    OPENAI_API_KEY="your_openai_api_key"
    DEBUG=1
    ```

### Running the Application

1. **Start the Flask Application**:

    ```sh
    python app.py
    ```

2. **Access the Web Interface**:

    Open your web browser and go to `http://127.0.0.1:5000/`.

### Usage

- **Model**: Specify the model you want to use (default is `llama3-70b-8192`).
- **Temperature**: Control the randomness of the output (default is `0.7`).
- **Max Tokens**: Set the maximum number of tokens for the response (default is `2048`).
- **Instruction**: Enter your prompt or instruction in the text area.

Submit the form to get a response from the MoA Chatbot. The response will be displayed on the same page.

## File Structure

- **MoA/**
  - `app.py` - Flask application
  - `bot.py` - Main chatbot logic
  - `utils.py` - Utility functions
  - `requirements.txt` - Python dependencies
  - **templates/**
    - `index.html` - HTML template for the web interface
  - **static/**
    - `style.css` - CSS styles for the web interface


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

