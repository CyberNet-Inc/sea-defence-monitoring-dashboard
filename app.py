from flask import Flask, render_template, request, redirect, url_for
from models import db, Project
import os
import plotly.express as px
from flask import jsonify

app = Flask(__name__)

# Configure Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sea_defence.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)

@app.route('/add_project', methods=['GET', 'POST'])
def add_project():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        start_date = request.form['start_date'] # Simplifying date handling, should add parsing
        project = Project(name=name, description=description, start_date=start_date)
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_project.html')

@app.route('/visualize')
def visualize():
    projects = Project.query.with_entities(Project.name, Project.start_date).all()
    
    # Example visualization with Plotly
    fig = px.bar(
        x=[project.name for project in projects],
        y=list(range(1, len(projects) + 1)),
        title='Project Count Visualization',
        labels={'x': 'Projects', 'y': 'Total Projects Created'}
    )

    graph_json = jsonify(fig.to_json())
    return graph_json

if __name__ == '__main__':
    app.run(debug=True)
