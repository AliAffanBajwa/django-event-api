
# 📅 Event Manager API

A **Django REST Framework (DRF)** based API for managing events and categories. This API allows users to create, update, delete, and list events and categories efficiently.

## 🚀 Features
- 📂 CRUD operations for **Categories** & **Events**
- 📊 Event statistics with **Event Chart API**
- 🔒 Secure & Scalable with Django REST Framework (DRF)

## 📌 Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/AliAffanBajwa/django-event-api.git
   cd event_management_system
   ```

2. **Create & Activate a Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Development Server**
   ```sh
   python manage.py runserver
   ```

## 🛠 API Endpoints

### **Category Endpoints**
| Method | Endpoint | Description |
|--------|---------|-------------|
| `GET`  | `/api/categories/` | List all categories |
| `POST` | `/api/categories/` | Create a new category |
| `GET`  | `/api/categories/{category_id}/` | Get a category |
| `DELETE` | `/api/categories/{category_id}/` | Delete a category |

### **Event Endpoints**
| Method | Endpoint | Description |
|--------|---------|-------------|
| `GET`  | `/api/events/` | List all events |
| `POST` | `/api/events/` | Create a new event |
| `GET`  | `/api/events/{event_id}/` | Get an event |
| `PUT`  | `/api/events/{event_id}/` | Update an event |
| `DELETE` | `/api/events/{event_id}/` | Delete an event |

### **Event Chart**
| Method | Endpoint | Description |
|--------|---------|-------------|
| `GET`  | `/api/event-chart/` | Get pending event statistics |

## 🎯 Usage with Postman
1. Open **Postman** and set the URL to:
   ```
   http://127.0.0.1:8000/api/events/
   ```
2. Use `POST` with the following JSON body to create an event:
   ```json
   {
       "name": "Tech Conference 2025",
       "category": 1,
       "start_date": "2025-06-10T09:00:00Z",
       "end_date": "2025-06-12T18:00:00Z",
       "priority": 1,
       "description": "A major tech event.",
       "location": "New York",
       "organizer": "Tech Innovators"
   }
   ```

## 🏗️ Built With
- 🐍 **Django** - Python web framework
- 🔥 **Django REST Framework (DRF)** - API toolkit
- 🗃️ **SQLite/PostgreSQL** - Database
- ⚡ **Postman** - API testing
