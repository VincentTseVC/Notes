package shapes;

public class Rectangle extends Shape {
  
  // fields, properties, attributes, instance variable 
  
  private float length;
  private float width;
  
  // Constructor
  public Rectangle(float length, float width) {
    this.length = length;
    this.width = width;
  }
  
  // method overload
  // same method name, same return type, diff # of params, diff params type
  public Rectangle() { 
//    System.out.println("rec-con");
    // default values
    length = 10;
    width = 10;
  }
  
  
  // Accessors, Getters Setters
  public float getLength() {
    return length;
  }

  public void setLength(float length) {
    this.length = length;
  }

  public float getWidth() {
    return width;
  }

  public void setWidth(float width) {
    this.width = width;
  }
  
  @Override
  public float area() {
    return length * width;
  }
  
  
  public String toString() {
    return "I am a Rectangle with length: " + length + " and width: " + width; 
  }
}
















