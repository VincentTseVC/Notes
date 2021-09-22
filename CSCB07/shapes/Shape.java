package shapes;

// abstract class works the same as regular class.
// EXCEPT it CANNOT be created.. 
//   [x]   Shape x = 'new Shape()'
public abstract class Shape {
  
  public static int numberOfShapes = 0;
  
  
  public Shape() {
    numberOfShapes++;
  }

  
  public String toString() {
    return "Fuck Im a Shape";
  }
  
  // abstract method.
  // If forces any child class that extends this 'Shape' class, 
  // MUST Complete the body of this area() method
  public abstract float area();
}
