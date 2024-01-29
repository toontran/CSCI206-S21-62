public class Main {

    public static void main(String[] args) {
	House h = new House();

	h.doors = new Door[2];
	h.doors[0] = new Door();
	h.doors[0].numHinges = 2;
	h.doors[0].lockable = false;
	h.doors[1] = new Door();
	h.doors[1].numHinges = 3;
	h.doors[1].lockable = true;
    
	h.owner = "Samantha";

	h.mySofa = new Sofa();
	h.mySofa.color = Color.Orange;

	h.phoneBook = new int[3];
	h.phoneBook[0] = 5771234;
	h.phoneBook[1] = 5774567;
	h.phoneBook[2] = 5777890;

	h.myPhoneNum = 5771234;
    
	h.myTV = new TV();
	h.myTV.height = 35;
	h.myTV.width = 70;

	House h2 = new House(h);  /**** EDIT THIS LINE TO CALL COPY CONSTRUCTOR ****/ 
	House h3 = new House(h2); /**** EDIT THIS LINE TO CALL COPY CONSTRUCTOR ****/ 

	h.doors[0].numHinges = 3;
	h.doors[1].lockable = false;
	h.owner = "George";
	h.mySofa.color = Color.Blue;
	h.phoneBook[1] = 5771357;
	h.myPhoneNum = 5777890;
	h.myTV.height = 50;

	h2.doors = new Door[1];
	h2.doors[0] = new Door();
	h2.doors[0].numHinges = 4;  // its a dutch door
	h2.doors[0].lockable = true;

	h3.phoneBook[2] = 5774321;

	System.out.println(h);
	System.out.println(h2);
	System.out.println(h3);
    }
}
