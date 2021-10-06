package week3;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Stack;

public class Demo {

  public static void main(String[] args) {
    
//    ArrayList<String> list = new ArrayList<String>();
//    list.add(new String("B07"));
//    list.add(new String("A"));
//    list.add(new Integer(1));
    
//    List<Grade> grades = new ArrayList<Grade>();
    // List<Grade> grades = new LinkedList<Grade>();
    List<Grade> grades = new Stack<Grade>();
//     grades.add(new Grade());
    grades.add(new NumericGrade(99.0));
    grades.add(new LetterGrade("A"));
    
    
    
   
    
    
    Student tommy = new Student("Tommy", "Tse", "1234567890");
    Student prince = new Student("prince", "ss", "666666666");
    
    Instructor vc = new Instructor("Vicnent", "Tse", 1);
    
    System.out.println(tommy);
    System.out.println(vc);
    
    
    Course a48 = new Course("CSCA48", 10);
    a48.setInstructor(vc);
    
    Course b07 = new Course("CSCB07", 10);
    
    a48.enroll(tommy);
    prince.enroll(a48);
    prince.enroll(b07);
    
    System.out.println(a48);
    
    
    tommy.addGrade(a48, 99.0);
    
    prince.addGrade(a48, 84.0);
    prince.addGrade(b07, "A+");
    
    System.out.println(prince.cgpa());
    
    
    // d = {'vc': 4.0, 'anya': 0.7}
    // >>> d['vc']
    // >>> 4.0
    
    
    
    

  }

}
