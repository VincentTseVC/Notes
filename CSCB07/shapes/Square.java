package shapes;

public class Square extends Rectangle {
 
  public Square(float side) {
    // System.out.println("sq-con");
    
    
    // call the parent's constructor
    super(side, side);
    
  }
  
  @Override
  public String toString() {
    return "I am a Square with side: " + getLength();
  }
  
}
