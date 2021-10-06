package week3;

import java.util.HashMap;
import java.util.Map;

// Is-A relationship
public class Student extends Person {
  
  private String student_number;
  
  private HashMap<Course, Grade> grades;
  
  public Student(String firstName, String lastName, String student_num) {
    super(firstName, lastName);
    student_number = student_num;
    grades = new HashMap<Course, Grade>();
    
  }

  public String getStudent_number() {
    return student_number;
  }

  public void setStudent_number(String student_number) {
    this.student_number = student_number;
  }
  
  @Override
  public String toString() {
    return super.toString() + " " + this.student_number;
  }
  
  public boolean enroll(Course course) {
    return course.enroll(this);
  }
  
  
  public void addGrade(Course course, double grade) {
    grades.put(course, new NumericGrade(grade));
  }
  
  public void addGrade(Course course, String grade) {
    grades.put(course, new LetterGrade(grade));
  }
  
  
  
  
  public Grade getGrade(Course course) {
    return grades.get(course);
  }
  
  
  public double cgpa() {
    
    double total = 0;
    double num = 0;
    for (Grade grade : grades.values()) { 
      total += grade.gpa();
      num += 1;
    }
    
    return total / num;
  }
  
}



















