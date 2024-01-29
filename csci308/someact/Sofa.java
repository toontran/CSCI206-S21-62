
public class Sofa {
    Color color;

    public Sofa() {  
    }
    
    public Sofa(Sofa that) {
        this.color = that.color;
    }

    public String toString() {
        return color + " colored";
    }
}
