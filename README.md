# Taller 7: Patrones de Diseño - Publish-Subscribe e Inyección de Dependencia

## Descripción del Proyecto
[cite_start]Este repositorio contiene la implementación práctica de dos patrones de arquitectura de software[cite: 4, 5]:
1. [cite_start]**Publish-Subscribe**: Un sistema de eventos dinámicos donde los publicadores y suscriptores no están acoplados directamente[cite: 13, 14, 15].
2. [cite_start]**Inyección de Dependencia**: Un sistema de notificaciones desacoplado usando *Constructor Injection*, permitiendo intercambiar servicios de envío de mensajes.

## Diagramas de Arquitectura

### Patrón Publish-Subscribe
```mermaid
graph TD
    P1[Publisher: Tutor] -->|Publica Evento| EM(EventManager / Broker)
    P2[Publisher: Sistema] -->|Publica Evento| EM
    EM -->|Notifica 'Tutorias'| S1[Subscriber: Estudiante 1]
    EM -->|Notifica 'Tutorias'| S2[Subscriber: Estudiante 2]
    EM -->|Notifica 'Mantenimiento'| S1

classDiagram
    class MessageService {
        <<interface>>
        +send(message: str)
    }
    class EmailService {
        +send(message: str)
    }
    class SMSService {
        +send(message: str)
    }
    class MockMessageService {
        +send(message: str)
    }
    class StudentOnboarding {
        -service: MessageService
        +welcome_student(name: str)
    }
    MessageService <|-- EmailService
    MessageService <|-- SMSService
    MessageService <|-- MockMessageService
    StudentOnboarding --> MessageService : Inyectado por Constructor