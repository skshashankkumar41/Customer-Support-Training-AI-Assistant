# Customer Support Training AI Assistant

Welcome to the Customer Support Training AI Assistant! This project aims to create an interactive assistant that helps train customer support representatives by simulating real conversations with customers. The assistant uses state-of-the-art speech-to-text, language processing, and text-to-speech technologies to provide a realistic training environment.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Speech Recognition:** Uses Whisper for accurate speech-to-text conversion.
- **Natural Language Processing:** Utilizes the Ollama language model to generate realistic customer responses.
- **Text-to-Speech:** Provides audio responses using a custom Text-to-Speech service.
- **Interactive Interface:** A console-based interface for seamless interaction.
- **Customer Profiles:** Simulates different customer scenarios with predefined emotions and problems.

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/customer-support-training-ai-assistant.git
    cd customer-support-training-ai-assistant
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Download additional NLTK data:**
    ```python
    import nltk
    nltk.download('punkt')
    ```

## Usage

1. **Run the main script:**
    ```sh
    python main.py
    ```

2. **Follow the console instructions:**
    - Enter the customer's name when prompted.
    - Press Enter to start recording and press Enter again to stop.
    - The assistant will transcribe the audio, generate a response, and play it back.

3. **To exit the program:**
    - Press `Ctrl+C`.

## Architecture

- **Recording Audio:** Captures audio input from the microphone using the `sounddevice` library.
- **Transcription:** Converts audio to text using the Whisper model.
- **Response Generation:** Processes the transcribed text using the Ollama language model to generate a response.
- **Text-to-Speech:** Converts the text response to audio using a custom Text-to-Speech service.
- **Console Interface:** Manages user interaction and displays status messages.

## Contributing

We welcome contributions to enhance this project! Please follow these steps:

1. **Fork the repository.**
2. **Create a new branch:**
    ```sh
    git checkout -b feature/your-feature-name
    ```
3. **Make your changes and commit them:**
    ```sh
    git commit -m 'Add some feature'
    ```
4. **Push to the branch:**
    ```sh
    git push origin feature/your-feature-name
    ```
5. **Open a pull request.**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Thank you for using the Customer Support Training AI Assistant! We hope it provides valuable training for your customer support representatives. If you have any questions or suggestions, please open an issue or contribute to the project.
