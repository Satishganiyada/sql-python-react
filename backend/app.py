from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password123',
    'database': 'my_database',
    'port': '3306'
}

# Route to get the value
@app.route('/get-value', methods=['GET'])
def get_value():
    try:
        # Connect to MySQL
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Execute query
        cursor.execute("SELECT name FROM single_value_table LIMIT 1")
        result = cursor.fetchone()  # fetch one row
        
        # Close connection
        cursor.close()
        conn.close()
        
        if result:
            return jsonify({'name': result[0]})
        else:
            return jsonify({'message': 'No value found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/say-hello', methods=['GET'])
def sayhello():
    return "hello from python"
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=5000)
