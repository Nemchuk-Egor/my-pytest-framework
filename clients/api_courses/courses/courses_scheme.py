from pydantic import BaseModel, ConfigDict, Field

from clients.api_courses.files.files_scheme import FileScheme
from clients.api_courses.users.users_scheme import UserScheme


class CourseScheme(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    preview_file: FileScheme = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserScheme = Field(alias="createdByUser")


class UpdateCourseScheme(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")


class CreateCourseRequestScheme(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")


class CreateCourseResponseScheme(BaseModel):
    course: CourseScheme


class GetCoursesResponseScheme(BaseModel):
    courses: list[CourseScheme]


class GetCourseResponseScheme(BaseModel):
    course: CourseScheme
