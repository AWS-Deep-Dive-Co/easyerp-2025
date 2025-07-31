# EasyTicket - IT Service Management System

EasyTicket is a simplified IT service management system designed for training and demonstration purposes in AWS IT auditing scenarios.

## Features

- **Dynamic Ticket Types**: Configurable ticket categories (Change Requests, Access Requests, Incidents, etc.)
- **Simple Authentication**: Django users have admin access, anonymous users have read-only access
- **Approval Workflow**: Support for multiple approvers on change requests
- **Search & Filter**: Comprehensive ticket search and filtering capabilities
- **Bulk Operations**: Import/export tickets and bulk manage ticket types
- **Responsive Design**: Modern Bootstrap-based interface

## Quick Start

### Using Docker Compose (Recommended)

1. Clone and navigate to the easyticket directory:
   ```bash
   cd easyticket
   ```

2. Build and start the application:
   ```bash
   docker-compose up -d
   ```

3. Access the application:
   - **Main Application**: http://localhost:8080/
   - **Admin Panel**: http://localhost:8080/admin/
   - **Default Admin Login**: admin / password

### Manual Setup

1. Create virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations and setup:
   ```bash
   python manage.py migrate
   python manage.py collectstatic
   ./createsuperuser
   ```

4. Start development server:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

## Usage

### Public Access (Read-Only)
- Browse all tickets at `/tickets/`
- View detailed ticket information
- Search and filter tickets by type, status, priority
- View approval status and comments

### Admin Access (Full Access)
- Login at `/admin/` or use the "Admin Login" link
- Create, edit, and delete tickets
- Manage ticket types in bulk
- Add comments and update approval status
- Import/export tickets via CSV

### Bulk Management

#### Ticket Types
- Navigate to Admin → Tickets → Ticket Types
- Click "Bulk Manage" to add multiple types at once
- Format: "Type Name | Description" (one per line)

#### Ticket Import/Export
- Navigate to Admin → Tickets → Tickets
- Use "Export" to download all tickets as CSV
- Use "Import" to bulk upload tickets from CSV

## Default Ticket Types

The system comes with these predefined ticket types:
- **Standard Change Request**: Regular changes with standard approval
- **Emergency Change Request**: Urgent changes requiring expedited approval
- **Access Request**: User access and permissions requests
- **Incident Report**: IT security and operational incidents

## API Endpoints

- `/` - Dashboard with statistics
- `/tickets/` - Ticket list with search
- `/tickets/{ticket_number}/` - Ticket detail view
- `/tickets/create/` - Create new ticket (admin only)
- `/admin/` - Django admin interface

## Training Scenarios

This system is designed to support AWS IT auditing training with realistic examples of:

- **Change Management**: Standard vs emergency changes with approval workflows
- **Access Control**: User access requests with business justification
- **Incident Response**: Security and operational incident tracking
- **Audit Trails**: Proper documentation and approval processes
- **Risk Assessment**: Technical details and risk mitigation documentation

## Data Persistence

- **Database**: SQLite stored in Docker volume `ticket_data`
- **Static Files**: Served from Docker volume `static_files`
- **File Uploads**: Ticket attachments stored in database volume

## Configuration

Environment variables:
- `SECRET_KEY`: Django secret key (change in production)
- `DEBUG`: Enable debug mode (set to False in production)

## Development

To extend the system:

1. Models are in `tickets/models.py`
2. Views are in `tickets/views.py`
3. Templates are in `templates/tickets/`
4. Admin customization in `tickets/admin.py`

## Security Notes

This system is designed for training environments:
- Uses SQLite (not suitable for production)
- Default admin credentials (change immediately)
- Debug mode enabled by default
- No advanced security features

For production use, implement proper security measures including:
- Strong authentication and authorization
- Encrypted database connections
- Secure secret key management
- HTTPS enforcement
- Rate limiting and monitoring

## Support

This is a training tool created for AWS IT auditing courses. For questions or issues, refer to your training materials or instructor.
