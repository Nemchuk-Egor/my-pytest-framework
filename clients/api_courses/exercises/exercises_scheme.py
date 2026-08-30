from pydantic import BaseModel, ConfigDict, Field


class ExerciseScheme(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class CreateExerciseRequestScheme(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class CreateExerciseResponseScheme(BaseModel):
    exercise: ExerciseScheme


class GetExercisesResponseScheme(BaseModel):
    exercises: list[ExerciseScheme]


class GetExerciseResponseScheme(BaseModel):
    exercise: ExerciseScheme


class UpdateExerciseRequestScheme(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class UpdateExerciseResponseScheme(BaseModel):
    exercise: ExerciseScheme
