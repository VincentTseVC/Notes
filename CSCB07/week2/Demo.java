package week2;

import shapes.Circle;
import shapes.Rectangle;
import shapes.Shape;
import shapes.Square;

public class Demo {
  
  public static int add(int x, int y) {
    return x + y;
  }

  public static void main(String[] args) {
    // TODO Auto-generated method stub
    
    System.out.println("hello world");
    
    // primitive type (value type)
    // nothing else, but just a value
    // the variable only store the value itself, in the "STACK"
    
    int a = 5;
    float f = 1;
    double d = 5.0000;
    long l = 100000000;
    boolean t = true;
    char c = 'A';
    
    System.out.println(a + c);
    System.out.println(a == d);
    
    
    // Reference Type
    // think as a compound data type in c (struct)
    // has different fields, and methods, not just a value
    // it is created in the "HEAP",  using something like .. calloc() 
    // ** the variable store the "memory address of the object"
      
    
    String s1 = new String("CSCB07");
    String s2 = new String("CSCB07");
    
    String s3 = "CSCB07"; // short-cut of creating a string
    
    // Java will first look at the string-pool, 
    // and see if it can reference to an existing one to save space.
    // if not, then create a new one
    String s4 = "CSCB07";
    
    
    // same object ?
    System.out.println(s1 == s2);       // false
    System.out.println(s1 == s3);       // false
    
    System.out.println(s3 == s4);       // True ******
    
    
    // same content?
    System.out.println(s1.equals(s2));  // true
    System.out.println(s1.equals(s3));  // true
    
    
    // calling a function
    System.out.println(add(1, 3));
    
    // index for loop
    for (int i = 0; i < 5; i++) {
      System.out.println(i);
    }
    
    // 
    
    Rectangle r1 = new Rectangle(10, 20);
    
    System.out.println("num: " + Shape.numberOfShapes);
        
    Rectangle r2 = new Rectangle();
    r2.setLength(20);
    
    Rectangle r3 = new Rectangle(10, 6);
    
    System.out.println("num: " + Shape.numberOfShapes);
    System.out.println("num: " + Shape.numberOfShapes);
    System.out.println("num: " + Shape.numberOfShapes);

    System.out.println("area: " + r1.area());
    
    Square r4 = new Square(15);
    
    System.out.println(r4.getLength());
    System.out.println(r4.area());
    
    
    System.out.println(r1);
    System.out.println(r4);
    
    String msg = "hello, " + r4;
    System.out.println(msg);
    
    
    
    String[] names = {"vc", "tofu", "tommy", "B", "jason"};
    
    // for _______ in _____:
    for (String name : names) {
      System.out.println(name);
    }
    
    
   Shape[] shapes = {new Rectangle(), new Square(15), new Circle(2, 10)};
   
   for (Shape shape : shapes) {
     System.out.println("area: " + shape.area());
   }
  }

}






















