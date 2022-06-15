package assignment;

public class Demo {
  public static void main(String [] args) {

    Mesh mesh = new Mesh();

    mesh.setReader(new OBJMeshReader());

    mesh.readFromFile("car.obj");

    mesh.rotateYAxis(Math.PI/3);

    mesh.setWriter(new OBJMeshWriter());

    mesh.writeToFile("car_rotated.obj");

//    mesh.setWriter(new PLYMeshWriter());
//
//    mesh.writeToFile("/Users/rawad/car_rotated.ply");

    }
}
