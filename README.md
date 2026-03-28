# Taller 2: Patrones de Diseño - Semana 7

## Descripción del Proyecto
[cite_start]Este repositorio contiene la implementación práctica de dos patrones de diseño arquitectónicos solicitados en el taller[cite: 9]:
1. [cite_start]**Publish-Subscribe**: Un sistema que permite la comunicación entre emisores (Publishers) y receptores (Subscribers) de forma desacoplada y dinámica.
2. [cite_start]**Inyección de Dependencia**: Implementación utilizando *Constructor Injection* para garantizar que las dependencias sean intercambiables y faciliten el testeo mediante Mocking.

## Estructura de Archivos
```text
Arquitectura/
├── src/
│   ├── publish_subscribe.py    # Código del Patrón Pub-Sub
│   └── dependency_injection.py # Código del Patrón DI
├── tests/
│   └── test_mocking.py         # Pruebas unitarias y Mocking
├── .gitignore                  # Archivos excluidos de Git
└── README.md                   # Documentación principal

## Diagramas de Arquitectura

### 1. Patrón Publish-Subscribe
```mermaid
graph TD
    A[Tutor_Academico] -->|Publica| B(EventManager)
    C[Admin_Sistema] -->|Publica| B
    B -->|Notifica| D[Estudiante_Andres]
    B -->|Notifica| E[Estudiante_Lucia]

classDiagram
    class MessageService {
        <<interface>>
        +send(message)
    }
    class EmailService {
        +send(message)
    }
    class SMSService {
        +send(message)
    }
    class PlatformManager {
        -MessageService service
        +notify_user(user, note)
    }
    MessageService <|-- EmailService
    MessageService <|-- SMSService
    PlatformManager --> MessageService : utiliza

Instrucciones de Ejecución 

1. Clonar el repositorio

git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)
cd Arquitectura

2. Ejecutar Patrón Publish-Subscribe 

Este script demuestra el registro de 2 suscriptores, la publicación de eventos por parte de 2 publishers y la desuscripción dinámica de un usuario.

python src/publish_subscribe.py

3. Ejecutar Patrón Inyección de Dependencia 

Muestra cómo se inyectan diferentes servicios (Email y SMS) en la lógica de la plataforma.

python src/dependency_injection.py

Pruebas y Mocking 

Para verificar que las dependencias pueden ser reemplazadas por objetos simulados (Mocks) para pruebas aisladas:

Ejemplo de Salida Esperada 

Al ejecutar las pruebas, debería obtener:


Ran 1 test in 0.001s
OK