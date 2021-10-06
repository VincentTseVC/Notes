package week3;

public class NumericGrade extends Grade {

  private double grade;
  
  public NumericGrade(double grade) {
    this.grade = grade;
  }

  @Override
  public double gpa() {
    if (grade >= 85) return 4.0;
    if (grade >= 80) return 3.7;
    // .....
    return 0.0;
  }
  
}
