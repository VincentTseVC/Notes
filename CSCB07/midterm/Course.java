package midterm;

import java.util.ArrayList;
import java.util.List;

public class Course {
  String code;
  
  Professor professor;
  
  List<Student> students;
  
  Eligible eligible;
  
  public Course(String code, Professor professor, Eligible eligible) {
    this.code = code;
    this.professor = professor;
    students = new ArrayList<Student>();
    this.eligible = eligible;
    Administration.getInstance().addCourse(this);
  }
  
  public boolean isEligible(Student student) {
    // return student.passedCSCA48 && (student.cgpa >= 3.5 || student.inCSPOSt) && !student.passedCSC207;
    return eligible.isEligible(student);
  }
  
  @Override
  public boolean equals(Object obj) {
    if (obj == null)
      return false;
    if (getClass() != obj.getClass())
      return false;
    Course other = (Course) obj;
    return this.code.equals(other.code);
  }
  
  @Override
  public int hashCode() {
    return code.hashCode(); //  可以改
  }
  
  
  public void addStudent(Student student) {
    if (isEligible(student) && !students.contains(student))
      students.add(student);
  }
  
  public void displayInfo() {
    System.out.println(code);
    System.out.println(professor);
    students.sort(null);
    for (Student student : students)
      System.out.println(student);
  }
}
