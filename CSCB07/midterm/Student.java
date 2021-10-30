package midterm;

public class Student extends Person implements Comparable<Student> {
  
  double cgpa;
  
  boolean inCSPOSt;
  
  boolean passedCSCA48;
  
  boolean passedCSC207;

  public Student(int sin, String name, double cgpa, 
      boolean inCSPOSt, boolean passedCSCA48, boolean passedCSC207) {
    super(sin, name);
    this.cgpa = cgpa;
    this.inCSPOSt = inCSPOSt;
    this.passedCSCA48 = passedCSCA48;
    this.passedCSC207 = passedCSC207;
    Administration.getInstance().addStudent(this);
  }
  
  @Override
  public String toString() {
    return super.toString() + ", cgpa: " + cgpa;
  }

  @Override
  public int compareTo(Student other) {
    int nameDiff = this.compareName(other);
    
    if (nameDiff == 0) {
      if (this.cgpa > other.cgpa)
        return 1;
      else if (this.cgpa == other.cgpa)
        return 0;
      else
        return -1;
    }
    
    return nameDiff;
    
  }
}
