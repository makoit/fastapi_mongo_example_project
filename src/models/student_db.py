from .student import StudentModel

# extend workshop model with id for MongoDB ObjectId field
# id in mongo: _id
class StudentOnDbModel(StudentModel):
    """[summary]
    Student model used at DB level.

    [description]
    Used to abstract student model at DB level.
    """
    id: str