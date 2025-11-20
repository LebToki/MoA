<img width="1200" height="630" alt="image" src="https://github.com/user-attachments/assets/efd1d88a-885a-4629-8313-a9d87d9e9e24" />



    ```sh
    git clone https://github.com/LebToki/MoA.git
    cd MoA
    ```

2. **Install Dependencies**:

    ```sh
    pip install -r requirements.txt
    ```
    
2.1. **List of Dependencies**

- **openai**: OpenAI API client library.
- **fire**: A Python library for creating command line interfaces.
- **loguru**: A library to make logging in Python simpler and more readable.
- **datasets**: Hugging Face's library for accessing and managing datasets.
- **typer**: A library for building command line interface applications.
- **rich**: A Python library for rich text and beautiful formatting in the terminal.
- **Flask**: A micro web framework for Python.
- **Flask-SQLAlchemy**: Adds SQLAlchemy support to Flask applications.
- **Flask-Uploads**: A flexible library to handle file uploading in Flask.
- **Werkzeug**: A comprehensive WSGI web application library.
- **Flask-Migrate**: Handles SQLAlchemy database migrations for Flask applications using Alembic.
- **PyMuPDF (fitz)**: A Python binding for MuPDF – a lightweight PDF and XPS viewer.
- **python-docx**: A Python library for creating and updating Microsoft Word (.docx) files.


3. **Set Up Environment Variables**:

    Create a `.env` file in the root directory and add your API keys:

    ```
    GROQ_API_KEY=your_groq_api_key
    OPENAI_API_KEY=your_openai_api_key
    DEBUG=0
    ```

### Running the Application

    Open your web browser and navigate to the following URL to access the web-based interface: 
```sh
    http://127.0.0.1:5000/
```


## Usage

### Interacting with the MoA Grog Chatbot

- **Model Selection**: Choose the model you want to use from the dropdown menu. The default model is `llama3-70b-8192`, which balances performance and speed.
  
- **Temperature Control**: Adjust the temperature setting to control the randomness and creativity of the chatbot's responses. The default value is `0.7`, providing a good balance between deterministic and varied outputs.
  
- **Max Tokens**: Define the maximum number of tokens (words or characters) for the response. The default is `2048`, which ensures comprehensive answers without overwhelming verbosity.
  
- **Create Your Topics**: Easily create new conversation topics by entering your desired topic names in the text field provided. This helps organize your interactions and revisit previous conversations.
  
- **Choose Your Topic**: Select a topic by clicking on it in the sidebar. The chat interface will load on the right, allowing you to continue your discussion seamlessly.
  
- **Instruction Input**: Enter your prompt or instruction in the text area. This is where you ask questions or provide commands to the chatbot.
  
- **Theme Toggle**: Enhance your user experience by switching between light and dark modes. Use the "Switch to Dark Mode" button to toggle themes based on your preference.
  
- **Submit and View Responses**: After filling in the necessary fields, submit the form to receive a response from the MoA Grog Chatbot. The response will be displayed on the same page, within the chat interface.

### Additional Features

- **Create New Conversations**: Use the sidebar to create new conversation topics, helping you manage different discussions effectively.
  
- **Reset All Conversations**: If needed, reset all conversations from the sidebar to start fresh.

This intuitive interface makes it easy to engage with the MoA Grog Chatbot, providing a seamless and interactive user experience.


### Planned Features

- **Uploading Documents**: The MoA Groq Chatbot will support file uploads and interact with the content of the uploaded documents, adding functionality to handle file uploads, process the contents of these files, and integrate the results into the chatbot's conversation flow.
- **Refine the styling**: With the latest Bootstrap and jQuery, we have room to enhance the UI/UX further.
- **Chronological ordering**: Move recent chats to the top (DESC order) to cut down on scrolling.
- **Further enhancement of the output**: Currently, not much has been implemented to control the output except basic styling. This is an area to be worked on based on various use cases.


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
    - `bot.png` - favicon


## Changelog
What's New in 1.1.0 · [02/07/2024]
- Implemented Dark Mode Support: Switch between light and dark themes for better usability.
- Enhanced UI/UX: Updated the styling of the chat interface, including better message formatting and improved layout.
- Improved Form Layout: Grouped form inputs on a single row for better space utilization.
- Sidebar Adjustment: Reduced the sidebar width to 180px to provide more space for the main chat interface.
- Document Upload Support: Added the ability to upload documents and interact with the content within the chatbot.
- Improved Sorting: Ensured conversation messages are displayed in descending order to prioritize the most recent interactions.

<details>
<summary>Previous Releases</summary>
Initial Release · [01/07/2024]

- Code Organization: Initial setup of the project with organized structure for controllers, models, and views.
- Error Handling: Basic error handling for API requests and user inputs.
- Front-end Enhancements: Initial design of the UI with Bootstrap and FontAwesome integration. Responsive design for better accessibility on all devices.
- Performance Considerations: Basic optimizations for faster loading times.
- Accessibility and Usability: Added alt attributes to all images for better accessibility.
</details>

## Acknowledgements

- **Original Creator**: Special thanks to the original creator of this amazing project. [togethercomputer](https://github.com/togethercomputer/MoA)
- **Matthew Berman**: A special thanks to [Matthew Berman](https://www.youtube.com/@matthew_berman) for showcasing this project and providing valuable insights.

## License

<p xmlns:cc="http://creativecommons.org/ns#" >This work by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://2tinteractive">Tarek Tarabichi</a> is licensed under <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"></a></p>

## Contributing

We welcome contributions! Please read the [CONTRIBUTING](CONTRIBUTING.md) guidelines before submitting a pull request.

# Note for Contributors
This project is based on Groq's API, not the original Together API. 
If you are contributing, please ensure compatibility and optimizations are aligned with Groq's specifications and guidelines.

## Contact

For any questions or feedback, please open an issue in this repository.

---
#  Get Involved
Whether you're a developer, system integrator, or enterprise user, you can trust that we did everything possible to make it as smooth and easy as 1,2,3 to set up MoA Groq Chatbot.

⭐ Give us a star on GitHub 👆

⭐ Fork the project on GitHub and contribute👆

🚀 Do you like to code? You're more than welcome to contribute Join the Discussions!

💡 Got a feature suggestion? Add your roadmap ideas

<br/>

This project is licensed under the Attribution License.
2024 · Tarek Tarabichi from 2TInteractive.com · Made with 💙

Thank you for using MoA Groq Chatbot!
We hope you find it useful and look forward to your contributions.

