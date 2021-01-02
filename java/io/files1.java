
import java.util.*;
import java.io.*;

class files1 {
    public static void main (String [] args) {
        var f_in = new File (".", "in.txt");
        if (f_in == null) {
            System.out.printf ("f_in == null\n");
            return;
        }
        var f_out = new File (".", "out.txt");
        if (f_out == null) {
            System.out.printf ("f_out == null\n");
            return;
        }
        if (f_out.exists ()) {
            System.out.printf ("note: f_out existed\n");
        }

        try {
            InputStream stream_in = new FileInputStream (f_in);
            OutputStream stream_out = new FileOutputStream (f_out);
            byte[] b = new byte[stream_in.available ()];
            stream_in.read (b);
            stream_out.write (b);
            stream_in.close ();
            stream_out.close ();
        } catch (IOException e) {
            System.out.printf ("fout_error: ");
            System.out.printf (e.toString ());
            System.out.printf ("\n");
        }
    }
}

