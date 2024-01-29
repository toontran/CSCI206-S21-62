public class CircusClown extends Clown {
    CircusClown(String name) {
	super(name);
    }

    public void dance() { 
	System.out.println( name + " hops up and down\n"); 
    }
}
