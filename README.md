# Customized LLMs response with your information

This project is designed to run a script called `customized.py`, which utilizes various AI services and APIs. Follow the steps below to prepare the necessary credentials and set up the environment.

## Prerequisites

1. **Google Cloud Credentials**
   - Go to [Google Cloud Console](https://cloud.google.com/console/).
   - Create or select a project.
   - Enable the googledoc API required for your application.
   - Download the `credentials.json` file:
     - Navigate to **APIs & Services > Credentials**.
     - Create a new service account key (if not already available).
     - Download the JSON file and place it in the root directory of this project.

2. **API Keys for LLMs**
   - Obtain API keys for the large language models you plan to use:
     - **ChatGPT**: Get your API key from [OpenAI's API page](https://platform.openai.com/).
     - **ClaudeAI**: Obtain access and API keys via [Anthropic](https://www.anthropic.com/).
     - **DeepSeek**: Refer to their [official documentation](https://deepseek.ai/) for API key generation.
   - Store these keys securely and ensure they are accessible in your code (e.g., environment variables or a configuration file).

## Installation

1. **Clone the Repository**
   - Clone this project to your local machine:
     ```bash
     git clone https://github.com/IntArchive/Customized_ChatGPT_with_your_own_corpus.git
     cd Customized_ChatGPT_with_your_own_corpus
     ```

2. **Install Dependencies**
   - Use `pip` to install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```

## Usage

1. Ensure that:
   - The `credentials.json` file is in the root directory.
   - The required API keys are configured correctly (e.g., in a `.env` file or environment variables).

2. Run the script:
   ```bash
   python customized.py
   ```


## License

This project is licensed under MIT License. See the `LICENSE` file for more details.
Feel free to adjust the instructions to match your project's specifics or add more details about how to set up credentials or configure the environment.



