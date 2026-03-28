import unittest
from src.dependency_injection import PlatformManager, MessageService

class MockService(MessageService):
    """Dependencia Mockeada para pruebas sin efectos reales."""
    def __init__(self):
        self.sent_count = 0

    def send(self, message: str):
        self.sent_count += 1

class TestDI(unittest.TestCase):
    def test_injection_works(self):
        mock = MockService()
        system = PlatformManager(mock)
        system.notify_user("TestUser", "Prueba de Inyección")
        
        # Verifica que la dependencia fue llamada correctamente
        self.assertEqual(mock.sent_count, 1)

if __name__ == "__main__":
    unittest.main()