from pydantic import BaseModel


class BaseGradeStats(BaseModel):
    student_id: int | None = None
    teacher_id: int | None = None
    group_id: int | None = None