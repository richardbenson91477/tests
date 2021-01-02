
import java.util.*;

class al1 {
    public static void main (String [] args) {
        var t = new ArrayList <String> (Arrays.asList ("Yo", " Dawg"));
        var u = t;
        t.add (" Heard");
        u.add (" You\n");
        for (String s : t)
            System.out.printf ("%s", s);
    }
}

