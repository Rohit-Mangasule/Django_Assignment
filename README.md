# Django Project

## Overview

This is a Django-based web application that includes user authentication features such as sign-up, login, password reset, and profile management. The project is designed to be a starting point for building more complex web applications.

## Features

- User Registration
- User Login
- Password Reset
- Profile Management
- Password Change

## Requirements

- Python 3.x
- Django 3.x or higher

## Setup

### Clone the Repository

```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject

## Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

##Install Dependencies
pip install -r requirements.txt


##Apply Migrations
python manage.py migrate

##Run the Development Server
Run the Development Server

## Usage

Access the Application
Open your web browser and go to http://127.0.0.1:8000/.

User Authentication
Sign Up: Create a new account.
Login: Log in with your credentials.
Profile: View and manage your profile.
Password Change: Change your password.
Password Reset: Reset your password via email.