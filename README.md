# 🛍️ Django-Vue E-commerce Project 🛍️

## 📖 Introduction

Welcome to the Django-Vue E-commerce Project repository! This project exemplifies a collaborative effort between specialized developers and a designer, demonstrating our expertise in building a seamless and efficient e-commerce application.

## 🎨 Frontend Development by Mugiwara

The frontend of this application is meticulously crafted by Mugiwara using Vue.js, a progressive JavaScript framework renowned for building dynamic user interfaces. The frontend encompasses all elements visible and interactive for the user, including the product catalog, shopping cart, and checkout process.

### Key Responsibilities

- **🔧 Component Development:** Crafting reusable Vue components to ensure a modular and maintainable codebase.
- **📊 State Management:** Utilizing Vuex for robust state management, ensuring a consistent and efficient user experience.
- **🔗 API Integration:** Making asynchronous API requests with axios to interact seamlessly with the backend services.
- **🎨 Styling:** Implementing responsive and visually appealing designs using CSS, ensuring a polished look across all devices.

## 🏗️ Backend Development by Jose

The backend of this application is robustly developed by Jose using Django and Django REST Framework (DRF), which are powerful frameworks for creating scalable and secure web APIs. The backend is responsible for all server-side logic, including user authentication, data validation, and database interactions.

### Key Responsibilities

- **🗄️ Model Creation:** Designing Django models to define the structure of the database and manage data effectively.
- **🔄 View and Serializer Implementation:** Developing views and serializers to handle the transformation of data between the database and the API endpoints.
- **🛣️ URL Routing:** Setting up precise URL routing to ensure smooth navigation and interaction within the application.
- **🌐 API Development:** Implementing comprehensive API endpoints that facilitate the frontend's requirements and ensure efficient data exchange.
- **🚀 Hosting and Git Structure:** Managing all aspects of hosting the application and structuring the Git repository for efficient collaboration and version control.

## 🎨 Design by Third-Party Designer

The visual design and user experience elements of the application are created by a dedicated third-party designer.

## 🤝 Collaboration for a Full-Stack Solution

By leveraging their expertise, Mugiwara, Jose, and the third-party designer collaboratively deliver a full-stack e-commerce application that is both highly functional and user-friendly. Their combined efforts ensure the seamless integration of frontend aesthetics with backend functionality, providing users with an optimal shopping experience.

## 📂 Repository Information

This repository demonstrates our ability to work together to create a sophisticated and user-centric e-commerce platform. Explore the code, check out the issues, and feel free to reach out with any questions or feedback. Your contributions and insights are always welcome!

## 📬 Get in Touch

- **Mugiwara (Frontend Developer):** [GitHub Profile](https://github.com/mugiwaraxdxd)
- **Jose (Backend Developer):** [GitHub Profile](https://github.com/Jose05Code)
- **Third-Party Designer:** The visual design and user experience elements of the application were created by an anonymous third-party designer.

Thank you for visiting our repository!

## 🚀 How to Run the Project

### Prerequisites

- Python 3.x
- Node.js and npm
- PostgreSQL (or any preferred database)

### Backend (Django) Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-repo/django-vue-ecommerce.git
    cd django-vue-ecommerce
    ```

2. **Set up a virtual environment:**
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install backend dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Configure the database:**
    - Update the `DATABASES` setting in `backend/settings.py` with your database credentials.

5. **Apply migrations:**
    ```sh
    python manage.py migrate
    ```

6. **Create a superuser:**
    ```sh
    python manage.py createsuperuser
    ```

7. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

### Frontend (Vue.js) Setup

1. **Navigate to the frontend directory:**
    ```sh
    cd frontend
    ```

2. **Install frontend dependencies:**
    ```sh
    npm install
    ```

3. **Run the development server:**
    ```sh
    npm run serve
    ```

### Access the Application

- The Django backend will be running at `http://localhost:8000`.
- The Vue.js frontend will be running at `http://localhost:8080`.

Open your browser and navigate to the appropriate URLs to explore the application.

## 📜 License

This project is licensed under the [GNU General Public License, version 3.0](LICENSE) - see the [LICENSE](LICENSE) file for details.
