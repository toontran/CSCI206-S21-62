public class TV {
    int width;
    int height;

    public TV() {  }

    public TV(TV that) {
        this.width = that.width;
        this.height = that.height;
    }
    public String toString() {
	return "W " + width + " H " + height;
    }
   
}
