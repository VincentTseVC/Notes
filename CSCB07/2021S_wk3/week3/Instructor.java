package week3;

public class Instructor extends Person {
  
  private int empId;
  
  public Instructor(String firstName, String lastName, int empId) {
    super(firstName, lastName);
    this.empId = empId;
  }

  public int getEmpId() {
    return empId;
  }

  public void setEmpId(int empId) {
    this.empId = empId;
  }
  
  @Override
  public String toString() {
    return super.toString() + " " + this.empId;
  }

}
