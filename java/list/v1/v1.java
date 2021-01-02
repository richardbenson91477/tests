
import java.util.*;

class v1 {
    public static void main (String [] args) {
        //Vector <Integer> numbers = new Vector <Integer> (Arrays.asList (3, 4));
        var numbers = new Vector<Integer>(Arrays.asList (3, 4));
        numbers.add (1);
        numbers.add (2);
        System.out.printf ("%s\n", numbers);
        for (Integer n : numbers) {
            System.out.printf ("%s\n", n);
        }
    }
}

