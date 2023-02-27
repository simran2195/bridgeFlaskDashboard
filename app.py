from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def index():
    # Load data from CSV
    df = pd.read_csv('data.csv')
    
    # Generate plot
    plt.plot(df['x'], df['y'])
    plt.xlabel('X')
    plt.ylabel('Y')
    
    # Save plot to file
    plt.savefig('static/plot.png')
    
    # Render HTML template with plot
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
