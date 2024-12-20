# Construction Management System

## Description
The **Construction Management System** is a Command-Line Interface (CLI) tool that allows project managers to manage workers, clients, and projects effectively. The system supports **CRUD (Create, Read, Update, Delete)** operations for workers, clients, and projects, and tracks the relationships between workers and projects, as well as clients and projects.

## Problem Statement
Managing construction workers, clients, and projects can become cumbersome with manual processes like spreadsheets or paper records. This system aims to:
- Eliminate data redundancy and errors.
- Simplify tracking of workers assigned to projects and clients.
- Provide scalability and quick information retrieval for growing businesses.

## Technologies Used
- **Python**: Programming language used to develop the system.
- **SQLite**: Database system used to store worker, client, and project data.
- **cmd (Python Module)**: Used for creating the command-line interface.
- **Git**: For version control of the project code.
- **GitHub**: For hosting the repository and managing collaboration.

## Installation

### Prerequisites
Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Steps to Install
1. **Clone the repository** to your local machine:
   ```bash
   git clone https://github.com/your-username/construction-management-system.git
   cd construction-management-system
Install dependencies (if any dependencies are required, like sqlite3 or other packages, you can list them here):

bash
Copy code
pip install -r requirements.txt
Run the program: To start the CLI system, run:

bash
Copy code
python construction_management.py
Usage
The system allows project managers to perform various tasks using simple commands.

Available Commands:
add_worker name job_title email: Adds a new worker.
view_workers: Displays a list of all workers.
update_worker worker_id name job_title email: Updates worker details.
delete_worker worker_id: Deletes a worker.
add_client name email contact_info: Adds a new client.
view_clients: Displays a list of all clients.
update_client client_id name email contact_info: Updates client details.
delete_client client_id: Deletes a client.
add_project "project_name" "description" worker_id client_id: Adds a new project.
view_projects: Displays a list of all projects with assigned workers and clients.
update_project project_id project_name description worker_id client_id: Updates project details.
delete_project project_id: Deletes a project.
Example:
To add a worker:

bash
Copy code
add_worker "John Doe" "Plumber" "john.doe@example.com"
To view all workers:

bash
Copy code
view_workers
Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m "Add new feature").
Push to the branch (git push origin feature-branch).
Open a pull request.