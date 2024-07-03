# Truck and Driver API

This project provides RESTful API endpoints for managing Truck and Driver models using Django and Django REST Framework.

## Project Structure

The project includes the following main components:

- **Models**: Defines the Truck and Driver models with common timestamp fields.
- **Serializers**: Serializes the Truck and Driver models for API responses.
- **Viewsets**: Provides CRUD operations for Truck and Driver models.
- **URLs**: Defines the API endpoints.

## Setup Instructions

### Prerequisites

- Python 3.x
- Django 3.x
- Django REST Framework

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/ongraphpythondev/truck-driver-api.git
    cd truck-driver-api
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

5. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

## API Endpoints

The API provides the following endpoints:

- **Truck Endpoints**:
    - `GET /trucks/`: List all trucks.
    - `POST /trucks/`: Create a new truck.
    - `GET /trucks/{id}/`: Retrieve a truck by ID.
    - `PUT /trucks/{id}/`: Update a truck by ID.
    - `DELETE /trucks/{id}/`: Soft delete a truck by ID.

- **Driver Endpoints**:
    - `GET /drivers/`: List all drivers.
    - `POST /drivers/`: Create a new driver.
    - `GET /drivers/{id}/`: Retrieve a driver by ID.
    - `PUT /drivers/{id}/`: Update a driver by ID.
    - `DELETE /drivers/{id}/`: Soft delete a driver by ID.

