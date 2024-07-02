# MoA Grog Chatbot

Welcome to the MoA (Mixture-of-Agents) Chatbot repository! 
This project leverages the collective strengths of multiple Large Language Models (LLMs) to enhance performance, achieving state-of-the-art results. 
MoA uses a layered architecture where each layer comprises several LLM agents, significantly outperforming traditional models.

The MoA Grog Chatbot leverages a powerful combination of open-source models to generate high-quality responses, ensuring both accuracy and relevance. 
This repository includes essential modifications to enable the MoA Chatbot to work seamlessly with Groq, resulting in incredibly fast local LLM inference.

In addition to the core functionality, I've integrated a user-friendly web-based interface, replacing the previous command-line interaction. 
This interface provides a more accessible and visually appealing way to engage with the chatbot. 
While the current design serves as a proof of concept, demonstrating the chatbot's capabilities effectively, there is ample room for further styling and enhancements to refine the user experience.


![Light Mode](https://github.com/LebToki/MoA/assets/957618/aac6e231-c131-4313-a9ea-4043c2e32218)
![Dark Mode](https://github.com/LebToki/MoA/assets/957618/0486aa70-da5a-45a7-90e5-285c8c1b7e9a)
![persistant chat and topics](https://github.com/LebToki/MoA/assets/957618/6e2a5739-b775-4500-be7a-17e4266bafdb)



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

- **Model Selection**: Choose the model you want to use from the dropdown menu. The default model is llama3-70b-8192, which balances performance and speed.
- **Temperature Control**: Adjust the temperature setting to control the randomness and creativity of the chatbot's responses. The default value is 0.7, providing a good balance between deterministic and varied outputs.
- **Max Tokens**: Define the maximum number of tokens (words or characters) for the response. The default is 2048, which ensures comprehensive answers without overwhelming verbosity.
- **Create Your Topics**: Easily create new conversation topics by entering your desired topic names in the text field provided. This helps organize your interactions and revisit previous conversations.
- **Choose Your Topic**: Select a topic by clicking on it in the sidebar. The chat interface will load on the right, allowing you to continue your discussion seamlessly.
- **Instruction Input**: Enter your prompt or instruction in the text area. This is where you ask questions or provide commands to the chatbot.
- **Theme Toggle**: Enhance your user experience by switching between light and dark modes. Use the "Switch to Dark Mode" button to toggle themes based on your preference.
- **Submit and View Responses**: After filling in the necessary fields, submit the form to receive a response from the MoA Grog Chatbot. The response will be displayed on the same page, within the chat interface. 

### Additional Features
- **Create New Conversations**: Use the sidebar to create new conversation topics, helping you manage different discussions effectively.
- **Reset All Conversations**:  If needed, reset all conversations from the sidebar to start fresh.

This intuitive interface makes it easy to engage with the MoA Grog Chatbot, providing a seamless and interactive user experience.


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

