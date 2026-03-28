from abc import ABC, abstractmethod

class MessageService(ABC):
    """Interfaz para asegurar que las dependencias sean intercambiables."""
    @abstractmethod
    def send(self, message: str):
        pass

class EmailService(MessageService):
    """Implementación de servicio por correo electrónico."""
    def send(self, message: str):
        print(f"[EMAIL] Enviando: {message}")

class SMSService(MessageService):
    """Implementación de servicio por SMS."""
    def send(self, message: str):
        print(f"[SMS] Enviando: {message}")

class PlatformManager:
    """
    Clase que utiliza Constructor Injection.
    Recibe la dependencia a través del método __init__.
    """
    def __init__(self, service: MessageService):
        self.service = service

    def notify_user(self, user, note):
        text = f"Usuario {user}: {note}"
        self.service.send(text)

if __name__ == "__main__":
    # Las dependencias se pueden intercambiar fácilmente
    email = EmailService()
    sms = SMSService()

    # Inyección del servicio de Email
    app = PlatformManager(email)
    app.notify_user("User01", "Bienvenido a la plataforma.")

    # Inyección del servicio de SMS
    app.service = sms # Cambio dinámico (Setter-like)
    app.notify_user("User01", "Tu clave ha sido actualizada.")