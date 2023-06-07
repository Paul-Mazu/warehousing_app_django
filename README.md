# <center>warehousing_app_django</center>
## <center> _[Link to the deployed project.](http://warehouse.us-east-1.elasticbeanstalk.com/)_ </center>
<hr>

<div align="center">

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/Paul-Mazu/warehousing_app_django?color=1d7147&style=for-the-badge)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/Paul-Mazu/warehousing_app_django?color=EAE6B4&style=for-the-badge) ![GitHub milestones](https://img.shields.io/github/milestones/all/Paul-Mazu/warehousing_app_django?color=F2F2F2&style=for-the-badge) ![GitHub language count](https://img.shields.io/github/languages/count/Paul-Mazu/warehousing_app_django?color=62B096&style=for-the-badge)
</div>

<div align="center">
  <a href="#About">About</a>  |
  <a href="#Key Features">Key Features</a>  |
  <a href="#Prototype">Prototype</a>  |
  <a href="#Setup">Setup</a>  |
  <a href="#API documentation">API documentation</a>  |
  <a href="#Technologies Used">Technologies Used</a>  |
  <a href="#Authors">Authors</a>
</div>

<br>

# About

Welcome to our Warehouse Management System (WMS) functional prototype! This custom, dynamic web application is designed to efficiently store and manage information in a secure database. With a robust user system, registered users can easily interact with the database contents using web forms, enabling them to make persistent changes to the website's content. Experience a seamless and intuitive interface that empowers users to streamline their warehouse management processes.

<br>

## Key Features

* Database storage: Our web application securely stores all warehouse management information in a reliable database.
* User system: A comprehensive user system allows registered users to access and interact with the contents of the database.
* Web forms: Intuitive web forms enable users to input and modify data directly, ensuring easy and efficient interaction with the website's content.
* Persistent changes: Any modifications made through the web forms are stored persistently, ensuring that updates to the website's content are maintained over time.
* Streamlined interface: Enjoy a user-friendly and intuitive interface that simplifies navigation and enhances the overall user experience.


## Prototype

_Video/gif demonstration of the user flow._

_[Link to the deployed project.](http://warehouse.us-east-1.elasticbeanstalk.com/)_

## Setup


## API documentation
Base URL: http://example.com/api/stock/

### Item API Endpoints:

#### GET /list-items/
* Returns a list of all items in the warehouse.
* Permissions: Authenticated users only.

#### GET /list-items/{id}/
* Returns details of a specific item by its ID.
* Permissions: Authenticated users only.

#### PUT /list-items/{id}/
* Updates the details of a specific item by its ID.
* Permissions: Authenticated users only.

#### DELETE /list-items/{id}/
* Deletes a specific item by its ID.
* Permissions: Authenticated users only.

### Authentication:
* The API endpoints require authentication. Please include the authentication token in the request headers.

### Example Usage:
* Get a list of all items:  
``GET /api/list-items/``
* Response:  
```[  
  {  
      "id": 1,  
      "state": "State 1",  
      "category": "Category 1",  
      "date_of_stock": "2023-06-01T10:30:00Z",  
      "warehouse": 1  
  },  
  {
      "id": 2,
      "state": "State 2",
      "category": "Category 2",
      "date_of_stock": "2023-06-02T12:45:00Z",
      "warehouse": 2
  }
]
```
* Get details of a specific item:
``GET /api/list-items/1/``
* Response:
```
{
  "id": 1,
  "state": "State 1",
  "category": "Category 1",
  "date_of_stock": "2023-06-01T10:30:00Z",
  "warehouse": 1
}
```
* Update details of a specific item:  
``PUT /api/list-items/1/``  
* Request Body:  
```
{
  "state": "Updated State 1",
  "category": "Updated Category 1",
  "date_of_stock": "2023-06-01T15:00:00Z",
  "warehouse": 2
}

```


## Technologies Used
* Front-end: HTML, CSS, Bootstrap, JavaScript
* Back-end: Python Django, Django Rest Framework
* Database: PostgreSQL
* Authentication: JSON Web Tokens (JWT)

## Authors

* Pawel Mazurkiewicz:  
Tutor and Student Digital Career Institute  
[GitHub](https://github.com/Paul-Mazu)  
[LinkedIn](https://www.linkedin.com/in/pawel-mazurkiewicz-906877173/)





