public class House {
    public Door[] doors;
    public String owner;
    public Sofa mySofa;
    public int[] phoneBook;
    public int	myPhoneNum;
    public TV	myTV;

    public House() { }
    
    public House(House that) {
        // this.numHinges = that.numHinges;
        // this.lockable = that.lockable;
        this.doors = new Door[that.doors.length];
        for (int i = 0; i < that.doors.length; i++) {
            this.doors[i] = new Door(that.doors[i]);
        }
        this.owner = new String(that.owner);
        this.mySofa = new Sofa(that.mySofa);
        this.phoneBook = new int[that.phoneBook.length];
        for (int j = 0; j < that.phoneBook.length; j++) {
            this.phoneBook[j] = that.phoneBook[j];
        }
        this.myPhoneNum = that.myPhoneNum;
        this.myTV = new TV(that.myTV);
    }

    public String toString() {
	String s = owner + "'s house.\n";

	s += doors.length + " doors:\n";
	for (Door door : doors) 
	    s += "\t" + door.toString() + "\n";
	
	s += "Sofa: " + mySofa.toString() + "\n";
	s += "TV: " + myTV.toString() + "\n";
	
	s += "Home phone: " + myPhoneNum + "\n";
	s += "Phone Book: \n";
	for (int i : phoneBook)
	    s += "\t" + i + "\n";
	s += "\n";
	return s;
    }
}
