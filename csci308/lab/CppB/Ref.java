public class Ref{

    public boolean mybool = true;
    private int myint = 8; 

    public void print() {
        System.out.printf("%b %d\n", this.mybool, this.myint);
    }

    public void change(int i) {
        this.myint = i;
    } 

    public static void main(String[] args) {
      Ref obj1 = new Ref(); 
      Ref obj2 = obj1;

      obj1.print();
      obj2.print();
      obj1.change(42); // change a member data to 42
      obj1.print();
      obj2.print();
    }
}
