
package throw1;
import throw1.mythrow;

public class try2 {
    public static void main (String [] args) {
        try {
            throw new mythrow ();
        }
        catch (mythrow t) {
            System.out.println ("t.x is " + t.x);
        }
    }
}

