
import java.util.*;

class ll1 {
    public static void main (String [] args) {
        var numbers = new LinkedList<Integer>();
        numbers.add (10);
        numbers.add (0, 20);
        numbers.remove (0);
        numbers.add (20);
        System.out.printf ("%s\n", numbers);
    }
}

