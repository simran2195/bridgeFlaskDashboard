from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def index():
    # Load data from CSV
    # df = pd.read_csv('data.csv')
    df = pd.read_csv('/Users/admin/Desktop/UW MSTI/Quarter 2/514/project/bridgeFlaskDashboard/data/mlt_20170619_083708_300.csv')
    data = df.loc[:, ['Timestamp', 'accelZ', 'Lat', 'Long']]
    # Begin by visualizing the z-axis acceleration:
    z_acc = data[["Timestamp", "accelZ"]]
    z_acc.plot(x = "Timestamp", y = "accelZ", kind = "line", figsize=(20, 8), xlabel = None)
    plt.show()
    
    # Generate plot
    plt.xlabel('X')
    plt.ylabel('Y')
    
    # Save plot to file
    plt.savefig('static/plot.png')
    
    # Render HTML template with plot
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
