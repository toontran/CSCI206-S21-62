// Needs Clown and CircusClown
public class TestBinding {

    public static void main(String[] args) {
	Clown carl = new Clown("Carl"); // Here's Carl
	// Clowns twirl
	carl.dance(); // Make Carl dance.

	CircusClown joe = new CircusClown("Joe");
	// Circus Clowns hop
	joe.dance(); // Make Joe dance.
    
        // Implicit Coercion
	Clown bob = new CircusClown("Bob");
	// Does bob twirl or hop?
	bob.dance(); 

        // Explicit Coercion
	Clown joeJr = (Clown) joe;
	// Does joeJr twirl or hop?
	joeJr.dance();
    }
}
