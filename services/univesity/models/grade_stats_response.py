from pydantic import Field

from services.univesity.models.base_grade_stats import BaseGradeStats


class GradeStatsResponse(BaseGradeStats):
    count: int = Field(ge=0)
    min: int | None = Field(..., ge=0, le=5)
    max: int | None = Field(..., ge=0, le=5)
    avg: float | None = Field(..., ge=0, le=5)
