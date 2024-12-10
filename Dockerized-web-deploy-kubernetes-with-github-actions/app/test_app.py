import unittest
from app import app

class AppTestCase(unittest.TestCase):
    # El cliente de prueba de Flask
    def setUp(self):
        self.app = app.test_client()

    # Test para la ruta /api/data
    def test_get_data(self):
        response = self.app.get('/api/data')  # Realiza una solicitud GET.
        json_data = response.get_json()  # Obtén los datos JSON de la respuesta
        self.assertEqual(response.status_code, 200)  # Verifica que el código de estado sea 200.
        self.assertEqual(json_data['message'], 'Hello from Python!')  # Verifica el mensaje

if __name__ == '__main__':
    unittest.main()
