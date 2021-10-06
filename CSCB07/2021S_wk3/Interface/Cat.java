package Interface;

public class Cat extends Animal implements Fuckable {

  public Cat(String name) {
    super(name);
  }

  @Override
  public void fuck() {
    System.out.println("喵喵喵");
  }

}
