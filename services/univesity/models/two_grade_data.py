from services.univesity.models.grade_response import GradeResponse
from dataclasses import dataclass


@dataclass
class TwoGradeData:
    teacher_id_1: int
    teacher_id_2: int
    student_id: int
    grade_1: GradeResponse
    grade_2: GradeResponse