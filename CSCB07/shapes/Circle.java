package shapes;

public class Circle extends Shape {
  
  private float r;
  private float l;
  
  public Circle(float r, float l) {
    this.r = r;
    this.l = l;
  }

  @Override
  public float area() {
    return (float) (r * l * 3.14);
  }
  
  
}
