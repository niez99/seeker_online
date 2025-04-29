from flask import Flask, render_template, request
import sqlite3
import requests
import datetime

app = Flask(__name__)

# Setup database
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS locations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT,
            city TEXT,
            region TEXT,
            country TEXT,
            latitude REAL,
            longitude REAL,
            source TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

def get_ip_location():
    try:
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        lat, lon = map(float, data['loc'].split(','))
        return {
            "ip": data['ip'],
            "city": data['city'],
            "region": data['region'],
            "country": data['country'],
            "latitude": lat,
            "longitude": lon
        }
    except:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    ip_location = get_ip_location()

    if request.method == "POST":
        latitude = request.form.get("latitude")
        longitude = request.form.get("longitude")
        source = request.form.get("source")

        if latitude and longitude:
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            c.execute('''
                INSERT INTO locations (ip, city, region, country, latitude, longitude, source, timestamp)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                ip_location['ip'] if ip_location else None,
                ip_location['city'] if ip_location else None,
                ip_location['region'] if ip_location else None,
                ip_location['country'] if ip_location else None,
                float(latitude),
                float(longitude),
                source,
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ))
            conn.commit()
            conn.close()

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM locations ORDER BY timestamp DESC')
    locations = c.fetchall()
    conn.close()

    return render_template("index.html", ip_location=ip_location, locations=locations)

@app.route("/delete_all", methods=["POST"])
def delete_all():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('DELETE FROM locations')
    conn.commit()
    conn.close()
    return ('', 204)

@app.route("/export_csv", methods=["GET"])
def export_csv():
    import csv
    from io import StringIO
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM locations ORDER BY timestamp DESC')
    rows = c.fetchall()
    conn.close()

    si = StringIO()
    cw = csv.writer(si)
    cw.writerow(['ID', 'IP', 'City', 'Region', 'Country', 'Latitude', 'Longitude', 'Source', 'Timestamp'])
    cw.writerows(rows)
    output = si.getvalue()

    from flask import Response
    return Response(
        output,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=location_history.csv"}
    )

@app.route("/link")
def link():
    return render_template("link.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
