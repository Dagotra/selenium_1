from pydantic import Field

from services.univesity.models.base_grade import MIN_GRADE, MAX_GRADE
from services.univesity.models.base_grade_stats import BaseGradeStats


class GradeStatsResponse(BaseGradeStats):
    count: int = Field(ge=MIN_GRADE)
    min: int | None = Field(..., ge=MIN_GRADE, le=MAX_GRADE)
    max: int | None = Field(..., ge=MIN_GRADE, le=MAX_GRADE)
    avg: float | None = Field(..., ge=MIN_GRADE, le=MAX_GRADE)
