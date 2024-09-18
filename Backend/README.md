# 📚 Installation Instructions

To get started with the Ecommerce Project Backend, follow these steps:

1. Navigate to the project directory:
    ```sh
    cd Backend
    ```

2. Create a virtual environment (optional but recommended):
    ```sh
    python -m venv env
    ```

3. Activate the virtual environment:
    For Windows:
    ```sh
    .\env\Scripts\activate
    ```
    For Unix or MacOS:
    ```sh
    source env/bin/activate
    ```

4. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

5. Set up the environment variables:
    - Create a `.env` file in the root directory.
    - Copy the contents of `.env.example` into `.env`.
    - Update the values of the environment variables in `.env` as per your configuration.

6. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

7. Start the server:
    ```sh
    python manage.py runserver
    ```

8. The backend server should now be running on `http://localhost:8000`.

9. You can test the API endpoints using tools like Postman or cURL.

That's it! You have successfully installed and set up the Ecommerce Project Backend. Happy coding!