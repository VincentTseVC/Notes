package midterm;

public class Professor extends Person {

  public Professor(int sin, String name) {
    super(sin, name);
    Administration.getInstance().addProfessor(this);
  }
  
  @Override
  public String toString() {
    return "Prof. " + super.toString();
  }
}




