# CV Generator - Django

## Overview

CV Generator is a Django web application that simplifies the process of creating and downloading professional CVs (resumes) in PDF format. This app provides a user-friendly interface for entering personal and professional information, allowing users to customize their CVs effortlessly.

## Features

- **User-Friendly Interface:** Navigate through the CV creation process with a clean and intuitive UI.
  
- **Customization Options:** Tailor your CV by adding personal details, education, work experience, skills, and more.

- **Download in PDF Format:** Generate a professional-looking CV and download it as a PDF document with a single click.

## How to Use

1. **Clone the Repository:**
   - Open your terminal or command prompt.
   - Navigate to the directory where you want to clone the repository.
     ```bash
     cd path/to/your/directory
     ```
   - Run the following command to clone the repository.
     ```bash
     git clone https://github.com/Rahulns21/cv-generator-django.git
     ```
   - Change into the cloned directory.
     ```bash
     cd cv-generator-django
     ```

2. **Set Up Virtual Environment:**
   - Create and activate a virtual environment.
     ```bash
     python -m venv env
     source env/bin/activate  # On Windows, use `env\Scripts\activate`
     ```

3. **Install Dependencies:**
   - Install the required packages using pip.
     ```bash
     pip install -r requirements.txt
     ```

4. **Database Migration:**
   - Apply migrations to set up the database.
     ```bash
     python manage.py migrate
     ```

5. **Run the Development Server:**
   - Start the Django development server.
     ```bash
     python manage.py runserver
     ```

6. **Access the Application:**
   - Open your web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to use the CV Generator.

7. **Generate and Download CV:**
   - Fill in the necessary details, customize your CV, and click the "Download PDF" button to get your professional CV in PDF format.

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
