# Style Prompt Web Application

This project is a web application that allows users to upload an image and receive a cinematic, Midjourney-style prompt for that image. The generated prompt can be used in other chatbots to create similar images.

## Features

- Upload images to the web application.
- Generate cinematic prompts using the Groq API based on the uploaded images.
- Store images in Azure Blob Storage.

## Project Structure

```
style-prompt-webapp
├── src
│   ├── app.py                # Main entry point of the web application
│   ├── templates
│   │   ├── index.html        # HTML template for the upload page
│   │   └── result.html       # HTML template for displaying the result
│   ├── static
│   │   └── styles.css        # CSS styles for the web application
│   ├── azure_uploader.py     # Azure Blob Storage uploader
│   ├── groq_client.py        # Groq API client for generating prompts
│   └── utils
│       └── __init__.py      # Initialization file for utility functions
├── requirements.txt          # Project dependencies
├── .env                      # Environment variables for sensitive information
└── README.md                 # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd style-prompt-webapp
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up your environment variables in the `.env` file:
   ```
   AZURE_CONNECTION_STRING=<your_azure_connection_string>
   AZURE_CONTAINER_NAME=<your_container_name>
   GROQ_API_KEY=<your_groq_api_key>
   ```

## Usage

1. Run the application:
   ```
   python src/app.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

3. Upload an image and receive a cinematic prompt for it.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.