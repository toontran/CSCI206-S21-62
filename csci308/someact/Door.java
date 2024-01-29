public class Door {
    int numHinges;
    boolean lockable;

    public Door() {  }
    
    public Door(Door that) {
        this.numHinges = that.numHinges;
        this.lockable = that.lockable;
    }

    public String toString() {
	if (lockable)
	    return "Lockable with " + numHinges + " hinges";
	else
	    return "Plain with " + numHinges + " hinges";	
    }
}
