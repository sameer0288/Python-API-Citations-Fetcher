# Python Gen-AI Developer Assignment

## Introduction
This project fetches data from a given API, processes it to identify sources for each response, and returns the citations. An optional Flask-based UI is provided to display the results.

## Setup
1. Clone the repository.
    ```sh
    git clone <repository_url>
    cd gen-ai-assignment
    ```
2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
- Run the script:
    ```sh
    python main.py
    ```
- To use the optional Flask UI:
    ```sh
    python app.py
    ```
    Navigate to `http://127.0.0.1:5000/` to view the results.

## Code Overview
- `main.py`: Contains the main logic for fetching data from the API and processing it to find citations.
- `app.py`: Optional Flask application to serve the citations through a web interface.
- `requirements.txt`: Lists the required Python packages.

## Notes
- Ensure you have given collaborator access to `Pankaj-Baranwal` on GitHub.
- Follow PEP-8 guidelines for coding standards.
