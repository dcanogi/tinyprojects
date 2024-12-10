import unittest
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permitir solicitudes desde dominios cruzados (CORS).

# Endpoint para obtener datos
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'message': 'Hello from Python!'})

# Test Unitario
class TestData(unittest.TestCase):
    def test_message(self):
        response = app.test_client().get('/api/data')
        json_data = response.get_json()
        self.assertEqual(json_data['message'], 'Hello from Python!')

# Endpoint para ejecutar los tests
@app.route('/api/test', methods=['GET'])
def run_tests():
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestData)
    result = unittest.TextTestRunner().run(test_suite)
    
    test_results = {
        'success': result.wasSuccessful(),
        'failures': str(result.failures),
        'errors': str(result.errors)
    }
    
    # Asegurándonos de que la respuesta sea en JSON
    return jsonify(test_results)

if __name__ == '__main__':
    app.run(debug=True)
