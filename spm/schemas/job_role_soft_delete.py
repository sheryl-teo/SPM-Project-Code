from pydantic import BaseModel


class Job_role_soft_delete(BaseModel):
    Job_Role_ID: str
    soft_delete: bool
