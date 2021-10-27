package assignment;

public class Vertex extends GraphicalObject {
  private double x;
  private double y;
  private double z;
  
  public Vertex(double x, double y, double z) {
    this.x = x;
    this.y = y;
    this.z = z;
  }

  @Override
  public void transform(double[][] R) {
    System.out.println("tranforming Vertex");
    double x_ = (x * R[0][0]) + (y * R[0][1]) + (z * R[0][2]);
    double y_ = (x * R[1][0]) + (y * R[1][1]) + (z * R[1][2]);
    double z_ = (x * R[2][0]) + (y * R[2][1]) + (z * R[2][2]);
    x = x_;
    y = y_;
    z = z_;
  }
  
  @Override
  public boolean equals(Object o) {
    
    if (o == null)
      return false;
    
    if (o == this) 
      return true;
    
    if (!(o instanceof Vertex)) 
      return false;
    
    Vertex other = (Vertex) o;
    
    return this.x == other.x && this.y == other.y && this.z == other.z;
  }
  
  @Override
  public int hashCode() {
    return (int) (x + y + z);
  }
  
  @Override
  public String toString() {
    return String.format("%f %f %f", x, y, z);
  }
  
}
