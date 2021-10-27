package assignment;

import java.util.HashSet;
import java.util.LinkedHashSet;

public class Demo {
  
  public static void main(String [] args) {

    Mesh mesh = new Mesh();

    mesh.setReader(new OBJMeshReader());

    mesh.readFromFile("car.obj");
    
    mesh.rotateYAxis(Math.PI/3);
   
    mesh.setWriter(new OBJMeshWriter());

    mesh.writeToFile("car_rotated.obj");

//    mesh.setWriter(new PLYMeshWriter());
//    mesh.writeToFile("/Users/rawad/car_rotated.ply");
    
    double theta = Math.PI/3;
    Vertex v = new Vertex(3.8,1.4,0.5 );
    double[][] Ry = {
        {Math.cos(theta), 0, Math.sin(theta)},
        {0, 1, 0},
        {-Math.sin(theta), 0, Math.cos(theta)}
    };
    
//    v.transform(Ry);
//    v.rotateYAxis(theta);
    LinkedHashSet<Vertex> vs = new LinkedHashSet<Vertex>();
    vs.add(v);
    
    Polygon p = new Polygon(vs);
    
    HashSet<Polygon> ps = new HashSet<Polygon>();
    ps.add(p);
    
    Mesh m = new Mesh();
    m.polygons = ps;
    
    m.rotateYAxis(theta);
    
    System.out.println(v);
    
    m.setWriter(new OBJMeshWriter());
  
    m.writeToFile("t.obj");
    

  }
}
