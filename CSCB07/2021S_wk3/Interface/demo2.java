package Interface;

public class demo2 {
  

  public static void fuck(Fuckable a, Fuckable b) {
    a.fuck();
    b.fuck();
  }

  public static void main(String[] args) {
    // TODO Auto-generated method stub
    
    fuck(new Cat("vc"), new Dog("tommy"));
    
    
    
  }

}
