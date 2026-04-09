
class EventManager:
    """Clase Broker que gestiona suscripciones y notificaciones dinámicas[cite: 19]."""
    def __init__(self):
        self._subscribers = {}

    def subscribe(self, event_type, subscriber):
        """Permite suscribirse dinámicamente a eventos."""
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(subscriber)
        print(f"[*] {subscriber.name} suscrito a '{event_type}'.")

## Requisito 2.2: Desuscripción dinámica
    def unsubscribe(self, event_type, subscriber):
        """Permite desuscribirse dinámicamente de eventos."""
        if event_type in self._subscribers and subscriber in self._subscribers[event_type]:
            self._subscribers[event_type].remove(subscriber)
            print(f"[*] {subscriber.name} removido de '{event_type}'.")

    def notify(self, event_type, data):
        """Envía datos a todos los suscriptores activos."""
        if event_type in self._subscribers:
            for subscriber in self._subscribers[event_type]:
                subscriber.update(data)

class Subscriber:
    """Representa a los consumidores de eventos."""
    def __init__(self, name):
        self.name = name

    def update(self, data):
        print(f"[{self.name}] Notificación recibida: {data}")

class Publisher:
    """Representa a los emisores de eventos."""
    def __init__(self, name, event_manager):
        self.name = name
        self.event_manager = event_manager

    def publish(self, event_type, data):
        print(f"\n-> {self.name} publicando en '{event_type}': {data}")
        self.event_manager.notify(event_type, data)

if __name__ == "__main__":
    broker = EventManager()
    
    # Requisito 2.1: Al menos dos publishers y dos subscribers [cite: 17, 18]
    pub1 = Publisher("Tutor_Academico", broker)
    pub2 = Publisher("Admin_Sistema", broker)
    
    sub1 = Subscriber("Estudiante_Andres")
    sub2 = Subscriber("Estudiante_Lucia")

    # Requisito 2.2: Suscripción dinámica [cite: 19]
    broker.subscribe("clases", sub1)
    broker.subscribe("clases", sub2)
    broker.subscribe("alertas", sub1)

    pub1.publish("clases", "Nueva monitoría de Cálculo disponible.")
    
    # Desuscripción dinámica [cite: 19]
    broker.unsubscribe("clases", sub2)
    pub1.publish("clases", "La monitoría cambió de salón.")