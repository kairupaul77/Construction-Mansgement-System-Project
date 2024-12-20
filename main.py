import sqlite3
import cmd
import re


def init_db():
    conn = sqlite3.connect('construction_management.db')
    c = conn.cursor()

    # Create Workers table
    c.execute('''CREATE TABLE IF NOT EXISTS workers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    job_title TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE)''')

    # Create Clients table
    c.execute('''CREATE TABLE IF NOT EXISTS clients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    contact_info TEXT)''')

    # Create Projects table
    c.execute('''CREATE TABLE IF NOT EXISTS projects (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    project_name TEXT NOT NULL,
                    description TEXT,
                    worker_id INTEGER,
                    client_id INTEGER,
                    FOREIGN KEY (worker_id) REFERENCES workers(id),
                    FOREIGN KEY (client_id) REFERENCES clients(id))''')

    conn.commit()
    conn.close()


init_db()


def add_worker(name, job_title, email):
    conn = sqlite3.connect('construction_management.db')
    c = conn.cursor()
    c.execute("INSERT INTO workers (name, job_title, email) VALUES (?, ?, ?)", (name, job_title, email))
    conn.commit()
    conn.close()


def view_workers():
    conn = sqlite3.connect('construction_management.db')
    c = conn.cursor()
    c.execute("SELECT * FROM workers")
    workers = c.fetchall()
    conn.close()
    return workers


def update_worker(worker_id, name, job_title, email):
    conn = sqlite3.connect('construction_management.db')
    c = conn.cursor()
    c.execute("UPDATE workers SET name=?, job_title=?, email=? WHERE id=?", (name, job_title, email, worker_id))
    conn.commit()
    conn.close()


def delete_worker(worker_id):
    conn = sqlite3.connect('construction_management.db')
    c = conn.cursor()
    c.execute("DELETE FROM workers WHERE id=?", (worker_id,))
    conn.commit()
    conn.close()


def add_client(name, email, contact_info):
    conn = sqlite3.connect('construction_management.db')
    c = conn.cursor()
    c.execute("INSERT INTO clients (name, email, contact_info) VALUES (?, ?, ?)", (name, email, contact_info))
    conn.commit()
    conn.close()


def view_clients():
    conn = sqlite3.connect('construction_management.db')
    c = conn.cursor()
    c.execute("SELECT * FROM clients")
    clients = c.fetchall()
    conn.close()
    return clients


def update_client(client_id, name, email, contact_info):
    conn = sqlite3.connect('construction_management.db')
    c = conn.cursor()
    c.execute("UPDATE clients SET name=?, email=?, contact_info=? WHERE id=?", (name, email, contact_info, client_id))
    conn.commit()
    conn.close()


def delete_client(client_id):
    conn = sqlite3.connect('construction_management.db')
    c = conn.cursor()
    c.execute("DELETE FROM clients WHERE id=?", (client_id,))
    conn.commit()
    conn.close()


def add_project(project_name, description, worker_id, client_id):
    conn = sqlite3.connect('construction_management.db')
    c = conn.cursor()
    c.execute("INSERT INTO projects (project_name, description, worker_id, client_id) VALUES (?, ?, ?, ?)", 
              (project_name, description, worker_id, client_id))
    conn.commit()
    conn.close()


def view_projects():
    conn = sqlite3.connect('construction_management.db')
    c = conn.cursor()
    c.execute('''SELECT projects.id, project_name, description, workers.name, clients.name
                 FROM projects
                 JOIN workers ON projects.worker_id = workers.id
                 JOIN clients ON projects.client_id = clients.id''')
    projects = c.fetchall()
    conn.close()
    return projects


def update_project(project_id, project_name, description, worker_id, client_id):
    conn = sqlite3.connect('construction_management.db')
    c = conn.cursor()
    c.execute('''UPDATE projects 
                 SET project_name=?, description=?, worker_id=?, client_id=? 
                 WHERE id=?''', 
              (project_name, description, worker_id, client_id, project_id))
    conn.commit()
    conn.close()


def delete_project(project_id):
    conn = sqlite3.connect('construction_management.db')
    c = conn.cursor()
    c.execute("DELETE FROM projects WHERE id=?", (project_id,))
    conn.commit()
    conn.close()


class ConstructionManagementCLI(cmd.Cmd):
    intro = "Welcome to the Construction Management System. Type help or ? to list commands."
    prompt = "(CMS) "

    def do_add_worker(self, arg):
        'Add a new worker: add_worker name job_title email'
        args = arg.split()
        add_worker(args[0], args[1], args[2])
        print("Worker added successfully.")

    def do_view_workers(self, arg):
        'View all workers'
        workers = view_workers()
        for worker in workers:
            print(worker)

    def do_update_worker(self, arg):
        'Update a worker details: update_worker worker_id name job_title email'
        args = arg.split()
        update_worker(int(args[0]), args[1], args[2], args[3])
        print("Worker updated successfully.")

    def do_delete_worker(self, arg):
        'Delete a worker: delete_worker worker_id'
        delete_worker(int(arg))
        print("Worker deleted successfully.")

    def do_add_client(self, arg):
        'Add a new client: add_client name email contact_info'
        args = arg.split()
        add_client(args[0], args[1], args[2])
        print("Client added successfully.")

    def do_view_clients(self, arg):
        'View all clients'
        clients = view_clients()
        for client in clients:
            print(client)

    def do_update_client(self, arg):
        'Update client details: update_client client_id name email contact_info'
        args = arg.split()
        update_client(int(args[0]), args[1], args[2], args[3])
        print("Client updated successfully.")

    def do_delete_client(self, arg):
        'Delete a client: delete_client client_id'
        delete_client(int(arg))
        print("Client deleted successfully.")

    def do_add_project(self, arg):
        'Add a new project: add_project "project_name" "description" worker_id client_id'

        # Use regular expression to extract quoted project name, description and numeric IDs
        pattern = r'"([^"]+)"\s+"([^"]+)"\s+(\d+)\s+(\d+)'
        match = re.match(pattern, arg.strip())

        if match:
            project_name = match.group(1)
            description = match.group(2)
            worker_id = int(match.group(3))
            client_id = int(match.group(4))

            add_project(project_name, description, worker_id, client_id)
            print("Project added successfully.")
        else:
            print("Error: Incorrect format. Please use the format: add_project \"name\" \"description\" worker_id client_id")

    def do_view_projects(self, arg):
        'View all projects'
        projects = view_projects()
        for project in projects:
            print(project)

    def do_update_project(self, arg):
        'Update project details: update_project project_id project_name description worker_id client_id'
        args = arg.split()
        update_project(int(args[0]), args[1], args[2], int(args[3]), int(args[4]))
        print("Project updated successfully.")

    def do_delete_project(self, arg):
        'Delete a project: delete_project project_id'
        delete_project(int(arg))
        print("Project deleted successfully.")

    def do_exit(self, arg):
        'Exit the system'
        print("Exiting Construction Management System.")
        return True


if __name__ == '__main__':
    init_db()  # Initialize the database
    ConstructionManagementCLI().cmdloop()  # Start the CLI
