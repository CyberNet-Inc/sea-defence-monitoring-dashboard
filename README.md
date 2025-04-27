# Sea Defence Monitoring Dashboard

The Sea Defence Monitoring Dashboard is a Flask-based web application that monitors the progress and environmental impacts of coastal protection projects. This application helps project managers track ongoing sea defenses, visualize progress, and understand the environmental effects of these projects.

## Features

- **Project Management:** Add, list, and manage coastal protection projects.
- **Data Visualization:** Simple bar chart visualization using Plotly to display project data.
- **Dynamic Forms:** Add new projects through simple web forms.

## Technologies

- **Backend Framework:** Flask
- **Database:** SQLite via SQLAlchemy
- **Frontend:** HTML/CSS with Jinja2 templates
- **Data Visualization:** Plotly

## Installation

To set up and run the application locally:

1. **Clone this repository:**

   ```bash
   git clone <repository-url>
   cd sea-defence-monitoring-dashboard
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install requirements:**

   Install required packages from `requirements.txt` (make sure you have Flask, SQLAlchemy, Plotly, etc.).

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**

   ```bash
   python app.py
   ```

5. **Navigate to the application in your browser:**

   Visit `http://127.0.0.1:5000/` in your web browser to view the dashboard.

## Usage

- **Homepage:** View a list of all projects with their start dates.
- **Add Projects:** Enter project details on `/add_project` form to add new project entries.
- **Visualizations:** Visualize project data with simple embedded charts.

## Dependencies

- **Flask:** `>= 2.0.1`
- **SQLAlchemy:** `>= 1.4.20`
- **Plotly:** `>= 5.3.1`

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any proposed changes.

---

This README provides the necessary information for setting up and running the Sea Defence Monitoring Dashboard.