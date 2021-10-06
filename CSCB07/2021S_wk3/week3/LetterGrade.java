package week3;

public class LetterGrade extends Grade {
  
  private String grade;
  
  public LetterGrade(String grade) {
    this.grade = grade;
  }

  @Override
  public double gpa() {
    if (grade.equals("A") || grade.equals("A+"))
      return 4.0;
    if (grade.equals("A-")) return 3.7;
    if (grade.equals("B+")) return 3.3;
    // ....
    
    return 0.0;
  }
  
}
