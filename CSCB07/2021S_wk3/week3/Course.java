package week3;

import java.util.ArrayList;

public class Course {
  
  private String courseCode;
  private int capacity;
  
  
  // Aggregation (Has-A relationship) (contains)
  private Instructor instructor;
  
  private ArrayList<Student> students;
  
  
  public Course(String courseCode, int capacity) {
    
    this.courseCode = courseCode;
    this.capacity = capacity;
    this.students = new ArrayList<Student>();
  }


  public int getCapacity() {
    return capacity;
  }


  public void setCapacity(int capacity) {
    this.capacity = capacity;
  }


  public Instructor getInstructor() {
    return instructor;
  }


  public void setInstructor(Instructor instructor) {
    this.instructor = instructor;
  }


  public String getCourseCode() {
    return courseCode;
  }
  
  public boolean enroll(Student student) {
    if (students.size() == capacity) return false;
    this.students.add(student);
    return true;
  }
  
  @Override
  public String toString() {
    String res = courseCode + " " + capacity;
    
    res += "\nInstructor:\n  " + instructor; 
    
    res += "\nStudents:";
    for (Student student : students) 
      res += "\n  " + student; // toString()
    
    return res;
    
  }
  
}





















