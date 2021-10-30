package midterm;

public abstract class Person {
  int sin;
  String name;
  
  public Person(int sin, String name) {
    this.sin = sin;
    this.name = name;
  }
  
  @Override
  public boolean equals(Object obj) {
    if (obj == null)
      return false;
    if (getClass() != obj.getClass())
      return false;
    Person other = (Person) obj;
    return sin == other.sin;
  }
  
  @Override
  public int hashCode() {
    return sin;
  }
  
  @Override
  public String toString() {
    return name;
  }
  
  public int compareName(Person other) {
    if (other == null) 
      throw new IllegalArgumentException();
    return this.name.compareTo(other.name);
  }
  
}


