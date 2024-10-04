# Role Based Access Control System

## Overview
This project is a **Role-Based Access Control (RBAC) management system**, designed to provide flexible access management for users, roles, and permissions. It offers an intuitive interface that allows users to access assigned functions while enabling administrators to manage various access levels based on predefined roles.


## Features
- ***User Management***&nbsp;&nbsp;-&nbsp;&nbsp;Admins can create, update, and manage users and their roles within the system
- ***Role Management***&nbsp;&nbsp;-&nbsp;&nbsp;Define the role with specific permissions, controlling which menu each role can access
- ***Menu Management***&nbsp;&nbsp;-&nbsp;&nbsp;Customize system menus based on simulating development needs of business management


## Tech Stack
### Backend&nbsp;&nbsp;|&nbsp;&nbsp;RBAC-system
- Built with Django and MySQL, supporting the RBAC logic and API endpoints
- Developed RESTful APIs with Django REST Framework
- Implemented authentication using JSON Web Tokens (JWT)
- Optimized captcha processing time by integrating Redis
### Frontend&nbsp;&nbsp;|&nbsp;&nbsp;rbac_vue3_admin
- Use Axios to send HTTP request to the server for APIs
- Built with Vue.js and element-plus


## Demo
[Full Demo Video](https://youtu.be/_qI658-zzIM)

![demo-login](https://github.com/user-attachments/assets/ee220b68-0668-4d5b-8423-f74b4ed07c6b)
##  Main features Demo
### User Management
![demo1-user-mgt](https://github.com/user-attachments/assets/72df3300-3858-432b-ba48-8c20e0e5b78c)
### Role Management
![demo2-role-mgt](https://github.com/user-attachments/assets/399a16b4-a7a7-41c1-a184-ae6ab5ae68c8)
### Menu Management
![demo3-menu-mgt](https://github.com/user-attachments/assets/c3722b3b-55a2-4564-9bd0-7f37923788b9)
Only admins have access to the above.
### Custom Role-Based Access
![demo4-RoleBasedAccess](https://github.com/user-attachments/assets/6d80360b-84c8-4c13-83c4-eea691954c68)
### Account Center
![demo5-AccountCenter](https://github.com/user-attachments/assets/dd4af671-09c4-4d3c-87c8-d49eb3bbe42f)


## Getting Started
### Redis
```bash
sudo service redis-server start
```
### Backend&nbsp;&nbsp;|&nbsp;&nbsp;RBAC-system
#### Installation
Install dependencies with `pip install -r requirements.txt`
#### Run
```bash
python manage.py runserver
```
### Frontend&nbsp;&nbsp;|&nbsp;&nbsp;rbac_vue3_admin
```bash
npm run serve
```
Then, you can start with http://localhost:8080/#/login/
### Data
You can execute SQL files in `./testdata` to get the test data.
