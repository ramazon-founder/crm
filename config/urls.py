from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from django.conf import settings
from django.conf.urls.static import static

from users.views import UserViewSet, AuditLogViewSet
from students.views import StudentViewSet
from subjects.views import SubjectViewSet
from teachers.views import TeacherViewSet
from groups.views import GroupViewSet
from grades.views import GradeViewSet
from payments.views import PaymentViewSet
from attendance.views import AttendanceViewSet, HolidayViewSet, WorkdaysView

# Router
router = DefaultRouter()
router.register("users",    UserViewSet,    basename="user")
router.register("students", StudentViewSet, basename="student")
router.register("subjects", SubjectViewSet, basename="subject")
router.register("teachers", TeacherViewSet, basename="teacher")
router.register("groups", GroupViewSet, basename="group")
router.register("grades", GradeViewSet, basename="grade")
router.register("payments", PaymentViewSet, basename="payment")
router.register("attendance", AttendanceViewSet, basename="attendance")
router.register("holidays", HolidayViewSet, basename="holiday")
router.register("audit-logs", AuditLogViewSet, basename="audit-log")

# ✅ TO'LIQ SWAGGER KONFIGURATSIYA
schema = get_schema_view(
    openapi.Info(
        title="CRM API",
        default_version="v1",
        description="""
# 🚀 CRM System REST API Documentation

## 🔐 Authentication
All protected endpoints require token authentication:


Authorization: Token <your_token_here>


---

## 📌 API Modules

### 👤 Users
- User registration
- Login / authentication
- Profile management

### 🎓 Students
- CRUD operations for students
- Student profile management

### 👨‍🏫 Teachers
- CRUD operations for teachers
- Teacher profile management

### 📚 Subjects
- Create, update, delete subjects
- Subject management system

### 🏫 Groups
- Group creation and management
- Student grouping system

### 🏅 Grades
- Student grading system
- Performance tracking

### 💳 Payments
- Payment records management
- Financial tracking

### 📅 Attendance
- Attendance tracking
- Daily presence records

### 🎉 Holidays
- Holiday calendar management
- Non-working days setup

### 📊 Audit Logs
- System activity tracking
- User action history

---

## ⚙️ Base URL

https://crmuz.up.railway.app


---

## 📡 Additional Endpoint
- `/api/workdays/` → Workdays configuration endpoint

---

## 📖 API Docs
- Swagger UI: `/swagger/`
- ReDoc: `/redoc/`
- JSON Schema: `/swagger.json`

---

## ⚡ Notes
- All endpoints are RESTful
- Use proper HTTP methods (GET, POST, PUT, DELETE)
- Always send JSON payloads for requests
""",
    ),
    public=True,
    permission_classes=[AllowAny],
    authentication_classes=[],
    url='https://crmuz.up.railway.app',
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("swagger/", schema.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/",   schema.with_ui("redoc",   cache_timeout=0), name="schema-redoc"),
    path("api/workdays/", WorkdaysView.as_view(), name="workdays"),
    path("swagger.json", schema.without_ui(cache_timeout=0), name="schema-json"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)