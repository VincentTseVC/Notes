package midterm;

import java.util.LinkedHashSet;

public class Administration {
  
  private static Administration instance;
  
  private LinkedHashSet<Professor> professors;
  
  private LinkedHashSet<Student> students;
  
  private LinkedHashSet<Course> courses;
  
 
  private Administration() {
  }
  
  public static Administration getInstance() {
    if (instance == null)
      instance = new Administration();
    return instance;
  }
  
  public void addProfessor(Professor professor) {
    professors.add(professor);
  }
  
  public void addStudent(Student student) {
    students.add(student);
  }
  
  public void addCourse(Course course) {
    courses.add(course);
  }
  
}

