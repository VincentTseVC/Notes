package midterm;

public class EligibleCSC207 implements Eligible {

  @Override
  public boolean isEligible(Student student) {
    return student.passedCSCA48 && (student.cgpa >= 3.5 || student.inCSPOSt) && !student.passedCSC207;
  }

}
