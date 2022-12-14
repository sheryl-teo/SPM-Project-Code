from fastapi import FastAPI
from routes.course import course
from routes.skill import skill
from routes.job_role import job_role
from routes.job_role_skill import job_role_skill
# from routes.course_soft_delete import course_soft_delete
# from routes.skill_course import skill_course
from fastapi.middleware.cors import CORSMiddleware
from routes.learning_journey import learning_journey
from routes.staff import staff
from routes.role import role

app = FastAPI(
    debug = True,
    title="Users API",
    description="a REST API using python and mysql",
)

app.include_router(course)
app.include_router(skill)
app.include_router(job_role)

app.add_middleware(
    CORSMiddleware,
    allow_origins= ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    
)


# app.include_router(job_role_skill)
app.include_router(learning_journey)
app.include_router(role)
app.include_router(job_role_skill)
# app.include_router(course_soft_delete)
# app.include_router(skill_course)
app.include_router(staff)


