## Overview
A REST api to be consumed by a mobile app, which is somewhat similar to various popular apps which tell you if a number is spam, or allow you to find a person’s name by searching for their phone number.
This Django REST API project provides APIs for user management, contact operations, and spam-related functionality with help of mysql & django rest framework.

## API Endpoints

### Users
#### Register a new user
- `POST /api/auth/users/`
  - Create a new user account.

#### See all the users
- `GET /api/auth/users/`

#### Edit the user information
- `PUT /api/auth/users/id`

#### Login and Obtain Access Token
- `POST /api/token/`
  - Obtain an access token by providing a valid username and password.

#### Refresh Access Token
- `POST /api/token/refresh/`
  - Refresh an expired access token.

#### Token generated with help of JWT authentication for disallowing unauthorised users to access the data.Include the token in authentication header of every request to access contacts, to mark number as spam, get contacts by name, get contacts by number

### Contacts

#### Add a new contact
- `POST /contacts/`
  - Add a new contact.

#### Get contacts by name
- `GET /get_contacts_name/?name=Aditi`
  - Retrieve contacts based on the name if it is registered user than returns email id otherwise checks for name startswith & contains condition in contacts

#### Get contacts by phone number
- `GET /get_contacts_phone/?phone=8856930560`
- Retrieve contacts based on the phone number if it is registered user than returns email id otherwise checks for name startswith & contains condition in contacts

#### Edit the contacts information
- `PUT /contacts/id`


### Spam

#### Mark a phone number as spam
- `POST /spam/mark_number_as_spam/`
- Mark a phone number as spam, updating spam likelihood for users and contacts.

## Usage

1. Clone the repository: `git clone <repository_url>`
2. Apply migrations: `python manage.py migrate`
3. Run the development server: `python manage.py runserver`


