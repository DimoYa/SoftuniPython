class SeniorStudent:
    def __init__(self, student_id: str, name: str, student_gpa: float):
        self.student_id = student_id
        self.name = name
        self.student_gpa = student_gpa
        self.colleges = set()

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, value):
        if len(value.strip()) < 4:
            raise ValueError("Student ID must be at least 4 digits long!")
        self.__student_id = value.strip()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Student name cannot be null or empty!")
        self.__name = value

    @property
    def student_gpa(self):
        return self.__student_gpa

    @student_gpa.setter
    def student_gpa(self, value):
        if value <= 1.0:
            raise ValueError("Student GPA must be more than 1.0!")
        self.__student_gpa = value

    def apply_to_college(self, gpa_required: float, college_name: str):
        if gpa_required > self.student_gpa:
            return 'Application failed!'
        self.colleges.add(college_name.upper())
        return f'{self.name} successfully applied to {college_name}.'

    def update_gpa(self, new_gpa: float):
        if new_gpa <= 1.0:
            return 'The GPA has not been changed!'
        self.student_gpa = new_gpa
        return 'Student GPA was successfully updated.'

    def __eq__(self, other):
        return self.student_gpa == other.student_gpa



